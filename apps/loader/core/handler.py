from apps.loader.core.process import OnDemandProcess
from apps.loader.core.components.reader.exceptions import *
from pydantic import ValidationError
from apps.api.api_responser import ApiResponser


class OnDemandHandler:

    @staticmethod
    def run(request):
        try:
            p = OnDemandProcess(request)
            p.run()
        except ValidationError as e:
            return ApiResponser.bad_format_response(e.json())
        except (InvalidColumnName, InvalidFileError, InvalidJsonlFileError, InvalidEncodingFormatError) as e:
            return ApiResponser.bad_request_response(str(e))
        except Exception as e:
            return ApiResponser.error_response(e)
        else:
            return ApiResponser.success_response()
