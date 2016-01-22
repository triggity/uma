import os

import flask
from flask import request
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

mongo_location = os.environ.get("MONGO_LOCATION")
PORT = int(os.environ.get("PORT", 8086)  )
app = flask.Flask(__name__)
mongo = pymongo.MongoClient(mongo_location, 27017)
#encoder = JSONEncoder()

def encode(items):
    return json.dumps( items, default=json_util.default)


@app.route("/restaurants", methods=["GET"])
def all_restaurants():
    restaurants = mongo.test.restaurants.find()
    items = [x for x in restaurants]
    return encode(items)

@app.route("/restaurants", methods=["POST"])
def add_restaurant():
    data = request.get_json()
    if not data.get('restaurant_id', ""):
        print "ASDFASDFASDFA"
        next_id = get_next_id()
        print next_id
        data['restaurant_id'] = next_id
    item = mongo.test.restaurants.insert(data)
    return encode(data['restaurant_id'])

def get_next_id():
    lst = mongo.test.restaurants.find().sort([("restaurant_id",-1)])
    item = lst.next()
    cur_id = item['restaurant_id']
    return int(cur_id) + 1

@app.route("/restaurants/<id>", methods=["GET"])
def get_restaurant(id):
    restaurant = mongo.test.restaurants.find_one({ "restaurant_id": id })
    print restaurant
    return encode(restaurant)

@app.route("/restaurants/<id>", methods=["PUT"])
def put_restaurant(id):
    data = request.get_json()
    restaurant = mongo.test.restaurants.update({ "restaurant_id": id }, data)
    print restaurant
    return encode(restaurant)

@app.route("/restaurants/<id>", methods=["DELETE"])
def delete_restaurant(id):
    restaurant = mongo.test.restaurants.remove({ "restaurant_id": id })
    return encode(restaurant)
if __name__ == "__main__":
    print "ASDFASDFASFD"
    app.run(debug=True, port=PORT, host="0.0.0.0")
