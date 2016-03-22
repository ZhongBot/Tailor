import pickle
from preprocess import Preprocessor
from prepare_training_set import get_set_files
from model import PatternType


def load_nn():
    fileObj = open('nn.pkl', 'r')
    nn = pickle.load(fileObj)
    fileObj.close()
    return nn

if __name__ == '__main__' :
    preprocessor = Preprocessor()
    nn = load_nn()

    test_set_files = get_set_files("test_set")
    training_set_files = get_set_files("training_set")

    for pattern_type, files in test_set_files.iteritems():
        print "[INFO]: Processing {}".format(PatternType(pattern_type).name)
        for file in files:
            entry = preprocessor.preprocess(pattern_type, file)
            sums = list(entry.sums.x)
            sums.extend(entry.sums.y)
            result_nn = nn[0].activate(sums)
            max_result = max(result_nn)
            result = [1 if i == max_result else 0 for i in result_nn]
            print [file, result]

# check     [0, 0, 0, 1] 3
# solid     [0, 0, 1, 0] 2
# dot       [0, 1, 0, 0] 1
# stripe    [1, 0, 0, 0] 0
