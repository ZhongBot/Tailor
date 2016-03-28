from scrapper.config.db_config import connect_to_mongo
from bson.objectid import ObjectId


def fuzzy_variable_updater(db, user, fuzzy_var, inf, new_entry):
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

    user_id = ""
    try:
        cur_inf = user[0]["user_membership_funcs"][fuzzy_var][inf]
        user_id = user[0][u'_id']
    except:
        return 'Could not find the appropriate current membership function', False

    new_mf = new_entry.membership_funcs[0].membership
    cur_mf = []

    for k in cur_inf.keys():
        # ignore fuzzy var, only interested in rel_pos entries
        if 'membership' in cur_inf[k].keys():
            cur_mf = cur_inf[k]['membership']

        # check if two mf are the same length
        if len(cur_mf) != len(new_mf):
            continue
    
        #updating mf. The more confidence we are about the membership value, the less we want
        #to adjust based on one input.
        for i in range(len(cur_mf)):
            direction = new_mf[i] - cur_mf[i]
            confidence = min(1 - new_mf[i], new_mf[i])
            cur_mf[i] += direction * confidence

        # update entry in mongo
        update_field = "user_membership_funcs." + str(fuzzy_var) + "." + str(inf) + "." + str(k) + ".membership"
        db['user'].update({"_id": user_id},{"$set": {update_field: cur_mf}})

    
    return 'updated!', True

if __name__ == '__main__':
    db = connect_to_mongo()
    user = db['user'].find({"_id": ObjectId("56f1ae649db17b22bc0d86e7")})
    #fuzzy_varaible_updater(db, user, fuzzy_var, inf, origin_mf, new_entry)
