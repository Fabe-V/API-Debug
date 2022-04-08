from flask import *
import json
from flask_cors import CORS
import routes

app = Flask(__name__)


CORS(app)
cors = CORS(app, resources={
    r"/*": {
       "origins": "*"
    }
})

@app.route('/', methods=['GET'])
def route():

    json_output = json.dumps(routes.route)

    return json_output

@app.route('/py/', methods=['GET'])
def apd():

    json_output = json.dumps(routes.py)

    return json_output



if __name__ == '__main__':
    app.run(port=2002)