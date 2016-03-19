
def fuzzy_variable_updater(user, fuzzy_var, inf, origin_mf, new_entry):
    '''
    Given a user and the the membership func to update. Update the membership func 
    with respect to momentum.

    :param user: The user to update
    :param fuzzy_var: The fuzzy variable membership func to update
    :param inf: Specify whether we are updating the if or the then func
    :param origin_mf: The current membership func
    :param new_entry: The new data point (in membership func form)
    '''
    
    #user.user_membership_funcs['color'][0].membership_funcs[0].name
    try:
        cur_mf = user.user_membership_funcs[fuzzy_var.name][inf].membership_funcs[new_entry.name]
    except:
        return 'Could not find the apporpriate current membership function', False
    
    old_mf = cur_mf.membership
    new_mf = new_entry.membership
    if len(old_mf) != len(new_mf):
        return 'len(old_mf) != len(new_mf)', False
    
    #updating mf. The more confidence we are about the membership value, the less we want
    #to adjust based on one input.    
    for i in range(old_mf):
        direction = new_mf[i] - old_mf[i]
        confidence = min(1 - new_mf[i], new_mf[i])
        old_mf[i] += direction * confidence
    return 'updated!', True
