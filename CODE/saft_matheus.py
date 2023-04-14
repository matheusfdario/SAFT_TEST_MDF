#!/usr/bin/env python3
# -*- coding, utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import math

file = "DadosEnsaio.mat"

mat = scipy.io.loadmat(file)

pi = 500  # Amostra inicial dos A-Scan
pf = 900  # Amostra final dos A-Scan
zmax = 0 
g = mat["ptAco40dB_1"]["AscanValues"][0][0][pi:pf]  # B-Scan
cl = mat["ptAco40dB_1"]["CscanData"][0][0]["Cl"][0][0][0][0]  # Velocidade
t = mat["ptAco40dB_1"]["timeScale"][0][0][pi:pf]*1e-6  # Tempo
T = t[1][0]-t[0][0]  # Período de amostragem
z = cl*t/2  # Conversação para posição /2->ida/volta
x = mat["ptAco40dB_1"]["CscanData"][0][0]["X"][0][0]*1e-3  # Posições transdut

def saft(g, x, z, cl, T):
    N = len(x)
    Nz = len(z)
    f = np.zeros((Nz, N))

    for i in range(N):
        for j in range(Nz):
            for n in range(N):
                tau = (2 * np.sqrt((x[n] - x[i]) ** 2 + z[j] ** 2)) / cl
                tau_idx = int(np.round(tau / T))
                tau_idx = tau_idx-pi
                if(tau_idx<399):
                    f[j, i] += g[tau_idx,n]
    return f

plt.figure()
plt.imshow(g, aspect="auto")
plt.title('B-Scan -  Matheus Fortunato Dário')
plt.figure()
f = saft(g, x, z, cl, T)
plt.imshow(f, aspect="auto")
plt.title('SAFT -  Matheus Fortunato Dário')
plt.show()
