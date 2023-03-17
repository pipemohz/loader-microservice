from abc import ABC, abstractmethod


class BaseProcess(ABC):
    def __init__(self, request) -> None:
        self._request = request
        self._args = request.form.to_dict()

    @abstractmethod
    def run(self):
        """
        Method intended to implement process logic
        """
        pass
