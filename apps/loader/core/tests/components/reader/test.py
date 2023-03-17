from apps.loader.core.tests.base_test import BaseTest
from apps.loader.core.components.reader.service import Service
from apps.loader.core.components.reader.exceptions import InvalidFileError, InvalidEncodingFormatError, InvalidJsonlFileError, InvalidColumnName
from pandas import DataFrame


class TestReader(BaseTest):
    test_name = 'Reader tests'

    @classmethod
    def set_up_class(cls):
        cls.read_input_files()

    def setUp(self) -> None:
        super().setUp()
        self.service.orchestrator.payload['service.formatter'] = {
            'format': 'txt', 'encoding': 'utf8', 'separator': ','
        }

    @property
    def component_name(self):
        return 'reader'

    @property
    def service_class(self):
        return Service

    def test_file_read(self):
        self.service.orchestrator.base_data = {
            'file': self.files['test_txt'],
        }
        self.service.run()
        assert self.service.temp_data
        assert 'data' in self.service.temp_data
        assert type(self.service.temp_data['data']) is DataFrame

    def test_bad_file(self):
        self.service.orchestrator.base_data = {
            'file': self.files['bad_txt'],
        }

        with self.assertRaises(InvalidFileError):
            self.service.run()

    def test_bad_json_file(self):
        self.service.orchestrator.payload['service.formatter']['format'] = 'jsonl'

        self.service.orchestrator.base_data = {
            'file': self.files['bad_json'],
        }

        with self.assertRaises(InvalidJsonlFileError):
            self.service.run()

    def test_bad_encoding_format(self):
        self.service.orchestrator.payload['service.formatter']['format'] = 'csv'
        self.service.orchestrator.payload['service.formatter']['encoding'] = 'foo'

        self.service.orchestrator.base_data = {
            'file': self.files['test_csv'],
        }

        with self.assertRaises(InvalidEncodingFormatError):
            self.service.run()

    def test_bad_column(self):
        self.service.orchestrator.base_data = {
            'file': self.files['bad_column'],
        }

        with self.assertRaises(InvalidColumnName):
            self.service.run()
