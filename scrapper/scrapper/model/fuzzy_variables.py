class color(object):
    possible_ratings = {'Dislike':0, 'Ok':1, 'Like':2}
    upper_bound = 1
    lower_bound = 0
    
class complexity(object):
    possible_ratings = {'Not complex enough':0, 'Just right':1, 'Too complex':2}
    upper_bound = 1
    lower_bound = 0

class size(object):
    """
    Just consider chest size
    """
    possible_ratings = {'too small':0, 'small':1, 'just right':2, 'big':3, 'too big':4}
    upper_bound = 135
    lower_bound = 80

