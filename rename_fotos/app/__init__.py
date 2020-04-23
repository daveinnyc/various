# Modified from flask sample project 
#   https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/

from flask import Flask

app = Flask(__name__)

# Needs to be after app definition to avoid namespace collisions. 
from app import routes
