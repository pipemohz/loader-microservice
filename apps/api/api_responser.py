from flask_json import json_response
import json


class ApiResponser:
    @staticmethod
    def error_response(exception, code: int = 500):
        response = {
            "internal_error": "An error has ocurred, "
            "contact system administrator",
            "description": str(exception)
        }

        return json_response(
            status_=code,
            data_=response
        )

    @staticmethod
    def success_response(msg='Success', code: int = 200):
        return json_response(
            message=msg,
            status_=code,
        )

    @staticmethod
    def bad_format_response(msg, code: int = 400):

        return json_response(
            status_=code,
            data_=json.loads(msg)
        )

    @staticmethod
    def bad_request_response(msg, code: int = 400):

        return json_response(
            status_=code,
            message=msg
        )
