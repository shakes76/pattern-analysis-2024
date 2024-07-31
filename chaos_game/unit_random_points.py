'''
Draw N points for the chaos game
'''
import numpy as np

N = 3

#create a unit circle
r = np.arange(0,N)
points = np.exp(2.0*np.pi*1j*r/N)
print("Points:", points)

#coordinates of the unit circle
res = 100
w = np.arange(0,res)
unit_circle = np.exp(2.0*np.pi*w*1j/res)

#pick random point
start = np.random.randint(0, N)
start_point = points[start]
print("Start:", start_point)

#plot
import matplotlib.pyplot as plt

plt.plot(np.real(unit_circle), np.imag(unit_circle), "b-")
plt.plot(np.real(points), np.imag(points), "r.")
plt.plot(np.real(start_point), np.imag(start_point), "g.")

plt.show()
print("END")