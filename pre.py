import numpy as np
import matplotlib.pyplot as plt
import sys

class Estocasticos(object):

    def __init__(self):
        self.rand = np.random.random

    def rand_binom(self, n, p):
        return np.sum(self.rand(n)<p)

    def coef_binom(self, n, k):
        return np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k))

    def rand_pascal(self, n, p):
        count, success = 0,0
        while(success < n):
            success+= 1 if (self.rand()<=p) else 0
            count+=1
        return count

    def pmf_teorica(self, n, p):
        kteorico = np.zeros(n)
        l = np.arange(n)+1
        for k in l:
            kteorico[k-1] = self.coef_binom(n,k) * ((p**k)*(1-p)**(n-k))
        return kteorico

    def pmf_pratica(self, N, n, p):
        kpratico = self.k_pratico(N,n,p)
        print(len(kpratico))
        freq = np.histogram(kpratico, bins=np.arange(n))
        return freq/N

    def k_pratico(self, N, n, p):
        kpratico = np.zeros(N)
        l = np.arange(N)+1
        for k in l:
            kpratico[k-1] = self.rand_binom(n,p)
        return kpratico

if __name__ == '__main__':

    pre =  Estocasticos()
    # PMF TEORICA
    try:
        N = int(sys.argv[1])
        n = int(sys.argv[2])
        p = float(sys.argv[3])

        y = np.arange(n)
        kpratico = pre.k_pratico(N, n, p)
        plt.title("PMFs Binomiais")
        plt.stem(y, pre.pmf_teorica(n, p), 'r')
        plt.hist(kpratico, bins=np.arange(0,n+2), density=N, color='yellow')
        plt.text(x=6,y=0.3, s ="Médias e Variâncias:")
        plt.text(x=6,y=0.28, s="Média Teórica: {}".format(str(n*p)))
        plt.text(x=6,y=0.26, s="Média Prática: {}".format(str(np.mean(kpratico))))
        plt.text(x=6,y=0.24, s="Variância Teórica: {}".format(str(n*p*(1-p))))
        plt.text(x=6,y=0.22, s="Variância Prática: {}".format(np.around(a=np.var(kpratico), decimals=8)))
        plt.show()


    except Exception as e:
        print(e)
