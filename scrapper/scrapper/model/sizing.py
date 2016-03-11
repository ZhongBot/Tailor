class sizing(object):
    default = '_not_available_'
    
    type_of_clothing = default
    """
    {
        type_of_measurement: {
            'size':('lowerbound', 'upperbound')
        }
    } 
    ALL MEASURED IN CM
    Example: {"ARM":{"XS":(81,81)}}
    """
    measurements = {}

    def to_dict(self):
        _dict = {
            'type_of_clothing': self.type_of_clothing,
            'sizing': self.measurements
        }
        return _dict
    
