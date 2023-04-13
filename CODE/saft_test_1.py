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
    cont = 0
    nx = len(x)
    nz = len(z)
    nxt = len(x)  # number of elements in z
    f = np.zeros((nzg, nxg))  # initialize the output matrix f
    #print(nxg,nzg,nxt,g[0][1],x[0],x[1])
    
    for i in range(nxg):  # fix loop variable to iterate only up to nx
        for j in range(nzg):
            for k in range(nxt):
                #print("1-",k,i,j)

                XT = x[k]
                X0 = g[j][i]
                Z0 = z[j]
                td = int(2*((np.sqrt((XT - X0)**2 + Z0**2))/cl))  # compute distance
                #print("2-",x[k],g[j][i],z[j],td)
                #print("f",abs(g[j][i]-td))
                if(abs(g[j][i]-td)==0):    
                    #print("f",cont,abs(g[j][i]-td))
                    cont=cont+1
                    f[j,i] = f[j,i] + g[j,i]
    return f

f = saft(g, x, z, cl, T)


plt.figure()
plt.imshow(g, aspect="auto")
plt.title('B-Scan')

plt.figure()
f = saft(g, x, z, cl, T)
plt.imshow(f, aspect="auto")
plt.title('SAFT')
plt.show()