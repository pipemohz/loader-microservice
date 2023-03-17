from config.environment import ENVIRONMENT as env
from flask_migrate import Migrate
from apps.api import create_app, db
from flask.cli import cli

app = create_app(env['APP_ENV'] or 'default')
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=env['DEBUG'])
