import numpy as np
import matplotlib.pyplot as plt
from binom import Binom
import sys

if __name__ == '__main__':

    N = int(sys.argv[1])
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    f, axarr = plt.subplots(2,2)

    # questao 1b1
    b1 = Binom(N, 10,0.1)
    y = np.arange(10)+1
    axarr[0,0].set_title("K ~ Binom(10, 1/10)")
    axarr[0,0].stem(y, b1.theory_pmf(), linefmt='r', markerfmt='ro')
    axarr[0,0].hist(b1.random_variable(), np.arange(1,10)-0.5, density=N)
    axarr[0,0].text(0.35, 0.95, str(b1), transform=axarr[0,0].transAxes, fontsize=8,
        verticalalignment='top', bbox=props)

    # questao 1b2
    b2 = Binom(N, 50,0.25)
    y = np.arange(50)+1
    axarr[0,1].set_title("K ~ Binom(50, 1/4)")
    axarr[0,1].stem(y, b2.theory_pmf(), linefmt='r', markerfmt='ro')
    axarr[0,1].hist(b2.random_variable(), np.arange(1,50)-2.5, density=N)
    axarr[0,1].text(0.35, 0.95, str(b2), transform=axarr[0,1].transAxes, fontsize=8,
        verticalalignment='top', bbox=props)

    # questao



    plt.show()
