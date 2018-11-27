from dist import Dist

class Pascal(Dist):


    """
%Questão 2.b X~Pascal(2,1/2).

N = 500000; % N° de simulaçoes
n = 2; % N° de sucessos da pascal
p = 1/2;% Probabilidade de sucesso
X = zeros(1,N);
E_x_teor = n/p
Var_x_teor =n*(1-p)/p^2
for ii = 1 : N
  X(ii) = rand_pascal(n,p);
endfor
x = n : max(X);
freq = hist(X,x);
E_x_prat = mean(X)
Var_x_prat = var(X)
pmf_prat = freq/N;


figure;
hold on;
bar(x,pmf_prat,'y');
stem(x,pmf_teor, 'b');
grid on;

    """

    def __init__(self, N, n, p):
        super().__init__(N, n, p)

    def _rand(self):
        count, success = 0,0
        while(success < self.n):
            success+= 1 if (self.rand()<=self.p) else 0
            count+=1
        return count

    def _coef(self, k):
        # pasc = factorial(x-1)./(factorial(n-1).*factorial(x-n));
        # pmf_teor = pasc.*(p.^n) .* ((1-p).^(x-n));
        return self.factorial(k-1)/(self.factorial(self.n-1)*self.factorial(k-self.n)

    def theory_pmf(self):
        return self._coef*self.pn**self.n *(1-self.p)**

    def theory_mean(self):
        return self.k/self.p

    def theory_variance(self):
        return self.k*(1-self.p/self.p**2)
