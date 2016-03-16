import pymongo

class mongo_conn(object):
    uri = 'mongodb://127.0.0.1/Tailor'
    collection = 'Tailor'

def connect_to_mongo():
    client = pymongo.MongoClient(mongo_conn.uri)
    db = client[mongo_conn.collection]
    return db

def disconnect_from_mongo(db):
    db.client.close()
