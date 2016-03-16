class user_purchase(object):
    def __init__(self, user_id, product_id, default='_not_available_'):
        self.user_id = user_id
        self.product_id = product_id
        self.color_rating = default
        self.complexity_rating = default
        self.size_rating = default

    def populate_fuzzy_ratings(self, color_rating, complexity_rating, size_rating):
        self.color_rating = color_rating
        self.complexity_rating = complexity_rating
        self.size_rating = size_rating
       
    def to_dict(self):
        _dict = {
            'user_id': self.user_id,
            'product_id': self.product_id,
            'color_rating': self.color_rating,
            'complexity_rating': self.complexity_rating,
            'size_rating': self.size_rating
        }
        return _dict
        
