import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from difuzzifier import *
from aggregation import *

# Membership Functs
def get_membership_functions():
    x = np.arange(0,100)
    
    #Temperatura
    congelado = []
    for i in x:
        if i < -100 or i >= 13:
            congelado.append(0)
        if i >= -100 and i < -60:
            congelado.append((i-(-60)/(-100-(-60))))
        if i >= -60 and i < 0:
            congelado.append(1)
        if i >= 0 and i < 13:
            congelado.append((13 -i)/13)
    # Medium
    frio = []
    for i in x:
        if i < 10 or i >= 20:
            frio.append(0)
        if i >= 10 and i < 15:
            frio.append((i-10)/(15 -10))
        if i >= 15 and i < 20:
            frio.append((15 - i)/ (20-15))

    # High
    normal = []
    for i in x:
        if i < 15 or i >= 23:
            normal.append(0)
        if i >= 15 and i < 21:
            normal.append((i-15)/(21 -15))
        if i >= 21 and i < 23:
            normal.append((15 - i)/ (20-15))

    tibio = []
    for i in x:
        if i < 20 or i >= 35:
            tibio.append(0)
        if i >= 20 and i < 25:
            tibio.append((i-20)/(25 -20))
        if i >= 25 and i < 35:
            tibio.append((35 - i)/ (35-20))

    caliente = []
    for i in x:
        if i < 24 or i >= 100:
            caliente.append(0)
        if i >= 24 and i < 44:
            caliente.append((i-(24)/(44 -24)))
        if i >= 44 and i < 70:
            caliente.append(1)
        if i >= 70 and i < 100:
            caliente.append((100 -i)/(100-70))
    
    #Humedad

    seco = []
    for i in x:
        if i < -5 or i >= 12:
            seco.append(0)
        if i >= -5 and i < 1:
            seco.append((i- (-5))/(1 - (-5)))
        if i >= 1 and i < 8:
            seco.append(1)
        if i >= 8 and i < 12:
            seco.append((12 -i)/(12-8))
    
    humedo = []
    for i in x:
        if i < 8 or i >= 35:
            humedo.append(0)
        if i >= 8 and i < 12:
            humedo.append((i- 8)/(12-8))
        if i >= 12 and i < 30:
            humedo.append(1)
        if i >=30 and i < 35:
            humedo.append((35 -i)/(35-30))
    
    mojado = []
    for i in x:
        if i < 20 or i >= 100:
            mojado.append(0)
        if i >= 20 and i < 40:
            mojado.append((i- 20)/(40-20))
        if i >= 40 and i < 70:
            mojado.append(1)
        if i >= 70 and i < 100:
            mojado.append((100 -i)/(100-70))
            
    # tiempo regado
    corto = []
    for i in x:
        if i < 0 or i >= 20:
            corto.append(0)
        if i >= 0 and i < 1:
            corto.append(i)
        if i >= 1 and i < 10:
            corto.append(1)
        if i >= 10 and i < 20:
            corto.append((20 -i)/(20-10))
    
    medio = []
    for i in x:
        if i < 10 or i >= 55:
            medio.append(0)
        if i >= 10 and i < 25:
            medio.append((i- 10)/(25-10))
        if i >= 25 and i < 38:
            medio.append(1)
        if i >= 38 and i < 55:
            medio.append((55-i)/(55-38))

    largo = []  
    for i in x:
        if i < 45 or i >= 110:
            largo.append(0)
        if i >= 45 and i < 60:
            largo.append((i- 45)/(60-45))
        if i >= 60 and i < 90:
            largo.append(1)
        if i >= 90 and i < 110:
            largo.append((110 -i)/(110-90))    
            
    return congelado, frio, normal, tibio, caliente, seco, humedo, mojado, corto, medio, largo


def fuzzyfy(t, h):
    temperatura = {"congelado":cong[t], "frio":fri[t], "normal":nor[t], "tibio": tib[t], "caliente":cal[t]}
    humedad = {"seco":seco[h], "humedo":hum[h], "mojado":moj[h]}
    return temperatura, humedad

def eval_rules(t, h):
    d1 = [] #regado largo
    d2 = [] #regado corto
    d3 = [] #regado medio

    d1.append(min(h["seco"], t["congelado"]))
    d1.append(min(h["seco"], t["frio"]))
    d1.append(min(h["seco"], t["normal"]))
    d1.append(min(h["seco"], t["tibio"]))
    d1.append(min(h["seco"], t["caliente"]))

    d2.append(min(h["mojado"], t["congelado"]))
    d2.append(min(h["mojado"], t["frio"]))
    d2.append(min(h["mojado"], t["normal"]))
    d2.append(min(h["mojado"], t["tibio"]))
    d2.append(min(h["mojado"], t["caliente"]))
    d2.append(min(h["humedo"], t["congelado"]))

    d3.append(min(t["frio"], h["humedo"]))
    d3.append(min(t["normal"], h["humedo"]))
    d3.append(min(t["tibio"], h["humedo"]))    
    d3.append(min(t["caliente"], h["humedo"]))
    return d2,d3,d1    


t1 = int(input("Temperatura: "))
h1 = int(input("Humedad: "))
x = range(100)
cong, fri, nor, tib, cal, seco, hum, moj, cor, med, lar  = get_membership_functions()

t, h = fuzzyfy(t1,h1)

r1,r2,r3 = eval_rules(t,h)

a = [max(r1), max(r2), max(r3)]
cons = [cor, med, lar]

print("\nMamdani")
print("Media de los maximos")
print(mamdani(a, cons, med_max))
print("Centroide")
print(mamdani(a, cons, centroide))
print("Bisector")
print(mamdani(a, cons, bisector))

print("\nLarsen")
print("Media de los maximos")
print(larsen(a, cons, med_max))
print("Centroide")
print(larsen(a, cons, centroide))
print("Bisector")
print(larsen(a, cons, bisector))





