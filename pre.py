import numpy as np
import matplotlib.pyplot as plt


class Estocasticos(object):

    def __init__(self):
        self.rand = np.random.random
        self.factorial = np.math.factorial
        pass

    def rand_binom(self, n, p):
        return np.sum(self.rand(n)<p)

    def coef_binom(self, k, n):
        return self.factorial(n)/(self.factorial(k))*self.factorial(n-k)
