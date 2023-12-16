import numpy as np


def f1(x): 
    return np.sin(x)*np.sin(x)

def f2(x): 
    return np.sin(x)

def f3(x): 
    return 0.5 * np.exp(-np.power(x, 2))

def f4(x):
    return x*np.exp(-x)*np.cos(2*x)

