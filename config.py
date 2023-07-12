import os

basedir = os.path.dirname(os.path.abspath(__file__))

class Config(object):
    HOST = "localhost"
    DATABASE = "sentimen"
    USERNAME = "root"
    PASSWORD = "hendra24"
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    SQLALCHEMY_DATABASE_URI = 'mysql://'+USERNAME+':'+PASSWORD+'@'+HOST+'/'+DATABASE

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

# #Jwt Config
# JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
# JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)

# #Path Folder
MODELS_PATH = os.path.abspath(os.path.join(__file__, "../app/static/model")) + "/"
DATASET_PATH = os.path.abspath(os.path.join(__file__, "../app/static/dataset")) + "/"
DATA_PATH = os.path.abspath(os.path.join(__file__, "../app/static/csv")) + "/"
