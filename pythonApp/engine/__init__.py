from flask import Flask
import datetime
import os
import sys
from .config import *
from .MongoSession import MongoSession
import pymongo

app = Flask(__name__)
DOMAIN = ".arheneos.com" if sys.platform != 'darwin' else None
app.static_folder = f"../../{staticFolder}"
app.template_folder = f"../../{templateFolder}"
app.config['JWT_KEY'] = 'secret'
app.config['JSON_AS_ASCII'] = False
app.config['SESSION_COOKIE_DOMAIN'] = DOMAIN
app.config['REMEMBER_COOKIE_DOMAIN'] = DOMAIN
app.config['REMEMBER_COOKIE_SECURE'] = sys.platform != 'darwin'
app.config['REMEMBER_COOKIE_HTTPONLY'] = sys.platform != 'darwin'
app.config['COOKIE_HTTPONLY'] = True
app.config['COOKIE_SECURE'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = datetime.timedelta(days=30)
app.config['SESSION_COOKIE_SECURE'] = sys.platform != 'darwin'
FORK_SAFE_MONGO_CLIENT = pymongo.MongoClient('localhost', 27017,
                                             **{"maxPoolSize": 1024, "connectTimeoutMS": 10000,
                                                "socketTimeoutMS": 10000,
                                                "waitQueueTimeoutMS": 10000})
app.session = MongoSession(FORK_SAFE_MONGO_CLIENT)
