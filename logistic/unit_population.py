'''
Unit test for computing the logistic equation
'''
import numpy as np
import matplotlib.pyplot as plt

N = 30 #number of timesteps
x = 0.5
r = 1.5

T = np.arange(N)
X = np.zeros(N)

for t in T:
    x = r*x*(1-x)
    X[t] = x

plt.plot(T, X, '-k')
plt.show()
