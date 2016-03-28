from scrapper.config.db_config import connect_to_mongo
from bson.objectid import ObjectId
import scrapper.model.fuzzy_variables as fuzzy
from scrapper.model.membership_base import *
from scrapper.model.type_of_functions import *
from scrapper.model.sizing import *
import scrapper.app.fuzzy_updater as updater


def fuzzy_logic(db, user, product_id_list):
    fuzzy_list = [fuzzy.color(), fuzzy.complexity(), fuzzy.size()]
    inference_list = ['inf_1', 'inf_1', 'inf_0']

    for product in product_id_list:
        for index, fuzzy_var in enumerate(fuzzy_list):
            # create new fuzzy membership
            # TODO: create mf at center specific to product
            mf = membership_function(fuzzy_var,
                    inference_list[index],
                    bell_function
                )

            # call fuzzy updater with new fuzzy membership
            print(updater.fuzzy_variable_updater(db, user, fuzzy_var.name, inference_list[index], mf))


def neural_network():
    return


def worker(db, user, product_id_list, size_list, complexity_list, color_list):
    """
    worker called when receive purchase from user/server
    input: user, list of products ids, size, complexity, and color ratings
    1 - call fuzzy updater for each
    2 - defuzzify membership fns
    3 - retrieve list of input vectors
    4 - feed input vectors
    """
    fuzzy_logic(db, user, product_id_list)


if __name__ == '__main__':
    db = connect_to_mongo()
    user = db['user'].find({"_id": ObjectId("56f1ae649db17b22bc0d86e7")})
    product_id_list = [ObjectId("56f1ae5e9db17b26fc9f8aed"), ObjectId("56f1ae5f9db17b26fc9f8aee")]
    size_list = [0.3, 0.7]
    complexity_list = [0.1, 0.2]
    color_list = [0.9, 0.4]

    worker(db, user, product_id_list, size_list, complexity_list, color_list)

