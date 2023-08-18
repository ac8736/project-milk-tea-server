from pymongo import MongoClient
from bson import json_util
import json

def createDbInstance(connection_string, db_name):
    client = MongoClient(connection_string)
    return client[db_name]

def parseMongoData(data):
    return json.loads(json_util.dumps(data))