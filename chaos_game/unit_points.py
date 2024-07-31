'''
Draw N points for the chaos game
'''
import numpy as np

N = 3

#create a unit circle
r = np.arange(0,N)
points = np.exp(2.0*np.pi*1j*r/N)
print("Points:", points)
