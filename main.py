import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from difuzzifier import *
from aggregation import *

# Membership Functs
def get_membership_functions():
    x = np.arange(0,100)
    
    #Temperature
    
    # Medium
    cold = []
    for i in x:
        if i < 10 or i >= 20:
            cold.append(0)
        if i >= 10 and i < 15:
            cold.append((i-10)/(15 -10))
        if i >= 15 and i < 20:
            cold.append((15 - i)/ (20-15))

    #Normal
    normal = []
    for i in x:
        if i < 15 or i >= 23:
            normal.append(0)
        if i >= 15 and i < 21:
            normal.append((i-15)/(21 -15))
        if i >= 21 and i < 23:
            normal.append((15 - i)/ (20-15))

    warm = []
    for i in x:
        if i < 20 or i >= 35:
            warm.append(0)
        if i >= 20 and i < 25:
            warm.append((i-20)/(25 -20))
        if i >= 25 and i < 35:
            warm.append((35 - i)/ (35-20))

    hot = []
    for i in x:
        if i < 24 or i >= 100:
            hot.append(0)
        if i >= 24 and i < 44:
            hot.append((i-(24)/(44 -24)))
        if i >= 44 and i < 70:
            hot.append(1)
        if i >= 70 and i < 100:
            hot.append((100 -i)/(100-70))
    
    #Humidity

    dry = []
    for i in x:
        if i < -5 or i >= 12:
            dry.append(0)
        if i >= -5 and i < 1:
            dry.append((i- (-5))/(1 - (-5)))
        if i >= 1 and i < 8:
            dry.append(1)
        if i >= 8 and i < 12:
            dry.append((12 -i)/(12-8))
    
    wet = []
    for i in x:
        if i < 8 or i >= 35:
            wet.append(0)
        if i >= 8 and i < 12:
            wet.append((i- 8)/(12-8))
        if i >= 12 and i < 30:
            wet.append(1)
        if i >=30 and i < 35:
            wet.append((35 -i)/(35-30))
    
    soaked = []
    for i in x:
        if i < 20 or i >= 100:
            soaked.append(0)
        if i >= 20 and i < 40:
            soaked.append((i- 20)/(40-20))
        if i >= 40 and i < 70:
            soaked.append(1)
        if i >= 70 and i < 100:
            soaked.append((100 -i)/(100-70))
            
    # total dry time
    short = []
    for i in x:
        if i < 0 or i >= 20:
            short.append(0)
        if i >= 0 and i < 1:
            short.append(i)
        if i >= 1 and i < 10:
            short.append(1)
        if i >= 10 and i < 20:
            short.append((20 -i)/(20-10))
    
    medium = []
    for i in x:
        if i < 10 or i >= 55:
            medium.append(0)
        if i >= 10 and i < 25:
            medium.append((i- 10)/(25-10))
        if i >= 25 and i < 38:
            medium.append(1)
        if i >= 38 and i < 55:
            medium.append((55-i)/(55-38))

    long = []  
    for i in x:
        if i < 45 or i >= 110:
            long.append(0)
        if i >= 45 and i < 60:
            long.append((i- 45)/(60-45))
        if i >= 60 and i < 90:
            long.append(1)
        if i >= 90 and i < 110:
            long.append((110 -i)/(110-90))    
            
    return cold, normal, warm, hot, dry, wet, soaked, short, medium, long 

def fuzzyfy(t, h):
    temperature = {"cold":cold_t[t], "normal":nor_t[t], "warm": warm_t[t], "hot":hot_t[t]}
    humidity = {"dry":dry_h[h], "wet":wet_h[h], "soaked":soaked_h[h]}
    return temperature, humidity

def eval_rules(t, h):
    d1 = [] #long
    d2 = [] #short
    d3 = [] #medium

    d3.append(min(h["dry"], t["cold"]))
    d2.append(min(h["dry"], t["normal"]))
    d2.append(min(h["dry"], t["warm"]))
    d2.append(min(h["dry"], t["hot"]))

    d1.append(min(h["soaked"], t["cold"]))
    d1.append(min(h["soaked"], t["normal"]))
    d3.append(min(h["soaked"], t["warm"]))
    d3.append(min(h["soaked"], t["hot"]))

    d3.append(min(t["cold"], h["wet"]))
    d3.append(min(t["normal"], h["wet"]))
    d2.append(min(t["warm"], h["wet"]))    
    d2.append(min(t["hot"], h["wet"]))
    return d2,d3,d1    


t1 = int(input("Temperature: "))
h1 = int(input("Humidity: "))
x = range(100)
cold_t, nor_t, warm_t, hot_t, dry_h, wet_h, soaked_h, short, med, long  = get_membership_functions()

t, h = fuzzyfy(t1,h1)

r1,r2,r3 = eval_rules(t,h)

a = [max(r1), max(r2), max(r3)]
cons = [short, med, long]
print("Los resultados obtenidos segun las tecnicas utilizada son:")
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





