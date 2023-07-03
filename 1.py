import numpy as np
from scipy.stats import kurtosis
#rozkład normalny
n=100
norm_distr = np.random.normal(0, 1, n)
np.savetxt('norm_distr.txt', np.round(norm_distr,decimals=2), fmt='%.2f')
nd = np.genfromtxt('norm_distr.txt', dtype='float', defaultfmt='%.2f')
print('rozkład normalny')
def norm_dist(data):
    average_nd = np.average(data)
    median_nd = np.median(data)
    kurtosis_nd = kurtosis(data)
    # skośność
    r_nd = norm_distr - average_nd
    po = np.power(r_nd, 2)
    odchy = ((sum(po) / n) ** 0.5)
    odchy3 = odchy ** 3
    pow3 = np.power(r_nd, 3)
    suu = np.sum(pow3)
    skewww = (suu) / ((n - 1) * odchy3)
    print("średnia:",average_nd,"mediana:" ,median_nd,"kurtoza:",kurtosis_nd,'skośność:', skewww)
    return average_nd, median_nd, kurtosis_nd, skewww
norm_dist(nd)

#rozkład płaski
unif_distr = np.random.uniform(0, 1, n)
np.savetxt("unif_distr.txt",unif_distr, fmt='%1.2f')
ud = np.genfromtxt('unif_distr.txt', dtype='float',  defaultfmt='%1.2f')
print('rozkład płaski')
def unif_dist(data):
    average_ud = np.average(data)
    median_ud = np.median(data)
    kurtosis_ud = kurtosis(data)
    #skośność
    r_ud = unif_distr-average_ud
    p = np.power(r_ud,2)
    odch = (sum(p)/n)**0.5
    pow3=np.power(r_ud,3)
    su = np.sum(pow3)
    odch3 = odch**3
    skeww = (su)/((n-1)*odch3)
    print("średnia:",average_ud,"mediana:" ,median_ud,"kurtoza:",kurtosis_ud,'skośność:', skeww)
    return average_ud, median_ud, kurtosis_ud, skeww
unif_dist(ud)