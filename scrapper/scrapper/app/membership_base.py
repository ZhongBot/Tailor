class inference(enum):
    if_func = 1
    then_func = 2

class fuzzy_variable(enum):
    """
    These fuzzy variables are used to determine how many recommendations are shown to the user
    """
    color = 1
    complexity = 2
    size = 3

class func_type(enum):
    bell_membership_func = 1

class membership_function(object):
    def __init__(self, fuzzy_var, inf, func_type)
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
        
        if func_type == 1:
            self.membership_funcs = (bell_function(s, i, fuzzy_var) for i, s in enumerate(fuzzy_var.possible_ratings))
     

        
