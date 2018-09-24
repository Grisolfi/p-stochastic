import numpy as np
import matplotlib.pyplot as plt
import sys

class Estocasticos(object):

    def __init__(self):
        self.rand = np.random.random
        self.factorial = np.math.factorial

    def rand_binom(self, n, p):
        return np.sum(self.rand(n)<p)

    def coef_binom(self, k, n):
        return self.factorial(n)/(self.factorial(k))*self.factorial(n-k)

    def pmf_teorica(self, n, p):
        kteorico = np.zeros(n)
        l = np.arange(n)
        for k in l:
            kteorico[k] = self.coef_binom(k,n) * ((p**k)*(1-p)**(n-k))
        return kteorico

    def pmf_pratica(self, N, n, p):
        kpratico = np.zeros(N)
        l = np.arange(N)
        for k in l:
            kpratico[k] = pre.rand_binom(n,p)
        return np.histogram(kpratico, np.arange(n))/N

if __name__ == '__main__':

    pre =  Estocasticos()
    # PMF TEORICA
    try:
        N = int(sys.argv[1])
        n = int(sys.argv[2])
        p = float(sys.argv[3])

        y = np.arange(n)

        print(pre.pmf_teorica(n,p))
        # plt.title("PMFs Binomiais")
        # plt.stem(y, pre.pmf_teorica(n, p), 'b')
        # # plt.stem(y, pre.pmf_pratica(N, n, p), 'r')
        # plt.show()

    except Exception as e:
        print(e)
