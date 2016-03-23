from scrapper.config.db_config import connect_to_mongo, disconnect_from_mongo

import colorific
import urllib
import os
import math


# Object storing an img_url and an "RGB" score
class ItemColor(object):
    default = '_not_available_'
    rgb_colors = default

    def __init__(self, id, img_url):
        """
        :param id: string representation of image id (i.e. _id from mongoDB)
        :param img_url: string url for image
        :return:
        """
        self.id = id
        self.img_url = img_url

    def detect_colors(self):
        """
        Creates a temp directory, downloads the img_url (if it exists), extracts colors and generates
        RGB aggregating all colors
        :param dirName: directory name store temporary images for processing
        :return:
        """
        dirname = 'temp'
        if not os.path.exists(dirname):
            os.mkdir(dirname)

        filepath = dirname + '\\' + self.id + '.jpg'
        urllib.urlretrieve(self.img_url, filepath)

        palette = colorific.extract_colors(filepath)
        self.rgb_colors = colors_to_score_string(palette.colors)


def colors_to_score_string(colors):
    """
    Utility function to convert an iterable of Colors to an "RGB score".
    Sum prominence values for each colours to calculate a scaler to normalize prominence to 1.0
    Scores are calculated as tuple
    (sum(R values * prominence * scaler), sum(G values * prominence * scaler), sum(B values * prominence * scaler))
    :param colors:
    :return: string representation of the "RGB score" tuple
    """
    prominence_sum = 0.0
    for color in colors:
        prominence_sum += getattr(color, 'prominence')

    scaler = 1.0 / prominence_sum
    #print "Scaler: %s" % scaler

    r_score = 0.0
    g_score = 0.0
    b_score = 0.0
    for color in colors:
        color_tuple = getattr(color, 'value')
        prominence = getattr(color, 'prominence')
        r_score += (color_tuple[0] * prominence * scaler)
        g_score += (color_tuple[1] * prominence * scaler)
        b_score += (color_tuple[2] * prominence * scaler)

    color_score = (math.trunc(r_score), math.trunc(g_score), math.trunc(b_score))

    return str(color_score)


def main():
    try:
        db = connect_to_mongo()
        name = 'admin'
        collection = 'tops'

        tops = db[collection]
        print "Number of items to process: %s" % tops.count()
        for d in tops.find()[:]:
            top_id = d['_id']
            img_url = str(d['img_url'])
            # image names may be missing http:// in front
            if not img_url.startswith("http://"):
                img_url = "http://" + img_url

            item_color = ItemColor(str(top_id), img_url)
            item_color.detect_colors()
            print "Processing id %s with Color %s" %(top_id, item_color.rgb_colors)

            # update field for id with color
            tops.update({"_id": top_id}, {"$set": {"colors": item_color.rgb_colors}})

        print "Count of items with no colors: %s" % tops.find({"colors": "_not_available_"}).count()
        print "Processing complete"

    finally:
        disconnect_from_mongo(db)


def reset():
    try:
        db = connect_to_mongo()
        collection = 'tops'

        tops = db[collection]
        for d in tops.find()[:]:
            top_id = d['_id']
            tops.update({"_id": top_id}, {"$set": {"colors": "_not_available_"}})

    finally:
        disconnect_from_mongo(db)


def test_main():
     # testing
    urls = ['http://pics.ae.com/is/image/aeo/0153_9196_321_of',
            'http://pics.ae.com/is/image/aeo/0153_9196_321_of?fit=crop&wid=450&hei=504&qlt=50,0',
            'http://pics.ae.com/is/image/aeo/1152_9065_400_of?fit=crop&wid=450&hei=504&qlt=50,0']
    for url in urls:
        item = ItemColor(url)
        item.detect_colors()
        print item.rgb_colors

if __name__ == "__main__":
    main()
