from apps.common.service import BaseService
from apps.common.validators import FileValidator
from os.path import splitext


class Service(BaseService):
    def run(self):
        self._filename = self.orchestrator.base_data['file'].filename
        self._config = self.orchestrator.base_data['config']
        self._validator = FileValidator

        self._set_format()
        self._set_encoding()
        self._set_separator()

        config = self._validator(**self._config)
        self.temp_data = config.dict()
        self.store_temporal_data()

    def _set_format(self):
        if not 'format' in self._config:
            self._config['format'] = splitext(self._filename)[1]\
                .replace('.', '')

    def _set_encoding(self):
        if not 'encoding' in self._config:
            self._config['encoding'] = 'utf8'

    def _set_separator(self):
        if not 'separator' in self._config or self._config['format'] == 'jsonl':
            self._config['separator'] = ','
