import numpy as np


class NeuralNetwork:

    def __init__(self, layer_sizes):
        """
        Neural Network initialization.
        Given layer_sizes as an input, you have to design a Fully Connected Neural Network architecture here.
        :param layer_sizes: A list containing neuron numbers in each layers. For example [3, 10, 2] means that there are
        3 neurons in the input layer, 10 neurons in the hidden layer, and 2 neurons in the output layer.
        """
        # This part is implemented based on this hypothesis that layer_sizes is always a list with three elements
        self.layer_sizes = layer_sizes # This field is used for generating children and parents weights and biases are divided according to these numbers
        self.weights1 = np.random.normal(size=(layer_sizes[0], layer_sizes[1]))
        self.biases1 = np.zeros((1, layer_sizes[1]))
        self.weights2 = np.random.normal(size=(layer_sizes[1], layer_sizes[2]))
        self.biases2 = np.zeros((1, layer_sizes[2]))


    # This function normalizes the input_list elements by passing them to activation function and returns the list of normal inputs
    def normalizer(self, input_list):
        output_list = []
        for i in input_list:
            output_list.append(self.activation(i))
        return output_list


    def activation(self, x):
        return 1 / (1 + np.exp(-x))


    def forward(self, x):
        """
        Receives input vector as a parameter and calculates the output vector based on weights and biases.
        :param x: Input vector which is a numpy array.
        :return: Output vector
        """
        # This part is implemented based on the hypothesis that the neural network has three layers
        second_layer_output = (x @ self.weights1) + self.biases1
        second_layer_normal_output = self.normalizer(second_layer_output)
        third_layer_output = (second_layer_normal_output @ self.weights2) + self.biases2
        third_layer_normal_output = self.normalizer(third_layer_output)
        return third_layer_normal_output





