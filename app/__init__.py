from flask import Flask
from .routes import home, dashboard # or app.routes, same thing
from app.db import init_db

def create_app(test_config=None):
  # setup config
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )

  @app.route('/hello')
  def hello():
    return 'hello world'

  # register routes 
  app.register_blueprint(home)
  app.register_blueprint(dashboard)

  init_db(app) # pass in app

  return app