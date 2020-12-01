#import scipy as sc
from scipy import integrate

def med_max(f):
    m = f[0]
    x = []
    for i in range((len(f))):
        if f[i] > m:
            x.clear()
            m = f[i]
        if f[i] == m:
            x.append(i)
    return x[int(len(x)/2)]
           

def centroide(f):
    l = [(i,f[i]) for i in range(len(f))]
    l.insert(0,(0,0))
    l.append((99,0))
    l.append((0,0))
    a = 0
    for i in range(len(l) - 1):
        a += l[i][0]*l[i+1][1] - l[i+1][0]*l[i][1]
    a *= 1/2
    x = 0
    for i in range(len(l) - 1):
        x += (l[i][0] + l[i+1][0])*(l[i][0]*l[i+1][1] - l[i+1][0]*l[i][1])
    x *= 1/(a*6)
    return x
    

def bisector(f):
    min_dif = 1000
    pos = 0
    x = range(100)
    for i in x:
        al = integrate.trapz(f[:i], x[:i])
        ar = integrate.trapz(f[i:], x[i:])
        dif = abs(al - ar)
        if dif < min_dif:
            min_dif = dif
            pos = i
    return pos
    