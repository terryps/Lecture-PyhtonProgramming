import matplotlib.pyplot as plt
import math

x = [(x/1000-0.5)*20 for x in range(1000)]

def f(x):
    return 1/math.exp(x**2)*math.cos(5*x)-0.1

def graph(f,x):
    y = [f(t) for t in x]
    plt.plot(x,y)
    plt.show()

graph(f,x)
