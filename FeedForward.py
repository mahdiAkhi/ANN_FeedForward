from numpy import dot, tanh, random


class Feedforward:

    def __init__(self):
        # generate same weight in every run
        random.seed(1)
        # 3x1 matrix weight
        self.weight_matrix = 2 * random.rand(4, 1) - 1

    # tanh as activation function
    def tanh(self, x):
        return tanh(x)

    # derivative of tanh function
    # needed to calculate the gradients
    def tanh_derivitave(self, x):
        return 1.0 - tanh(x) ** 2

    # foreard propagataion
    def forward_propagation(self, inputs):
        return self.tanh(dot(inputs, self.weight_matrix))

    def train(self, train_inputs, train_outputs, num_train_itterations):
        for i in range(num_train_itterations):
            output = self.forward_propagation(train_inputs)

            # calculate error in output
            error = train_outputs - output

            adjustment = dot(train_inputs.T , error *
                             self.tanh_derivitave(output))

            # adjust the weight matrix

            self.weight_matrix += adjustment
