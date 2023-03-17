from apps.loader.core.tests.base_test import BaseTest
from apps.loader.core.components.formatter.service import Service
from pydantic import ValidationError


class TestFormatter(BaseTest):
    test_name = 'Formatter tests'

    @classmethod
    def set_up_class(cls):
        cls.read_input_files()

    @property
    def component_name(self):
        return 'formatter'

    @property
    def service_class(self):
        return Service

    def test_valid_format(self):
        self.service.orchestrator.base_data = {
            'file': self.files['test_txt'],
            'config': {'format': 'txt', 'encoding': 'utf8'}
        }
        self.service.run()
        assert self.service.temp_data
        assert self.service.temp_data == {
            'format': 'txt', 'encoding': 'utf8', 'separator': ','}

    def test_auto_format(self):
        self.service.orchestrator.base_data = {
            'file': self.files['test_txt'],
            'config': dict()
        }
        self.service.run()
        assert self.service.temp_data
        assert self.service.temp_data == {
            'format': 'txt', 'encoding': 'utf8', 'separator': ','}

    def test_validation_error(self):
        self.service.orchestrator.base_data = {
            'file': self.files['test_txt'],
            'config': {'format': 'foo', 'extra': 'value'}
        }
        with self.assertRaises(ValidationError):
            self.service.run()
