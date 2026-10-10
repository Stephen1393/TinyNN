import numpy as np

i = np.array([1,2,3,4])
w1 = np.array([0.2,0.8,-0.6,0.1])
w2 = np.array([0.3,0.9,-0.7,0.2])
w3 = np.array([0.4,1.0,-0.8,0.3])

weights = np.array([w1,w2,w3])

bias = np.array([1,-3,4])

z = weights @ i + bias

R_output = np.maximum(z, 0)

#second layer

i_2 = np.array(R_output)

w2_1 = np.array([4, -0.3, 0.7])
w2_2 = np.array([2, -0.1, 0.9])

bias2 = np.array([3,-2.2])

weights2 = np.array([w2_1, w2_2])

m = weights2 @ i_2 + bias2

print(weights.shape)
print(weights2.shape)
print(R_output.shape)
print(m.shape)
