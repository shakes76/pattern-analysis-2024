'''
Compute the phase space of the logistic model
'''
import numpy as np
import matplotlib.pylab as plt

def logistic(r, x):
    '''
    The logistic equation
    '''
    return r * x * (1 - x)

N = 1000
T = np.arange(N)

x0 = 0.5
#delta_r number of r points between the range 0.6 - 3.5
delta_r = 10000
r_values = np.linspace(0.6, 4.0, delta_r)
x = x0 * np.ones_like(r_values)

fig = plt.figure(figsize=(8,6))

last = 100
for t in T:
    x = logistic(r_values, x)

    #Display the plot
    if t >= (N - last):
        plt.plot(r_values, x, ',k', alpha=.33)

plt.show()
