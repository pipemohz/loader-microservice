from flask import Blueprint

main = Blueprint('main', __name__)

from apps.api.main import urls