from flask import Flask

from . import views


app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object('config.default')

# Tru to load the configuration from the instance folder
try:
    app.config.from_pyfile('config.py')
except FileNotFoundError:
    pass

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE')   

app.register_blueprint(views.blueprint)
