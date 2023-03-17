from apps.loader.core.orchestrator import ServiceOrchestrator
from apps.common.process import BaseProcess
from apps.loader.core.rule_process import RuleProcess


class OnDemandProcess(BaseProcess):

    def run(self, **kwargs):
        r = {
            "uuid": "a3b1e556-0044-4501-973f-3bebc730bdf2",
            "slug": "service",
            "version": 1,
            "steps": [
                    {
                        'component': 'formatter',
                        'alias': 'service.formatter',
                        'active': True,
                    },
                {
                        'component': 'reader',
                        'alias': 'service.reader',
                        'active': True
                    },
                {
                        'component': 'client',
                        'alias': 'service.client',
                        'active': True,
                        'steps': [
                            {
                                'service_name': 'items',
                                'method': 'get',
                                'uri': '${MELI_ITEMS_API}?ids=:[ids]&attributes=id,price,start_time,category_id,currency_id,seller_id',
                                'include_row': False,
                                'headers': [],
                                'placeholders': [
                                    {
                                        'name': 'id',
                                        'path': '$data.body.id'
                                    },
                                    {
                                        'name': 'price',
                                        'path': '$data.body.price'
                                    },
                                    {
                                        'name': 'start_time',
                                        'path': '$data.body.start_time'
                                    },
                                    {
                                        'name': 'category_id',
                                        'path': '$data.body.category_id'
                                    },
                                    {
                                        'name': 'currency_id',
                                        'path': '$data.body.currency_id'
                                    },
                                    {
                                        'name': 'seller_id',
                                        'path': '$data.body.seller_id'
                                    },
                                ],
                                'steps': [
                                    {
                                        'service_name': 'categories',
                                        'method': 'get',
                                        'uri': '${MELI_CATEGORIES_API}/:[category_id]?attributes=name',
                                        'headers': [],
                                        'placeholders': [
                                            {
                                                'name': 'name',
                                                'path': '$data.name'
                                            }
                                        ]
                                    },
                                    {
                                        'service_name': 'currencies',
                                        'method': 'get',
                                        'uri': '${MELI_CURRENCIES_API}/:[currency_id]?attributes=description',
                                        'headers': [],
                                        'placeholders': [
                                            {
                                                'name': 'description',
                                                'path': '$data.description'
                                            }
                                        ]
                                    },
                                    {
                                        'service_name': 'users',
                                        'method': 'get',
                                        'uri': '${MELI_USERS_API}/:[seller_id]?attributes=nickname',
                                        'headers': [],
                                        'placeholders': [
                                            {
                                                'name': 'nickname',
                                                'path': '$data.nickname'
                                            }
                                        ]
                                    },
                                ]
                            }
                        ]
                    },
            ]
        }

        rule = RuleProcess(r).rule

        orchestrator = ServiceOrchestrator(
            rule=rule,
            base_data={
                'file': self._request.files['file'],
                'config': self._args
            }
        )
        orchestrator.execute()
