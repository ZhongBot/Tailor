class bell_function(object):

    eqn = '1/(1 + math.pow(abs(({x} - {c})/{a}), 2*{b}))'

    def __init__(self, name, pos, fuzzy_var, default_c=False, default_a=1, default_b=1):
        '''
        :param name: indicate which characteristic the function is model after (small/large)
        :param pos: the position of the center
        :param fuzzy_var: the fuzzy variable associated with the membership function
        :param default_c: default center of the function
        :param default_a: the confidence of the function. Smaller = more confident
        :param default_b: the rate of change from yes to no. Smaller = more gradual
        '''
        self.name = name
        self.pos = pos
        self.length = len(fuzzy_var.possible_ratings)
        self.a = default_a
        self.b = default_b
        self.c = pos/(self.length-1) if not default_c else default_c
        self.upper_bound = fuzzy_var.upper_bound
        self.lower_bound = fuzzy_var.lower_bound
        self.c = self.c * self.upper_bound 
    
    def to_dict(self):
        _dict = {
            'name': self.name,
            'pos': self.pos,
            'length': self.length,
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'upper_bound': self.upper_bound,
            'lower_bound':self.lower_bound,
            'eqn': self.eqn,
            'type': 'bell function'
        }
        return _dict

