from dist import Dist

class Pascal(Dist):

    def __init__(self, N, n, p):
        super().__init__(N, n, p)

    def _rand(self):
        count, success = 0,0
        while(success < self.n):
            success+= 1 if (self.rand()<=self.p) else 0
            count+=1
        return count

    def _coef(self, k):
        return self.factorial(k-1)/(self.factorial(self.n-1)*self.factorial(k-self.n)

    def theory_mean(self):
        return self.n/self.p

    def theory_variance(self):
        return self.n*(1-self.p/self.p**2)
