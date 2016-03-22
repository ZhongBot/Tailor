import numpy as np

class Kohonen(object):
    def __init__(self, vector_size=3, num_cluster=2, learning_rate=0.3, max_epoch = 5, input_vectors=[]):
        self.vector_size = vector_size
        self.num_cluster = num_cluster
        self.learning_rate = learning_rate
        # initialize random weights from [0, 1)
        self.weight = np.random.rand(vector_size, num_cluster)
        self.max_epoch = max_epoch
        self.input_vectors = input_vectors

    def geometric_decay(self):
        # geometric decay of learning rate
        self.learning_rate *= 0.2

    # returns the node that is closest to the vector
    def apply_input_vector(self, vector):
        I = [None] * self.num_cluster
        closest = float("inf")
        closest_index = -1
        vector = np.array(vector)

        for col in range(0, self.num_cluster):
            I[col] = self.weight[:,col] - vector
            I[col] = np.square(I[col])
            closeness = np.sum(I[col])
            # calculate which weight column the input vector is the closest to
            if closeness < closest:
                closest = closeness
                closest_index = col

        return vector, closest_index

    def update_weight(self, vector, col):
        # update weights of the column that was calculated to be the closest to input
        self.weight[:,col] += self.learning_rate * (vector - self.weight[:,col])

    def train(self):
        for i in range(0, self.max_epoch):
            for input_vector in self.input_vectors:
                closest_vector, col = self.apply_input_vector(input_vector)
                self.update_weight(closest_vector, col)
            # decay learning rate every complete epoch
            self.geometric_decay()
