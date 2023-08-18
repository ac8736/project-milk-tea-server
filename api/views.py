from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.dbClient import createDbInstance, parseMongoData
from django.conf import settings

@api_view(['GET'])
def getData(response):
    dbClient = createDbInstance(settings.MONGO_CONNECTION_STRING, settings.MONGO_DB_NAME)
    users = dbClient['users']
    ret = parseMongoData(users.find_one({'test': 'test'}))
    dbClient.client.close()
    return Response(ret)
