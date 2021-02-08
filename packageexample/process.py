import numpy as np


def multiply(*args):
    s = 1
    for a in args:
        s *= a
    return s


def random_matrix(x):
    return np.random.rand(x, x)
