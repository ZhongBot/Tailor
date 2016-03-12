class user_purchase(object):
    def __init__(self, user_id, product_id, color_rating, complexity_rating, size_rating):
        self.user_id = user_id
        self.product_id = product_id
        self.color_rating = color_rating
        self.complexity_rating = complexity_rating
        self.size_rating = size_rating
        
    def retrieve_fuzzy_variables(self):
        
