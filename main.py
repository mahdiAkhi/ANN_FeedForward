from numpy import array
from FeedForward import Feedforward

# Create a Neural Neatwork Instance
neural_network = Feedforward()

# Pront Random Weight matrix
print("Random Weight at the Starft of Training :")
print(neural_network.weight_matrix)

# Train Input Matrix
train_inputs = array([[1, 0, 1, 0],
                      [0, 0, 1, 0],
                      [1, 0, 0, 0],
                      [1, 1, 0, 1]])

# Train Output Matrix
train_output = array([[1, 0, 0, 1]]).T

# Training Network By 10000 Epoch's
neural_network.train(train_inputs, train_output, 10000)

# Print Weight Matrix After Training Data
print("New Weight After Training :")
print(neural_network.weight_matrix)

# Test The Nural Network with New Sitaution
print("Tetsing Neural Network ------")
print(neural_network.forward_propagation(array([1,0,0,1])))