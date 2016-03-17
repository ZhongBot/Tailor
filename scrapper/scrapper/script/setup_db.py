from scrapper.model.user import *
from scrapper.model.purchase_history import *
from scrapper.config.db_config import connect_to_mongo, disconnect_from_mongo

def setup_user(db, name):
    collection = 'user'
    u = user()
    u.user_name = name
    u.defaultMembership()
    content =  u.to_dict()
    try:
        db[collection].insert(content)
    except:
        print 'Unable to create %s'% name
    print 'Created user %s'%name
    
    return u

def add_purchase(co, user, color_s=2, complexity_s=2, size_s=3, cond={}):
    '''
    Associate a user with a purchase.
    Update the user's membership_funcs based on user's ratings.
    '''
    if len(cond.items()) == 0:
        product = co.find_one()
    else:
        product = co.find(cond)
    if len(product) == 0:
        print "couldn't find a product"
        return False, None
    price = [
                product.get('full_price', None), 
                product.get('discounted_price', None)
            ]
    func = lambda p: float(p.split(' ')[0][1:]) if p else -1 
    price = map(func, price)
    if min(price) > 0:
        price = min(price)
    else:
        price = max(price)
    
    purchase = user_purchase(user['_id'],
                             product['_id'],
                             price
                            )
    purchase.populate_fuzzy_ratings(color_s, complexity_s, size_s)
    purchase.price = price
    entry = purchase.to_dict()
    db['purchase_history'].insert(entry)
    return True, purchase

if __name__ == '__main__':
    db = connect_to_mongo()
    name = 'admin'
    #user = setup_user(db, name)
    add_purchase(db['tops'], db['tops'].find_one({}))
