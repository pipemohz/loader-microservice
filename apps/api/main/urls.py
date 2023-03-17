from apps.api.main import main
from flask_json import json_response


@main.route('/')
def index():
    return json_response(
        message="File loader service"
    )


@main.route('/health')
def health():
    return json_response(
        message="OK"
    )
