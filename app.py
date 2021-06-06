from flask_pymongo import PyMongo
import flask
from flask import jsonify, request
import json
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.config["MONGO_URI"] = "mongodb://localhost:27017/restPythonDB"

mongodb_client = PyMongo(app)
db = mongodb_client.db
mycol = db["users"]

@app.route('/home', methods=['GET'])
def home():
    return "<h1> Welcome <h1>"

@app.route('/allNames', methods=['GET'])
def getAllNames():
    names = db.users.find()
    return jsonify([name for name in names])

@app.route('/addName', methods=['POST'])
def addName():
    some = request.data
    some = some.decode('utf8')
    newObj = json.loads(some)
    print(newObj)
    result = db.users.update_one({'_id': newObj['_id']},{"$set":{'name': newObj['name']}},upsert=True)
    return jsonify(result.raw_result)

app.run(host="0.0.0.0")