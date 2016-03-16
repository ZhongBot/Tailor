class bell_function(object):

    eqn = '1/(1 + math.pow(abs(({x} - {c})/{a}), 2*{b}))'

    def __init__(self, pos, fuzzy_var, default_c=False, default_a=1, default_b=1):
        '''
        :param pos: the position of the center
        :param fuzzy_var: the fuzzy variable associated with the membership function
        :param default_c: default center of the function
        :param default_a: the confidence of the function. Smaller = more confident
        :param default_b: the rate of change from yes to no. Smaller = more gradual
        '''

        self.c = pos/len(fuzzy_var.possible_ratings) if not default_c else default_c
        self.a = default_a
        self.b = default_b
        self.upper_bound = fuzzy_var.upper_bound
        self.lower_bound = fuzzy_var.lower_bound
        
