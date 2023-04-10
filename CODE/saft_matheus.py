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
g = mat["ptAco40dB_1"]["AscanValues"][0][0][pi:pf]  # B-Scan
cl = mat["ptAco40dB_1"]["CscanData"][0][0]["Cl"][0][0][0][0]  # Velocidade
t = mat["ptAco40dB_1"]["timeScale"][0][0][pi:pf]*1e-6  # Tempo
T = t[1][0]-t[0][0]  # Período de amostragem
z = cl*t/2  # Conversação para posição /2->ida/volta
x = mat["ptAco40dB_1"]["CscanData"][0][0]["X"][0][0]*1e-3  # Posições transdut


def saft(g, x, z, cl, T):
    f = np.zeros_like(g)
    # Completar
    return f


plt.figure()
plt.imshow(g, aspect="auto")
plt.title('B-Scan')

plt.figure()
f = saft(g, x, z, cl, T)
plt.imshow(f, aspect="auto")
plt.title('SAFT')
