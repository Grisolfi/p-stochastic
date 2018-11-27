import numpy as np

class Dist(object):

    def __init__(self, SAMPLES, a, p):
        self.rand = np.random.random
        self.factorial = np.math.factorial
        self.sum = np.sum
        self.SAMPLES = SAMPLES
        self.n = n # Number of experiments
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

    def random_variable(self):
        X_simulation = np.zeros(self.SAMPLES)
        vector = np.arange(self.SAMPLES)+1
        for i in l:
            X_simulation[i-1] = self._rand()  #rand_binom || rand_pascal
        return X_simulation

    # TODO Integrate this method with plt.bar plot type
    # def pmf_pratica(self):
    #     return np.histogram(self.random_variable(), np.arange(1,self.n)-0.5, density=self.N)

    def simulation_mean(self):
        return np.mean(self.random_variable())

    def simulation_variance(self):
        return np.var(self.random_variable())
