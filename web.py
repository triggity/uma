import flask
import pymongo
import json
# from flask.ext.pymongo import PyMongo
import bson
from bson import json_util

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, bson.ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = flask.Flask(__name__)
mongo = pymongo.MongoClient("172.17.0.2", 27017)
encoder = JSONEncoder()

@app.route("/foo")
def home_page():
    online_users = mongo.test.restaurants.find_one()
    print online_users
    return json.dumps( online_users, default=json_util.default)
    # return encoder.encode(online_users)

if __name__ == "__main__":
    print "ASDFASDFASFD"
    app.run(debug=True)
