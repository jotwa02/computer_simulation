import numpy as np
a=0
b=1
N=1000
h = (b-a)/N
unifdist = np.random.uniform(a,b,N)
unifdist2 = np.random.uniform(a,b,N)
udist = unifdist.tolist()
udist2 = unifdist2.tolist()

def func(x):
    return x**2+2*x

#riemann integration
def riemann():
    l1_unif=[]
    for i in range(N):
        f1 = func(unifdist[i])
        l1_unif.append(f1)
        c = np.array(l1_unif)
    sc = np.sum(c)
    l2_unif = []
    for i in range(N-1):
        f2=func(unifdist[i])
        l2_unif.append(f2)
        d = np.array(l2_unif)
    sd = np.sum(d)
    integral = h * ((sc+sd)/2)
    print('całka riemanna:',integral)
riemann()

def montecarlo():
    l_unif=[]
    for i in range(N):
        f1 = func(unifdist[i])
        l_unif.append(f1)
        c = np.array(l_unif)
    s = np.sum(c)
    integral = h * s
    print('całka monte carlo:',integral)
montecarlo()

#pole trójkąta niesymetrycznego za pomocą monte carlo
#trójkąt jest ogrniaczony prostymi: y=2x, x=2, y=0
l_xi = []
l_yi = []
#punkty przecięcia
a1=0
b1=2
a2=0
b2=4
for i in range(N):
    xi = a1 + (b1-a1)*udist[i]
    l_xi.append(xi)
    yi = a2 + (b2-a2)*udist2[i]
    l_yi.append(yi)
l=0
for i in range(N):
    if l_xi[i]*2>=l_yi[i] and l_yi[i]>=a2 and l_yi[i]<=b2 and l_xi[i]<=b1:
        l+=1
    else:
        l+=0
#p=pole prostokąta * ilość punktów w trójkącie/ilość wszystkich punktów
p=(b1*b2)*(l/N)
print('pole trójkąta: ',p)