# Sets up a flask server to host an app used to view and rename fotos

from flask import Flask
from flask import request 

app = Flask(__name__)

@app.route('/')
def is_running():
    return("Flask is running")


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Werkzeug server not running')
    func()
        
    
@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down'   

    
if __name__ == '__main__':
   app.run()