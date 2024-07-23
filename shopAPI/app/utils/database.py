import pymongo
from decouple import config

def get_database():
    client = pymongo.MongoClient(config("MONGODB_URL"))
    return client.bhx
