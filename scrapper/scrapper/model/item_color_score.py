import colorific
import urllib
import tempfile
import os

# Object storing an img_url and an "RGB" score
class ItemColorScore(object):
    default = '_not_available_'

    img_url = default
    color_score = default

    def __init__(self, img_url):
        self.img_url = img_url

    def detect_colors(self):
        '''
        Creates a temp directory, downloads the img_url (if it exists), extracts colors and generates "RGB score"
        :return:
        '''
        try:
            # Need to download file from URL. Ugly, but this works for now
            tmp_dir = tempfile.mkdtemp()
            filename = tmp_dir + '\\local-img.jpg'
            urllib.urlretrieve(self.img_url, filename)

            pallette = colorific.extract_colors(filename_or_img=filename)

            self.color_score = colors_to_score_string(pallette.colors)
            #print pallette # Debugging only

        except Exception, e:
            print "Error - %s" % e

        finally:
            # clean up
            os.remove(filename)
            os.removedirs(tmp_dir)

def colors_to_score_string(colors):
    '''
    Utility function to convert an iterable of Colors to an "RGB score".
    Sum prominence values for each colours to calculate a scaler to normalize prominence to 1.0
    Scores are calculated as tuple
    (sum(R values * prominence * scaler), sum(G values * prominence * scaler), sum(B values * prominence * scaler))
    :param colors:
    :return: string representation of the "RGB score" tuple
    '''
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

    color_score = (r_score, g_score, b_score)

    return str(color_score)

def test_main():
     # testing
    urls = ['http://pics.ae.com/is/image/aeo/0153_9196_321_of',
            'http://pics.ae.com/is/image/aeo/0153_9196_321_of?fit=crop&wid=450&hei=504&qlt=50,0',
            'http://pics.ae.com/is/image/aeo/1152_9065_400_of?fit=crop&wid=450&hei=504&qlt=50,0']
    for url in urls:
        item = ItemColorScore(url)
        item.detect_colors()
        print item.color_score

if __name__ == "__main__":
    test_main()