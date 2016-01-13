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

app = flask.Flask(__name__)
mongo = pymongo.MongoClient("172.17.0.2", 27017)
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
    #return json.dumps( restaurant, default=json_util.default)
    # return encoder.encode(online_users)

if __name__ == "__main__":
    print "ASDFASDFASFD"
    app.run(debug=True)
