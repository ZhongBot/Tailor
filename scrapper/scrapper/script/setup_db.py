from scrapper.model.user import *
from scrapper.config.db_config import connect_to_mongo, disconnect_from_mongo

def setup_user(db, name):
    collection = 'user'
    u = user()
    u.user_name = name
    u.defaultMembership()
    print u.to_dict()
    db[collection].insert(u.to_dict())

if __name__ == '__main__':
    db = connect_to_mongo()
    name = 'admin'
    setup_user(db, name)
