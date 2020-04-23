from flask import request
from app import app


# Test page
@app.route('/holamundo')
def holamundo():
    return 'Hola Mundo'


# Landing page
@app.route('/')
@app.route('/index')
def index():
    return "Renamer"
    

# Shutdown the server       
@app.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Werkzeug server not running')
    func()

    return 'Server shutting down' 

    
