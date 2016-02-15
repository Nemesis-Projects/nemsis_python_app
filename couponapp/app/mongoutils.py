#MongoUtils

from datetime import datetime
from app import mongo

def getUserById():
	mongo.db.coupon.find()