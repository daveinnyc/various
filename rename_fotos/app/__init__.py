# Modified from flask sample project 
#   https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/

import os
from flask import Flask
from flask import request 

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dahf98t45y',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/holamundo')
    def hello():
        return 'Hola Mundo'


    def shutdown_server():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Werkzeug server not running')
        func()
            
        
    @app.route('/shutdown')
    def shutdown():
        shutdown_server()
        return 'Server shutting down' 

    return app
    

