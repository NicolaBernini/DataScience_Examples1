
import numpy as np 

"""
  Kalman Filter in plain Python + Numpy 
  Filter State 
  - x = Updated State 
  - P = Updated State Uncertainty
  - x_pred = Predicted State 
  - P_pred = Predicted State Uncertainty

  Models 
  - F = Prediction Model 
  - H = Observation Model (Maps from State Space to Observation Space)
  - B = Evolved Forcing Term 
  - Q = Evolution Noise 
  - R = Observation Noise 
"""
class KF: 
  def __init__(self, x, P, F, B, H, Q, R): 
    # Init 
    self.x = x
    self.x_pred = x 

    # Initial State Uncertainty 
    self.P = P 
    self.P_pred = P 

    # Prediction Model 
    self.F = F 

    # Observation Model 
    self.H = H 

    # Process Noise 
    self.Q = Q 

    # Observation Noise 
    self.R = R 

  def predict(self, u): 
    self.x_pred = F.dot(x) + B.dot(u)
    self.P_pred = F.dot(P.dot(np.transpose(F))) + Q
      
  def __innovation(self, y): 
    return y - self.H.dot(self.x_pred)

  def __S(self): 
    return self.R + self.H.dot(self.P_pred.dot(np.transpose(self.H))) 

  def __K(self): 
    return self.P_pred.dot(np.transpose(self.H).dot(np.linalg.inv(self.__S())))

  def __I(self, A): 
    if(A.shape[0] != A.shape[1]): 
      raise ValueError("[Identity] Not Square")
    return np.identity(A.shape[0])

  
  def update(self, y): 
    self.x = self.x_pred + self.__K().dot(self.__innovation(y))
    temp = self.__K().dot(self.H)
    self.P = (self.__I(temp) - temp).dot(self.P_pred.dot(np.transpose(self.__I(temp) - temp))) + self.__K().dot(self.R.dot(np.transpose(self.__K()))) 

  def to_str(self): 
    return "x \n" + np.array2string(self.x) + "\n P \n" + np.array2string(self.P) + "\n x_pred \n" + np.array2string(self.x_pred) + "\n P_pred \n" + np.array2string(self.P_pred)

F = np.array([[1,0], [0,1]])
P = np.array([[1,0], [0,1]])
B = np.array([[1,0], [0,1]])
H = np.array([[1,0], [0,1]])
Q = np.array([[1,0], [0,1]])
R = np.array([[1,0], [0,1]])

x = np.array([[1], [0]])
y = np.array([[3], [5]])
u = np.array([[1], [1]])

kf = KF(x, P, F, B, H, Q, R)
kf.predict(u)
kf.update(y)


print("State = " + kf.to_str())
