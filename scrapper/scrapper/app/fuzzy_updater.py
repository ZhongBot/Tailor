
def fuzzy_variable_updater(db, user, fuzzy_var, inf, origin_mf, new_entry):
    '''
    Given a user and the the membership func to update. Update the membership func 
    with respect to momentum.

    :param db: The database to write to
    :param user: The user to update
    :param fuzzy_var: The fuzzy variable membership func to update
    :param inf: Specify whether we are updating the if or the then func
    :param origin_mf: The current membership func
    :param new_entry: The new data point (in membership func form)
    '''
    
    #user.user_membership_funcs['color'][0].membership_funcs[0].name
    try:
        cur_mf = user.user_membership_funcs[fuzzy_var.name][inf].membership_funcs[new_entry.name].membership
    except:
        return 'Could not find the apporpriate current membership function', False
    
    new_mf = new_entry.membership
    if len(cur_mf) != len(new_mf):
        return 'len(cur_mf) != len(new_mf)', False
    
    #updating mf. The more confidence we are about the membership value, the less we want
    #to adjust based on one input.    
    for i in range(cur_mf):
        direction = new_mf[i] - cur_mf[i]
        confidence = min(1 - new_mf[i], new_mf[i])
        cur_mf[i] += direction * confidence

    '''
    TODO: Update the user mongo document and set the correct membership function to cur_mf
    '''
    
    #return 'updated!', True

if __name__ == '__main__':
     
    fuzzy_varaible_updater(db, user, fuzzy_var, inf, origin_mf, new_entry)
