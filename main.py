import numpy as np


i = np.array([1,2,3,4])
w1 = np.array([0.2,0.8,-0.6,0.1])
w2 = np.array([0.3,0.9,-0.7,0.2])
w3 = np.array([0.4,1.0,-0.8,0.3])

weights = np.array([w1,w2,w3])

bias = np.array([1,-3,4])

z = weights @ i + bias

Reli_output = np.maximum(z, 0)

print(Reli_output)
print(Reli_output.shape)

