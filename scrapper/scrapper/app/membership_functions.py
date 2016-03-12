import math

class bell_function(object):
    def __init__(self, name, pos, fuzzy_var):
        self.name = name
        self.c = pos/total
        self.upper_bound = fuzzy_var.upper_bound
        self.lower_bound = fuzzy_var.lower_bound

        #self.equation = 1/(1 + math.pow(abs((x - c)/a), 2*b))
