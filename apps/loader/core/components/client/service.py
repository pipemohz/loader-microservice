from apps.common.service import BaseService
from concurrent.futures import ThreadPoolExecutor, as_completed
from apps.common.requests import get_request
from config.environment import MULTIGET_MAX_ITEMS
from apps.common.utils.localize import local_now
from apps.common.models.records import Record
from apps.api import db
import re


class Service(BaseService):
    def setup(self, **kwargs):
        self._services = kwargs['steps']

    def run(self):
        self._data = self.orchestrator.payload['service.reader']['data']
        self._block_size = MULTIGET_MAX_ITEMS
        self.blocks = list()

        try:
            for service in self._services:
                self._service = service
                self._steps = service['steps']
                self.temp_data = list()
                for i in range(0, self._data.shape[0], self._block_size):
                    row = {'ids': ','.join(
                        self._data[i:i+self._block_size]['ids'].to_list())}
                    uri = self._format_uri(service['uri'], row)
                    records = self._request(
                        **{
                            'uri': uri,
                            'headers': service['headers'],
                            'placeholders': service['placeholders']
                        }
                    )

                    self.temp_data = [
                        self._task1(record)
                        for record in records
                    ]

                    # Save in db
                    self._save()
                    # Register size of records
                    self.blocks.append(len(self.temp_data))
                    # Clear after store in db
                    self.temp_data.clear()

        except Exception as e:
            raise Exception(
                f'An error has ocurred in client module: {type(e)}: {e}]')

        print(self.blocks)

    def _task1(self, record):
        with ThreadPoolExecutor() as pool:
            futures = [
                pool.submit(
                    self._task2,
                    record,
                    step
                )
                for step in self._steps
            ]

        for future in as_completed(futures):
            record.update(future.result())

        return record

    def _task2(self, record, step):
        try:
            uri = self._format_uri(step['uri'], record)
            r = self._request(
                **{
                    'uri': uri,
                    'headers': step['headers'],
                    'placeholders': step['placeholders']
                }
            )
        except Exception:
            r = [{
                placeholder['name']: None
                for placeholder in step['placeholders']
            }]

        return r[0]

    def _save(self):
        records = [
            Record(
                site=re.sub(r'\d', '', record['id']),
                item_id=re.sub(r'[A-Z]|[a-z]', '', record['id']),
                price=record['price'],
                start_time=record['start_time'],
                name=record['name'],
                description=record['description'],
                nickname=record['nickname'],
                created_at=local_now()
            )
            for record in self.temp_data
        ]

        db.session.add_all(records)
        db.session.commit()

    def _format_uri(self, uri, record):
        pattern = re.compile(r'\:\[(.*?)\]')
        result = pattern.findall(uri)

        for item in result:
            if item in record:
                uri = uri.replace(f":[{item}]", record[item])

        return uri

    def _extract_data(self, response_data, placeholders):
        data = dict()
        list_pattern = re.compile(r'\[(\d*?)\]')
        for placeholder in placeholders:
            parts = placeholder['path'].replace('$data.', '').split('.')
            json = response_data
            for part in parts:
                if part in json:
                    if list_pattern.match(part):
                        json = json.__getitem__(
                            int(re.sub(r'\[|\]', '', part)))
                    else:
                        json = json.__getitem__(part)
                else:
                    json = None
                    break

            data[placeholder['name']] = str(json) if json else None

        return data

    def _request(self, rows=None, **kwargs):
        response = get_request(**kwargs)
        data = [{}]

        if response.ok:
            if type(response.json()) is list:
                data = [
                    self._extract_data(r, kwargs['placeholders'])
                    for r in response.json()
                    if r['code'] == 200
                ]
            else:
                data = [self._extract_data(
                    response.json(), kwargs['placeholders'])]

        return data
