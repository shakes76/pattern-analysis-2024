'''
Compute the chaos game for N points
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

#start
start = 0.1+0.5j

def compute_new_rand_location(startLoc):
    rand_location = np.random.randint(0, N)
    #print(rand_location, points[rand_location])
    vector = (points[rand_location] - startLoc)/2.0
    new_point = startLoc + vector
    return new_point, points[rand_location]

#compute the chaos game
iterations = 1000

#plot
import matplotlib.pyplot as plt

plt.plot(np.real(unit_circle), np.imag(unit_circle), "b-")
plt.plot(np.real(points), np.imag(points), "r.")
plt.plot(np.real(start), np.imag(start), "y.")

next_point = start
for iteration in range(iterations):
    next_point, rand_location = compute_new_rand_location(next_point)
    plt.plot(np.real(next_point), np.imag(next_point), "b.")

plt.show()
print("END")