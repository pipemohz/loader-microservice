from apps.api.loader import loader
from apps.loader.core.handler import OnDemandHandler
from flask_json import json_response
from flask import request


@loader.route('on_demand', methods=['POST'])
def on_demand():
    if request.files.get('file'):
        response = OnDemandHandler.run(request)
        return response
    else:
        return json_response(
            status_=400,
            message='File not loaded.'
        )
