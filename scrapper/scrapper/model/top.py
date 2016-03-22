class topItem(object):
    default = '_not_available_'
    
    #String fields
    name = default
    brand = default
    product_url = default
    img_url = default
    
    full_price = default
    discounted_price = default
    
    complexity = default
    #color_ame is provided to us by the website 
    color_name = default

    #List field
    #colors is populated by img rec
    # note this is a single RGB score tuple!
    colors = default
    category = default    

    def to_dict(self):
        _dict = {
            'name': self.name,
            'color': self.color_name,
            'brand': self.brand,
            'product_url': self.product_url,
            'img_url': self.img_url,
            'full_price': self.full_price,
            'discounted_price': self.discounted_price,
            'complexity': self.complexity,
            'color_name': self.color_name,
            'colors': self.colors,
            'category': self.category
        }
        return _dict

