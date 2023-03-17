from decouple import config
import json
import re


class RuleProcess:
    def __init__(self, rule) -> None:
        self.rule = rule
        self._format_rule()

    def _format_rule(self):
        if type(self.rule) is str:
            self.rule = json.loads(self.rule)

        self._format_uri(self.rule['steps'])

    def _format_uri(self, obj):
        for step in obj:
            if 'uri' in step:
                step['uri'] = self._replace_matches(step['uri'])
            if 'steps' in step:
                self._format_uri(step['steps'])

    def _replace_matches(self, string: str):
        pattern = re.compile(r'\$\{(.*?)\}')
        for item in pattern.findall(string):
            if config(item, None):
                string = string.replace('${%s}' % item, config(item))
            else:
                raise ValueError(f'{item} not set.')
        return string
