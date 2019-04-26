import numpy as np
import math

# The Transfer Function is the typical sigmoid 
def sigmoid(x):
  return 1 / (1 + math.exp(-x))


# The only relevant aspects of input and output vectors for NN Architecture are the shapes as they define the number of weights 
x = np.random.rand(1,4)
y = np.random.rand(1,1)


class NN: 
  def __init__(self, N, tf, x, y): 
    # Number of Neurons 
    self.N = N 
    
    # Transfer Function 
    self.tf = np.vectorize(tf)
    
    # Weights 
    self.weights_in = np.random.rand(x.shape[1], self.N)
    self.weights_out = np.random.rand(self.N, y.shape[0])
    
  def forward(self, x): 
    self.layer1 = self.tf(np.dot(x, self.weights_in))
    return self.tf( np.dot(self.layer1, self.weights_out) )
    
  def to_str(self): 
    return "Input Weights \n" + np.array2string(self.weights_in) + "\n Output Weights \n" + np.array2string(self.weights_out)


# Test 

temp = NN(5, sigmoid, x, y)
temp.forward(x)




