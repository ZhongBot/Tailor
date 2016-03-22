from kohonen import Kohonen

def offline_training():
    '''
    Retreives the current catalog of products from db.
    Train and create a NN.
    Output a NN model.
    '''

    # input vector with three attributes (brand, complexity, color)
    input_vectors = [[0.25, 0.88, 0.23], [1.00, 0.19, 0.98], [0.75, 0.20, 0.53], [0.50, 0.48, 0.92]]
    max_epoch = 5
    vector_size = 3
    learning_rate = 0.3
    num_cluster = 2

    k = Kohonen(vector_size, num_cluster, learning_rate, max_epoch, input_vectors)
    k.train()


if __name__ == '__main__':
    offline_training()

