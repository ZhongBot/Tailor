from collections import OrderedDict

class color(object):
    '''
    If the user like the color then user satisfiability increases.
    Otherwise, decrease.
    
    Update the color curve based on the purchase taking into consideration of momentum.
    
    To sample if the user like the color, take the membership value of the 'Ok' func
    and then minus the membershp value of the 'Dislike' and the 'Like' func. This will produce a value
    between the the upper and lower bound for the satisfiability x-axis. 
    '''
    possible_ratings = {'Dislike':0, 'Ok':1, 'Like':2}
    possible_ratings = OrderedDict(sorted(possible_ratings.items(), key=lambda t:t[1]))
    upper_bound = 10
    lower_bound = 0
    name = 'color'
    
    def to_dict(self):
        _dict = {
            'possible_ratings': self.possible_ratings,
            'upper_bound': 1,
            'lower_bound': 0,
            'name': self.name
        }
        return _dict

class complexity(object):
    '''
    If the user like the complexity then user satisfiability increases.
    Otherwise, decrease.

    Update the complexity curve based on the purchase taking into consideration of momentum.

    To sample if the user like the complexity, take the membership value of the 'Ok' func
    and then minus the membershp value of the 'Dislike' and the 'Like' func. This will produce a value
    between the the upper and lower bound for the satisfiability x-axis.
    '''
    possible_ratings = {'Not complex enough':0, 'Just right':1, 'Too complex':2}
    possible_ratings = OrderedDict(sorted(possible_ratings.items(), key=lambda t:t[1]))
    upper_bound = 10
    lower_bound = 0
    name = 'complexity'
    
    def to_dict(self):
        _dict = {
            'possible_ratings': self.possible_ratings,
            'upper_bound': 1,
            'lower_bound': 0,
            'name': self.name
        }
        return _dict

class size(object):
    """
    Just consider chest size
    """
    possible_ratings = {'too small':0, 'small':1, 'just right':2, 'big':3, 'too big':4}
    possible_ratings = OrderedDict(sorted(possible_ratings.items(), key=lambda t:t[1]))
    upper_bound = 51
    lower_bound = 32
    name = 'size'
    
    def to_dict(self):
        _dict = {
            'possible_ratings': self.possible_ratings,
            'upper_bound': 51,
            'lower_bound': 32,
            'name': self.name
        }
        return _dict

class satisfaction(object):
    """
    usually used in the then func
    """
    possible_ratings = {'less':0, 'same':1, 'more':2}
    possible_ratings = OrderedDict(sorted(possible_ratings.items(), key=lambda t:t[1]))
    upper_bound = 1
    lower_bound = 0
    name = 'satisfaction'

    def to_dict(self):
        _dict = {
            'possible_ratings': self.possible_ratings,
            'upper_bound': 1,
            'lower_bound': 0,
            'name': self.name
        }
        return _dict

