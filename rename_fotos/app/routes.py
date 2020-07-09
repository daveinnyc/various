import os

from flask import request
from flask import render_template
from app import app


# Test page
@app.route('/holamundo')
def holamundo():
    return "Hola Mundo"


# Landing page
@app.route('/')
@app.route('/index')
def index():
    working_dir = os.getcwd()
    return working_dir
    

# Landing page - template
# @app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',
                            title="Rename Fotos",
                            description="Utility to help organize fotos")


# Shutdown the server       
@app.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Werkzeug server not running')
    func()

    return "Server shutting down" 

    
