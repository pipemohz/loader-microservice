from decouple import config

ENVIRONMENT = {
    'FLASK_APP': config('FLASK_APP', None),
    'APP_ENV': config('APP_ENV', None),
    'DEBUG': config('DEBUG', False),
    'TIMEZONE': config('TIMEZONE', 'America/Bogota'),
    'PRODUCT': config('PRODUCT', 'aliatu')
}

MULTIGET_MAX_ITEMS = config('MULTIGET_MAX_ITEMS', default=20, cast=int)

FORMATS = config('FORMATS', cast=lambda v: [s.strip() for s in v.split(',')])
