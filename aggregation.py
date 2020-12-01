import numpy as np
import matplotlib.pyplot as plt

        
def mamdani(evals, consecuentes, defuzz_f):
    
    alfas = [[a for i in range(0,100)] for a in evals]
    f = [0 for i in range(0,100)]

    for i in range(len(consecuentes)):
        temp = np.fmin(alfas[i], consecuentes[i])
        f = np.fmax(f, temp)
    
    return defuzz_f(f)

def larsen(evals, consecuentes, defuzz_f):
    
    alfas = [[a for i in range(0,100)] for a in evals]
    f = [0 for i in range(0,100)]

    for i in range(len(consecuentes)):
        temp = [val for val in map(lambda x,y: x*y, alfas[i], consecuentes[i])]
        f = np.fmax(f, temp)

    return defuzz_f(f)


