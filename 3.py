import numpy as np
from scipy import stats
import math
#rozkład płaski
def unifdist(n):
    unif_distr = np.random.uniform(0, 1, n)
    np.savetxt('unif_distr.txt', np.round(unif_distr, decimals=2), fmt='%.2f')
    ud = np.genfromtxt('unif_distr.txt', dtype='float', defaultfmt='%.2f')
    return (ud)
value1 = unifdist(40)
def lcg(n,x0):
    a = 7**5
    b = 0
    c = 2**31-1
    l = []
    for i in range(n):
        x0 = (a * x0 + b) % c
        z = x0/c
        l.append(z)
        new = [round(item, 2) for item in l]
        npl = np.array(new)
    return npl

value2 = lcg(n=40, x0=2000)

def wilcoxntest(x,y):
    i = np.array([0])
    dif = np.subtract(x,y)
    new_dif = np.setdiff1d(dif,i)
    dif_tolist = new_dif.tolist()
    abs_dif = [abs(e) for e in dif_tolist]
    abs_dif = [i for i in abs_dif if i != 0]
    rank = list(range(1,len(abs_dif)+1))
    zipped = [i for i in zip(dif_tolist, abs_dif, rank)]
    lmin = []
    lplus = []
    for i in range(0,len(zipped)):
        if zipped[i][0] < 0:
            lmin.append(zipped[i][2])
            Sum_min = sum(lmin)
        else:
            lplus.append(zipped[i][2])
            Sum_plus = sum(lplus)

    minimum = min(Sum_min, Sum_plus)
    n = len(zipped)
    mean = n*(n+1)/4
    os = ((n*(n+1)*(2*n+1))/24)**0.5
    z = (minimum-mean)/os
    print('z:',z, ',poziom istotności 5%')
    #poziom istotności 5%
    if z>-1.96 or z>1.96:
        print('Nie ma różnicy między danymi z lcg i random.uniform')
    else:
        print('Jest różnica między danymi z lcg i random.uniform')
wilcoxntest(value1,value2)

#rozkład normalny
def normdist(n):
    norm_distr = np.random.normal(0, 2, n)
    np.savetxt('norm_distr.txt', np.round(norm_distr, decimals=2), fmt='%.2f')
    nd = np.genfromtxt('norm_distr.txt', dtype='float', defaultfmt='%.2f')
    return nd
v1 = normdist(50)

def box_muller(n):
    unif_distr1 = np.random.uniform(0, 1, n)
    u1 = np.round(unif_distr1,2)
    unif_distr2 = np.random.uniform(0, 1, n)
    u2 = np.round(unif_distr2,2)
    l_z0 = []
    for i in range(n):
        z0 = (-2*math.log(u1[i]))**0.5*math.cos(2*math.pi*u2[i])
        l_z0.append(z0)
        np_lz0=np.array(l_z0)
        r = np.round(np_lz0,2)
        return r
v2 = box_muller(50)

def tstudenttest(x,y,n):
    meannd = np.mean(x)
    stdtnd = np.std(x)
    variancend = stdtnd**2
    meanbm = np.mean(y)
    stdtbm = np.std(y)
    variancebm = stdtbm**2
    t = abs((meannd-meanbm))/((variancend*n/n + variancebm*n/n)**0.5)
    critical = stats.t.ppf(q=0.95, df=50)
    p = 1-stats.t.cdf(x=t, df=50)
    print("p:", p)
    alfa=0.05
    print("wartość krytyczna, poziom istotności 5%:",critical)
    if alfa<p:
        print('Nie ma różnicy między transformatą boxa-mullera i random.normal')
    else:
        print('Jest różnica między transformatą boxa-mullera i random.normal')
tstudenttest(v1,v2,50)
