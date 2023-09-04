""" Logistic: programs that predicts the output value using the linear formula combined with the logistic activation function.
""" 
import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

coefficients = [c1, c2, c3]
sigmoid_outputs = []  # Create an empty list to store sigmoid outputs

def sigmoid(z):
    x2 = -1.0 * z
    a = math.exp(x2)
    nominator = 1
    denominator = 1 + a
    return nominator / denominator

for i, c in enumerate(coefficients):
    output = sigmoid(np.dot(x, c))
    sigmoid_outputs.append(output)  # Append the output to the list

# print(sigmoid_outputs)
# Print the sigmoid outputs

for i, output in enumerate(sigmoid_outputs):
    print(f"Output for c{i+1}:", output)