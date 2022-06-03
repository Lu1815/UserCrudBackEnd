from distutils.log import debug
import resource
from flask import Flask
from flask_cors import CORS, cross_origin

from config import config;

#Routes
from routes import User

app = Flask(__name__)
cors = CORS(app, resources = {r'/*': {"origins": "*"}})

def page_not_found(error):
    return '<h1>Page not found :(</h1>', 404

@app.route('/', methods = ['GET'])
def index():
    return 'Hello world!'

if __name__ == "__main__":
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(User.main, url_prefix = '/api/users')

    #Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(debug==True)