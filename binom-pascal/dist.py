import numpy as np

class Dist(object):

    def __init__(self, N, n, p):
        self.rand = np.random.random
        self.factorial = np.math.factorial
        self.sum = np.sum
        self.N = N
        self.n = n
        self.p = p
        self.args = {
            'mt': self.theory_mean(),
            'vt': self.theory_variance(),
            'mp': self.simulation_mean(),
            'vp': self.simulation_variance()
        }

    def __str__(self):
        return """
        Média teórica: {mt}
        Média prática: {mp}
        Variância teórica: {vt}
        Variância prática: {vp}
        """.format(**self.args)

    def pmf_teorica(self):
        kteorico = np.zeros(self.n)
        l = np.arange(self.n)+1
        for k in l:
            kteorico[k-1] = self._coef(k) * ((self.p**k)*(1-self.p)**(self.n-k))
        return kteorico

    def random_variable(self):
        kpratico = np.zeros(self.N)
        l = np.arange(self.N)+1
        for k in l:
            kpratico[k-1] = self._rand()  #rand_binom || rand_pascal
        return kpratico

    # TODO Integrate this method with plt.bar plot type
    # def pmf_pratica(self):
    #     return np.histogram(self.random_variable(), np.arange(1,self.n)-0.5, density=self.N)

    def simulation_mean(self):
        return np.mean(self.random_variable())

    def simulation_variance(self):
        return np.var(self.random_variable())
