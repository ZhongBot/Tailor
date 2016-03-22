import os
import cv2
from preprocess import Preprocessor
from matplotlib import pyplot as plt
from model import Entry, PatternType
from remove_outlier import percentile_based_outlier
from pybrain.datasets import SupervisedDataSet
import pickle


def get_directory_structure(startpath):
    directory = {}
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        directory[os.path.basename(root)] = []
        for f in files:
            directory[os.path.basename(root)].append(f)

    return directory


def get_set_files(directory_name):
    training_set_directory = get_directory_structure(
        os.path.dirname(os.path.realpath(__file__)) + "/" + directory_name + "/")

    training_set_files = {
        PatternType.Stripe: [],
        PatternType.Dot: [],
        PatternType.Solid: [],
        PatternType.Check: [],
    }

    for filename in training_set_directory['stripe']:
        training_set_files[PatternType.Stripe].append(
            os.path.dirname(os.path.realpath(__file__)) +
            "/" + directory_name + "/stripe/" + filename)
    for filename in training_set_directory['dot']:
        training_set_files[PatternType.Dot].append(
            os.path.dirname(os.path.realpath(__file__)) +
            "/" + directory_name + "/dot/" + filename)
    for filename in training_set_directory['solid']:
        training_set_files[PatternType.Solid].append(
            os.path.dirname(os.path.realpath(__file__)) +
            "/" + directory_name + "/solid/" + filename)
    for filename in training_set_directory['check']:
        training_set_files[PatternType.Check].append(
            os.path.dirname(os.path.realpath(__file__)) +
            "/" + directory_name + "/check/" + filename)

    return training_set_files


def prepare_training_set(training_set_files):
    preprocessor = Preprocessor()
    ds = SupervisedDataSet(500 * 2, 4)
    for pattern_type, files in training_set_files.iteritems():
        print "[INFO]: Processing {}".format(PatternType(pattern_type).name)
        for file in files:
            entry = preprocessor.preprocess(pattern_type, file)
            sums = list(entry.sums.x)
            sums.extend(entry.sums.y)
            pattern_type_output = [0, 0, 0, 0]
            pattern_type_output[pattern_type.value - 1] = 1
            # pattern_type_output = [pattern_type.value - 1]
            ds.addSample(tuple(sums), tuple(pattern_type_output))
            print [file, pattern_type_output]

    return ds


def save_training_set(training_set):
    filename = "training_set.pkl"
    fileObj = open(filename, 'wb')
    pickle.dump(training_set, fileObj)
    fileObj.close()


if __name__ == '__main__':
    training_set_files = get_set_files("training_set")
    training_set = prepare_training_set(training_set_files)
    save_training_set(training_set)
