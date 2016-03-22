from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer
from pybrain.structure.modules   import LSTMLayer, SoftmaxLayer
from pybrain.datasets import SupervisedDataSet
import pickle
from preprocess import Preprocessor
from prepare_training_set import get_set_files


def load_training_set():
    fileObj = open('training_set.pkl', 'r')
    training_set = pickle.load(fileObj)
    fileObj.close()
    return training_set


def generate_and_test_nn():
    d = load_training_set()
    n = buildNetwork(d.indim, 13, d.outdim, hiddenclass=LSTMLayer, outclass=SoftmaxLayer, outputbias=False, recurrent=True)
    t = BackpropTrainer(n, learningrate=0.01, momentum=0.99, verbose=True)
    t.trainOnDataset(d, 1000)
    t.testOnData(verbose=True)
    return (n, d)


def save_nn(nn):
    filename = "nn.pkl"
    fileObj = open(filename, 'wb')
    pickle.dump(nn, fileObj)
    fileObj.close()


if __name__ == '__main__':
    nn = generate_and_test_nn()
    print "[INFO] input:{} output:{}".format(nn[1].indim, nn[1].outdim)
    save_nn(nn)
