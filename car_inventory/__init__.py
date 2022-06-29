from flask import Flask
from config import Config
from .site.routes import site
from  .authentication.routes import auth
from .api.routes import api
from .models import db as root_db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api) 

root_db.init_app(app)

app.config.from_object(Config)

migrate = Migrate(app, root_db)