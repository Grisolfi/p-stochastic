import numpy as np

class Binom(object):

    def __init__(self, N, n, p):
        self.rand = np.random.random
        self.factorial = np.math.factorial
        self.N = N
        self.n = n
        self.p = p

    def rand_binom(self):
        return np.sum(self.rand(self.n)<self.p)

    def coef_binom(self, k):
        return self.factorial(self.n)/(self.factorial(k)*self.factorial(self.n-k))

    def rand_pascal(self):
        count, success = 0,0
        while(success < self.n):
            success+= 1 if (self.rand()<=self.p) else 0
            count+=1
        return count

    def pmf_teorica(self):
        kteorico = np.zeros(self.n)
        l = np.arange(self.n)+1
        for k in l:
            kteorico[k-1] = self.coef_binom(k) * ((self.p**k)*(1-self.p)**(self.n-k))
        return kteorico

    def pmf_pratica(self):
        return np.histogram(self.k_pratico(), np.arange(1,self.n)-0.5, density=self.N)

    def k_pratico(self):
        kpratico = np.zeros(self.N)
        l = np.arange(self.N)+1
        for k in l:
            kpratico[k-1] = self.rand_binom()
        return kpratico

    def media_teorica(self):
        return self.n*self.p

    def media_pratica(self):
        return np.mean(self.k_pratico())

    def variancia_teorica(self):
        return self.n*self.p*(1-self.p)

    def variancia_pratica(self):
        return np.var(self.k_pratico())

    def meds_vars(self):
        return """
        Média teórica: {0}
        Média prática: {1}
        Variância teórica: {2}
        Variância prática: {3}
        """.format(self.media_teorica(), self.media_pratica(),
                        self.variancia_teorica(), self.variancia_pratica())
