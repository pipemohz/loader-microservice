from flask import Blueprint

loader = Blueprint('loader', __name__, url_prefix='/api/v1')

from apps.api.loader import urls