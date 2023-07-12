from flask import Flask     
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_assets import Environment
from config import Config
import cloudinary
from flask_cors import CORS
from flask_session import Session
from flask_jwt_extended import JWTManager

app = Flask(__name__, template_folder='templates')
cors = CORS(app, resources={r"*": {"origins": "*"}})

app.static_folder = 'static'

assets = Environment(app)

app.config.from_object(Config)
db = SQLAlchemy(app)
assets = Environment(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


jwt = JWTManager(app)

cloud=cloudinary.config(
    cloud_name = "df4pjo2rj",
    api_key = "686419874229111",
    api_secret = "QU5NQ3VXujb51b7Z8gQyBjx0T9A"
)

from app.models import dataTokohModel, userModel
from app import routes