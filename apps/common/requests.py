from requests import Response
from requests import get
from requests.exceptions import HTTPError


class UnavailableResponse(Response):
    def __init__(self) -> None:
        super().__init__()
        self.status_code = 504


def get_request(**kwargs):
    try:
        response = get(
            kwargs['uri'],
            headers=kwargs['headers'],
            timeout=2
        )

        response.raise_for_status()

    except HTTPError:
        print(f'Error -- URL:{response.url} code: {response.status_code}')
    except Exception as e:
        print(f'Error -- Request to {kwargs["uri"]} thrown exception:  {e}')
        return UnavailableResponse()
    else:
        print(f'Success -- URL:{response.url} code: {response.status_code}')

    return response
