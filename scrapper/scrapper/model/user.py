class user(object):
    default = '_not_available_'
    user_id = default
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
    
    def defaultMembership(self):
    '''
    Create the default membership func for the user and attach it to the user
    '''
    return NotImplemented

