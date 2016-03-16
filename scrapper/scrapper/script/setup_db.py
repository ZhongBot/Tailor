from scrapper.model.user import user
from scrapper.config.db_config import connect_to_mongo, disconnect_from_mongo

def setup_user(name):
    u = user()
    u.user_name = name
    u.defaultMembership()

if __name__ == '__main__':
    db = connect_to_mongo()
    name = 'admin'
    setup_user(db, name)
