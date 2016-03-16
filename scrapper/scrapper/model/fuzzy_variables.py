class color(object):
    possible_ratings = {'Dislike':1, 'Ok':2, 'Like':3}
    upper_bound = 1
    lower_bound = 0
    
class complexity(object):
    possible_ratings = ('Not complex enough', 'Just right', 'Too complex')
    upper_bound = 1
    lower_bound = 0

class size(object):
    """
    Just consider chest size
    """
    possible_ratings = ('too small', 'small', 'just right', 'big', 'too big')
    upper_bound = 135
    lower_bound = 80

