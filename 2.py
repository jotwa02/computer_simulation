import numpy as np
from scipy.stats import kurtosis
import matplotlib.pyplot as plt
import scipy.stats
n=100
#rozkład normalny
norm_distr = np.random.normal(0, 10, n)
np.savetxt('norm_distr.txt', np.round(norm_distr,decimals=2), fmt='%.2f')
nd = np.genfromtxt('norm_distr.txt', dtype='float', defaultfmt='%.2f')
average_nd = np.average(nd)
median_nd = np.median(nd)
kurtosis_nd = kurtosis(nd)
stdn = np.std(nd)
#rozkład płaski
unif_distr = np.random.uniform(0, 1, n)
np.savetxt("unif_distr.txt",unif_distr, fmt='%1.2f')
ud = np.genfromtxt('unif_distr.txt', dtype='float',  defaultfmt='%1.2f')
average_ud = np.average(ud)
median_ud = np.median(ud)
kurtosis_ud = kurtosis(ud)
#test chi kwadrat dla rozkładu płaskiego
r=10
rg = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
def chi():
    #wartości rozkładu płaskiego w liście
    ud_list = []
    for i in ud:
        ud_list.append(i)
    #tworzę 10 pustych list, bo tyle przedziałów
    pd = [[] for _ in range(r)]
    for k in range(len(rg)-1):
        for i in range(len(ud_list)):
            if rg[k]<ud_list[i] and ud_list[i]<=rg[k+1]:
                pd[k].append(ud_list[i])
    #wartości obserowane
    obs = []
    for i in range(len(pd)):
        obs.append(len(pd[i]))
    print('wartości obserowane: ',obs)
    #wartości oczekiwane
    ex = (n/r)
    exp_val = []
    if ex>=5:
        exp_val = r * [ex]
        print('wartości oczekiwane: ',exp_val)
    else:
        print('zła wartość oczekiwana')

    observed_val = np.array(obs)
    expected_val = np.array(exp_val)
    sub = observed_val-expected_val
    test_form = np.square(sub)/expected_val
    sum_test = np.sum(test_form)
    print("X^2: ", sum_test)
    alfa=0.95 #0.05
    free=r-1
    critical_val = scipy.stats.chi2.ppf(alfa, df=free)
    print('wartość krytyczna:', critical_val)
    if sum_test<critical_val:
        print('Hipoteza, że dane wygenerowane pochodzą z rozkładu płaskiego nie jest odrzucona. Zatem przyjujemy, że wygenerowane dane pochodzą z rozkładu płaskiego.')
    else:
        print('Hipoteza, że dane wygenerowane pochodzą z rozkładu płaskiego jest odrzucona. Zatem przyjujemy, że wygenerowane dane nie pochodzą z rozkładu płaskiego.')
chi()

#test kolomogorov-smirnov dla rozkładu normalnego
def ksmirnov():
    sort_norm = np.sort(norm_distr)
    lst = [i for i in range(1,n+1)]
    cumul = np.array(lst)
    expected = cumul/n
    ran = (cumul-1)/n
    data = []
    #cumulative distribution
    for i in range(len(sort_norm)):
        data.append(scipy.stats.norm.cdf(sort_norm[i], average_nd, stdn))
    difference = []
    for i in range(len(norm_distr)):
        difference.append(abs(data[i] - ran[i]))
    max_val = max(difference)
    print('wartość maksymalna: ',max_val)
    #alfa2 = 0.01
    #wartość krytczna dla n>40 w tym teście
    critical_val2 = 1.63/(n**0.5)
    if max_val<critical_val2:
        print('Hipoteza, że dane wygenerowane pochodzą z rozkładu normalnego nie jest odrzucona. Zatem przyjujemy, że wygenerowane dane pochodzą z rozkładu normalnego')
    else:
        print('Hipoteza, że dane wygenerowane pochodzą z rozkładu normalnego jest odrzucona. Zatem przyjujemy, że wygenerowane dane nie pochodzą z rozkładu normalnego')
ksmirnov()

#wykresy
plt.hist(norm_distr)
plt.title('rozkład normalny')
plt.show()
plt.plot(unif_distr)
plt.title('rozkład płaski')
plt.show()