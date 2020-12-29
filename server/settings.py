from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timedelta
import os

load_dotenv(dotenv_path=Path('..') / '.env')

MODE = os.getenv('MODE', 'development')

class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY", "iamthesecret")
    DEBUG = True
 
class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True