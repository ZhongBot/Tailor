from collections import OrderedDict

class color(object):
    possible_ratings = {'Dislike':0, 'Ok':1, 'Like':2}
    possible_ratings = OrderedDict(sorted(possible_ratings.items(), key=lambda t:t[1]))
    upper_bound = 1
    lower_bound = 0
    
    def to_dict(self):
        _dict = {
            'possible_ratings': self.possible_ratings,
            'upper_bound': 1,
            'lower_bound': 0
        }
        return _dict

class complexity(object):
    possible_ratings = {'Not complex enough':0, 'Just right':1, 'Too complex':2}
    possible_ratings = OrderedDict(sorted(possible_ratings.items(), key=lambda t:t[1]))
    upper_bound = 1
    lower_bound = 0
    
    def to_dict(self):
        _dict = {
            'possible_ratings': self.possible_ratings,
            'upper_bound': 1,
            'lower_bound': 0
        }
        return _dict

class size(object):
    """
    Just consider chest size
    """
    possible_ratings = {'too small':0, 'small':1, 'just right':2, 'big':3, 'too big':4}
    possible_ratings = OrderedDict(sorted(possible_ratings.items(), key=lambda t:t[1]))
    upper_bound = 135
    lower_bound = 80

    def to_dict(self):
        _dict = {
            'possible_ratings': self.possible_ratings,
            'upper_bound': 135,
            'lower_bound': 80
        }
        return _dict

class rec_size(object):
    """
    usually used in the then func
    """
    possible_ratings = {'less':0, 'same':1, 'more':2}
    possible_ratings = OrderedDict(sorted(possible_ratings.items(), key=lambda t:t[1]))
    upper_bound = 1
    lower_bound = 0

    def to_dict(self):
        _dict = {
            'possible_ratings': self.possible_ratings,
            'upper_bound': 1,
            'lower_bound': 0
        }
        return _dict

