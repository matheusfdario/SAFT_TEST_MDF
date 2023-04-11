#!/usr/bin/env python3
# -*- coding, utf-8 -*-

#normal coment
#* highlighted coment
#! urgent coment
#? question coment
#TODO important coments

#? Ultrassonic cristals? piezoelectric effect?
#? 1984? Almost 30 years? why?
#? A-scan?B-scan?what is this?

import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import math
from scipy.interpolate import interp1d

file = "DadosEnsaio.mat"

mat = scipy.io.loadmat(file)

pi = 500  # Amostra inicial dos A-Scan
pf = 900  # Amostra final dos A-Scan
g = mat["ptAco40dB_1"]["AscanValues"][0][0][pi:pf]  # B-Scan
cl = mat["ptAco40dB_1"]["CscanData"][0][0]["Cl"][0][0][0][0]  # Velocidade
t = mat["ptAco40dB_1"]["timeScale"][0][0][pi:pf]*1e-6  # Tempo
T = t[1][0]-t[0][0]  # Período de amostragem
z = cl*t/2  # Conversação para posição /2->ida/volta
x = mat["ptAco40dB_1"]["CscanData"][0][0]["X"][0][0]*1e-3  # Posições transdut

def saft(g, x, z, cl, T):
    nz, nx = g.shape
    f = np.zeros((nz, nx))  # Cria matriz para armazenar os resultados
    for j in range(nx):
        for i in range(nz):
            tdelay = 2 * z[i] / cl  # Cálculo do atraso em função da posição
            tdelay_idx = int(tdelay / T)  # Índice do atraso no vetor de tempo
            if tdelay_idx >= 0 and tdelay_idx < nx:
                f[i, j] = g[i, tdelay_idx]

    return f

# Example usage
# Assume g is your input B-scan data, x is the position of transducer elements,
# z is the conversion of time to position, cl is the speed of sound, and T is the
# time period of the samples.
# You can replace these variables with your own data and parameters.

# Load or generate g, x, z, cl, T

# Display the B-scan data
plt.figure()
plt.imshow(g, aspect="auto")
plt.title('B-Scan')

# Perform SAFT
f = saft(g, x, z, cl, T)

# Display the SAFT result
plt.figure()
plt.imshow(f, aspect="auto")
plt.title('SAFT')

plt.show()
