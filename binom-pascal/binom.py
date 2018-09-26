from dist import Dist

class Binom(Dist):

    def __init__(self, N, n, p):
        super().__init__(N, n, p)

    def _rand(self):
        return self.sum(self.rand(self.n)<self.p)

    def _coef(self, k):
        return self.factorial(self.n)/(self.factorial(k)*self.factorial(self.n-k))

    def theory_mean(self):
        return self.n*self.p

    def theory_variance(self):
        return self.n*self.p*(1-self.p)
