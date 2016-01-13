import flask
import pymongo
import json
# from flask.ext.pymongo import PyMongo
#import bson
from bson import json_util, ObjectId

#class JSONEncoder(json.JSONEncoder):
#    def default(self, o):
#        if isinstance(o, bson.ObjectId):
#            return str(o)
#        return json.JSONEncoder.default(self, o)

app = flask.Flask(__name__)
mongo = pymongo.MongoClient("172.17.0.2", 27017)
#encoder = JSONEncoder()

def encode(items):
    return json.dumps( items, default=json_util.default)


@app.route("/restaurants")
def all_restaurants():
    restaurants = mongo.test.restaurants.find()
    items = [x for x in restaurants]
    return encode(items)
    #return json.dumps( items, default=json_util.default)
    # return encoder.encode(online_users)

@app.route("/restaurants/<id>")
def get_restaurant(id):
    restaurant = mongo.test.restaurants.find_one({ "_id": ObjectId(id) })
    print restaurant
    return encode(restaurant)
    #return json.dumps( restaurant, default=json_util.default)
    # return encoder.encode(online_users)

if __name__ == "__main__":
    print "ASDFASDFASFD"
    app.run(debug=True)
