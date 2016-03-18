from scrapper.config.db_config import connect_to_mongo

def worker(db_conn, user, purchase):
    '''
    Receives a purchase request from a producer.
    First validate the purchase.
    Second retrieve the fuzzy variable's value.
    Third feed the product vector into NN.
    Fourth return recommendations.
    
    :param db_conn: The db connection
    :param user: The user that has made a purchase
    :param purchase: The item that has been purchased
    :return recommendation: A vector containing similar items
    '''

    #First validate the purchase
    

    #Second retrieve the fuzzy variable's values

    #Third feed the product vector into NN

    #Fourth return recommendations
    
if __name__ == '__main__':
    db = connect_to_mongo()
    worker(db, user, purchase)

