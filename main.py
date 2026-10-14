import numpy as np

class Dense():
    def __init__(self, n_inputs, n_neurons):
        self.n_inputs = n_inputs
        self.n_neurons = n_neurons
        self.weights = np.random.randn(n_neurons, n_inputs)
        self.biases = np.zeros(n_neurons)

    def forward(self, inputs):
        self.output = self.weights @ inputs + self.biases

class ReLU():
    def forward(self, inputs):
        self.output = np.maximum(inputs, 0)


layer1 = Dense(3, 4)
layer2 = Dense(4, 2)

layer1.forward(np.array([1,2,3]))

activated1 = ReLU()

activated1.forward(layer1.output)

layer2.forward(activated1.output)

activated2 = ReLU()

activated2.forward(layer2.output)

print(activated1.output)
print(activated2.output)
