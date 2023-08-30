from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.dbClient import createDbInstance, parseMongoData
from django.conf import settings
import json

@api_view(['GET'])
def getData(response):
    dbClient = createDbInstance(settings.MONGO_CONNECTION_STRING, settings.MONGO_DB_NAME)
    users = dbClient['users']
    ret = parseMongoData(users.find_one({'test': 'test'}))
    dbClient.client.close()
    return Response(ret)

@api_view(['GET'])
def test(response):
    return Response("test")

@api_view(['POST'])
def addLink(request):
    db = createDbInstance(settings.MONGO_CONNECTION_STRING, settings.MONGO_DB_NAME)
    test = db['test']
    user_request = json.loads(request.body)

    user_id = user_request["_id"]
    link = user_request["link"]

    filter = {"_id": user_id}
    existing_user = test.find_one(filter)

    if existing_user:
        update = {'$push': {'link': link}}
        test.update_one(filter, update)
    else:
        test.insert_one({"_id": user_id, "link": [link]})
    return Response(user_request)