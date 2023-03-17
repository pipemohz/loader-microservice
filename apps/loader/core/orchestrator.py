from apps.common.orchestrator import BaseOrchestrator


class ServiceOrchestrator(BaseOrchestrator):
    path = __name__.replace('.orchestrator', '')
