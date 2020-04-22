# Sets up a flask server to host an app used to view and rename fotos

from flask import Flask


app = Flask(__name__)

@app.route('/')
def is_running():
    return("Flask is running")

  

    
if __name__ == '__main__':
   app.run()