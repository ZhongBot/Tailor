from scrapper.config.db_config import connect_to_mongo
from colour import Color


class InputVector():
    def __init__(self, color, price, brand, categories):
        self.colors = color
        self.price = price
        self.brand = brand
        self.category = category

    def get_vector(self):
        return [self.colors.red, self.colors.blue, self.colors.green, self.price, self.brand, self.category]

    def __str__(self):
        return ", ".join([str(i)for i in self.get_vector()])


class AnnTraining():
    def __init__(self, db):
        self.db = db
        self.blacklist_categories = [
            "Shirts",
            "Tees",
            "Polos",
            "T-shirts",
        ]

    def get_brands(self):
        brands = self.db['tops'].distinct('brand')
        return dict(zip(brands, xrange(0,len(brands))))

    def get_tops(self):
        return self.db['tops'].find()

    def get_category(self):
        categories = self.db['tops'].distinct('category')
        categories = [category for category in categories
                      if category not in self.blacklist_categories]
        return dict(zip(categories, xrange(0,len(categories))))

    def reduce_prices(self, prices):
        func = lambda p: float(p.split(' ')[0][1:]) if p else -1
        price = map(func, prices)
        if min(price) > 0:
            price = min(price)
        else:
            price = max(price)
        return price


db = connect_to_mongo("Tailor")
ann_training = AnnTraining(db)
tops = ann_training.get_tops()
total_brands = ann_training.get_brands()
total_categories = ann_training.get_category()

for top in tops[:]:
    # colors
    colors = top.get('colors') if top.get('colors') != "_not_available_" else None
    try:
        colors = [int(i) for i in colors[1:len(colors) - 1].split(",")]
        colors = Color(rgb=(colors[0] / 255.0, colors[1] / 255.0, colors[2] / 255.0))
    except Exception, e:
        print "[ERROR] %s has failed to produce a color. %s" % (top['_id'], e)
        colors = None

    # price
    full_price = top.get('full_price') if top.get('full_price') != "_not_available_" else None
    if isinstance(full_price, list):
        full_price = full_price[0]
    discounted_price = top.get('discounted_price') if top.get('discounted_price') != "_not_available_" else None
    if isinstance(discounted_price, list):
        discounted_price = discounted_price[0]
    prices = [full_price, discounted_price]
    try:
        price = ann_training.reduce_prices(prices)
    except Exception, e:
        price = None
        print '[ERROR] %s' % e

    # brand
    brand = top.get('brand', None)
    brand = total_brands[brand]

    # categories
    categories = top.get('category', None)
    category = None
    if isinstance(categories, list):
        for category in categories:
            if category in total_categories:
                category = total_categories[category]
                break
    else:
        if categories in total_categories:
            category = total_categories[categories]
    if category is None:
        print '[ERROR] Cant find category or category has been blacklisted'

    # validation
    if colors and price and brand is not None and category is not None:
        input_vector = InputVector(colors, price, brand, category)
    else:
        print "[ERROR] %s has failed to produce a input_vector. (%s, %f, %d, %s)" % (top['_id'], colors, price, brand, category)
        continue

    # save input vector
    try:
        db['tops'].update({"_id": top['_id']}, {"$set": {"input_vector": str(input_vector)}})
    except Exception, e:
        print '[ERROR] %s' % (e)
        continue

print '[INFO] Finished insert input_vectors'
