from dist import Dist

class Binom(Dist):

    def __init__(self, N, n, p):
        super().__init__(N, n, p)
        self.n = self.a

    def _rand(self):
        return self.sum(self.rand(self.n)<self.p)

    def _coef(self, i):
        return self.factorial(self.n)/(self.factorial(i)*self.factorial(self.n-i))

    def theory_pmf(self):
        X_theory = np.zeros(self.n)
        vector = np.arange(self.n)+1
        for i in vector:
            X_theory[i-1] = self._coef(i) * ((self.p**i)*(1-self.p)**(self.n-i))
        return X_theory

    def theory_mean(self):
        return self.n*self.p

    def theory_variance(self):
        return self.n*self.p*(1-self.p)
