import pymongo

class mongo_conn(object):
    uri = 'mongodb://127.0.0.1/Tailor'
    collection = 'Tailor'

def connect_to_mongo(collection=False):
    client = pymongo.MongoClient(mongo_conn.uri)
    if collection:
        return client[collection]
    return client[mongo_conn.collection]

def disconnect_from_mongo(db):
    db.client.close()
