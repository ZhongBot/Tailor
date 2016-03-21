import numpy as np

class Kohonen(object):
    def __init__(self, vector_size=3, num_cluster=2, learning_rate=0.3, max_epoch = 5, input_vectors=[]):
        self.vector_size = vector_size
        self.num_cluster = num_cluster
        self.learning_rate = learning_rate
        self.weight = np.random.rand(vector_size, num_cluster)
        self.max_epoch = max_epoch
        self.input_vectors = input_vectors

        print("initial learning rate: " + str(self.learning_rate))
        print("initial weight: " + str(self.weight))


    def geometric_decay(self):
        self.learning_rate *= 0.2
        print("updated learning rate:" + str(self.learning_rate))

    # returns the node that is closest to the vector
    def apply_input_vector(self, vector):
        I = [None] * self.num_cluster
        closest = float("inf")
        closest_index = -1
        vector = np.array(vector)

        for col in range(0, self.num_cluster):
            print("col: " + str(col))
            print("weight col: " + str(self.weight[:,col]))
            print("vector: " + str(vector))
            I[col] = self.weight[:,col] - vector
            I[col] = np.square(I[col])
            closeness = np.sum(I[col])
            print("closeness: " + str(closeness))
            if closeness < closest:
                closest = closeness
                closest_index = col

        return vector, closest_index

    def update_weight(self, vector, col):
        print("updated weight col: " + str(col))
        self.weight[:,col] += self.learning_rate * (vector - self.weight[:,col])
        print("updated weight: " + str(self.weight))

    def train(self):
        for i in range(0, self.max_epoch):
            for input_vector in self.input_vectors:
                closest_vector, col = self.apply_input_vector(input_vector)
                self.update_weight(closest_vector, col)
            self.geometric_decay()