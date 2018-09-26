import numpy as np
import matplotlib.pyplot as plt
from binom import Binom
import sys

if __name__ == '__main__':

    N = int(sys.argv[1])
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    f, axarr = plt.subplots(1,2)
    b1 = Binom(N, 10,0.1)
    y = np.arange(10)+1
    axarr[0].set_title("K ~ Binom(10, 1/10)")
    axarr[0].stem(y, b1.pmf_teorica(), linefmt='r', markerfmt='ro')
    axarr[0].hist(b1.k_pratico(), np.arange(1,10)-0.5, density=N)
    axarr[0].text(0.35, 0.95, b1.meds_vars(), transform=axarr[0].transAxes, fontsize=8,
        verticalalignment='top', bbox=props)

    # questao b
    b2 = Binom(N, 50,0.25)
    y = np.arange(50)+1
    axarr[1].set_title("K ~ Binom(50, 1/4)")
    axarr[1].stem(y, b2.pmf_teorica(), linefmt='r', markerfmt='ro')
    axarr[1].hist(b2.k_pratico(), np.arange(1,50)-2.5, density=N)
    axarr[1].text(0.35, 0.95, b2.meds_vars(), transform=axarr[1].transAxes, fontsize=8,
        verticalalignment='top', bbox=props)
    plt.show()

    #
    # y = np.arange(n)+1
    # kpratico = pre.k_pratico(N, n, p)
    # plt.title("PMFs Binomiais")
    # plt.stem(y, pre.pmf_teorica(n, p), linefmt='r', markerfmt='ro')
    # plt.hist(kpratico, np.arange(1,n)-0.5, density=N, color='yellow')
    # plt.text(x=6,y=0.3, s ="Médias e Variâncias:")
    # plt.text(x=6,y=0.28, s="Média Teórica: {}".format(str(n*p)))
    # plt.text(x=6,y=0.26, s="Média Prática: {}".format(str(np.mean(kpratico))))
    # plt.text(x=6,y=0.24, s="Variância Teórica: {}".format(str(n*p*(1-p))))
    # plt.text(x=6,y=0.22, s="Variância Prática: {}".format(np.around(a=np.var(kpratico), decimals=8)))
    # plt.show()
