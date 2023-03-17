from apps.common.utils.components import absolute_component_factory_module


class BaseOrchestrator:
    def __init__(self, rule, base_data=None) -> None:
        self.rule = rule
        self.base_data = base_data
        self.payload = dict()
        self.set_services()

    def component_factory_module(self, component: str):
        path_component = f'{self.path}.components.{component}'
        return absolute_component_factory_module(path_component)

    def set_services(self):
        self.services = list()
        for component in self.rule['steps']:
            if component['active'] is True:
                module = self.component_factory_module(component['component'])
                service = module.Service(
                    component['alias'],
                    self
                )
                if 'steps' in component:
                    service.setup(steps=component['steps'])
                self.services.append(service)

    def execute(self):
        for s in self.services:
            s.run()
