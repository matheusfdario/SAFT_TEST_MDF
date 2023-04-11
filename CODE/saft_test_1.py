import numpy as np
import matplotlib.pyplot as plt
import scipy.io

file = "DadosEnsaio.mat"

mat = scipy.io.loadmat(file)

pi = 500  # Amostra inicial dos A-Scan
pf = 900  # Amostra final dos A-Scan
g = mat["ptAco40dB_1"]["AscanValues"][0][0][pi:pf]  # B-Scan
cl = mat["ptAco40dB_1"]["CscanData"][0][0]["Cl"][0][0][0][0]  # Velocidade (escalar)
t = mat["ptAco40dB_1"]["timeScale"][0][0][pi:pf] * 1e-6  # Tempo
T = t[1][0] - t[0][0]  # Período de amostragem (escalar)
z = cl * t / 2  # Conversão para posição /2->ida/volta
x = mat["ptAco40dB_1"]["CscanData"][0][0]["X"][0][0] * 1e-3  # Posições transdut

def saft(g, x, z, cl, T):
    nz, nx = g.shape
    print(nx,nz)
    nz = len(z)  # number of elements in z
    f = np.zeros((nz, nx))  # initialize the output matrix f
    maxval = 0
    for a in range(g.shape[0]):
        for b in range(g.shape[1]):
            if(maxval<g[a,b]):
                maxval=g[a,b]
    print(maxval)
    for i in range(nx):  # fix loop variable to iterate only up to nx
        for j in range(nx):
            for k in range(nx):
                d = np.sqrt((x[k] - x[i])**2 + z[j]**2)  # compute distance
                tdelay = 2 * d / cl  # compute time delay
                tdelay_idx = int(tdelay / T)  # compute index in g for time delay
                #print(g)
                #for s in range()
                if tdelay_idx < nz:  # ensure index is within bounds of g
                    f[i, j] = f[i,j] + g[j,tdelay_idx]  # perform SAFT

    return f

plt.figure()
plt.imshow(g, aspect="auto")
plt.title('B-Scan')

plt.figure()
f = saft(g, x, z, cl, T)
plt.imshow(f, aspect="auto")
plt.title('SAFT')
plt.show()