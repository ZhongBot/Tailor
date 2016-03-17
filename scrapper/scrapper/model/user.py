import scrapper.model.fuzzy_variables as fuzzy
from scrapper.model.membership_base import *
from scrapper.model.type_of_functions import *

class user(object):
    default = '_not_available_'
    user_name = default
    
    '''
    -User has multiple membership functions.
    -Each membership function is built using a fuzzy variable that 
        specified the parameters of that fuzzy variable as well as
        a specific type of function.
        - membership func: model/membership_base.py
        - fuzzy var: model/fuzzy_variables
        - type of func: model/type_of_functions.py
    '''
    user_membership_funcs = {
        'color':default,
        'complexity':default,
        'size':default
    }

    prefer_color = default
    prefer_complexity = default
    prefer_size = default 
    
    purchases = {}
    
    def to_dict(self):
        _dict = {
            'user_name': self.user_name,
            'prefer_color': self.prefer_color,
            'prefer_complexity': self.prefer_complexity,
            'prefer_size': self.prefer_size,
            'user_membership_funcs': {}
        }
        for t, func in self.user_membership_funcs.items():
            if func != self.default:
                _dict['user_membership_funcs'][t] = {}
                if t == 'size':
                    func = [func]
                for f in func:
                    _dict['user_membership_funcs'][t][str(f.inference.value)] = f.to_dict()
                continue
            #Default to this..
            _dict['user_memebership_funcs'][t] = self.default
        return _dict
    
    def defaultMembership(self):
        '''
        -Create the default membership func for the user and attach it to the user
        -Default color/complexity/size membership functions should be a uniform function
        that will recommend everything. (ok is 1 across, big/small is 0 across)
        -As the users enter purchases, it should be reshaped
        '''
        rec_size = fuzzy.rec_size()
        
        #color fuzzy inference membership functions
        color_if_mf = membership_function(fuzzy.color(), 
                                          inference.if_func, 
                                          bell_function
                                         )
        color_then_mf = membership_function(fuzzy.rec_size(),
                                            inference.then_func,
                                            bell_function
                                           )
        
        self.user_membership_funcs['color'] = (color_if_mf, color_then_mf)

        #complexity fuzzy inference membership functions    
        complexity_if_mf = membership_function(fuzzy.complexity(),
                                               inference.if_func,
                                               bell_function
                                              )
        complexity_then_mf = membership_function(fuzzy.rec_size(),
                                                 inference.then_func,
                                                 bell_function
                                                )
        self.user_membership_funcs['complexity'] = (complexity_if_mf, complexity_then_mf)

        #size membership functions
        size_mf = membership_function(fuzzy.size(),
                                      inference.none,
                                      bell_function)
        self.user_membership_funcs['size'] = (size_mf)
