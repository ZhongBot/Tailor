from enum import Enum

class inference(Enum):
    none = 0
    if_func = 1
    then_func = 2


class membership_function(object):
    def __init__(self, fuzzy_var, inf, func_type):
        """
        :param fuzzy_var: Tells us which one of the fuzzy variables are we dealing with 
        :param inf: There are two membership functions in the fuzzy inference. If and then.
        :param func_type: Which type of mathematical function do you want to use to represent
                          this membership function

        * Each if/then membership function is a collection of individual membership functions
        * Example: if (size). Size is a collection of membership functions consisting of 
                   <too small, small, just right, big, too big>.   
        """
        self.fuzzy_variable = fuzzy_var
        self.inference = inf
        self.membership_funcs = (func_type(n, p, fuzzy_var) for n, p in fuzzy_var.possible_ratings.items())
     

    def to_dict(self):
        _dict = {
            'inference': self.inference.value,
           'fuzzy_var':self.fuzzy_variable.to_dict()
        }
        for func in self.membership_funcs:
            _dict.update({func.pos: func.to_dict()})
        return _dict
        
