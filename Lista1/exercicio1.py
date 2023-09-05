import numpy as np
import pylab as plt

data = np.loadtxt("dados_bola_caindo.dat")

y0 = 2
D = 0.065
g = 9.8
vt = np.sqrt(g/D)

def y1(t):
    return y0 - (g/2)*(t**2)

def y2(t):
    return y0-((vt**2)/g)*np.log(np.cosh(g*t/vt))



t = data[:,0]
y = data[:,1]
y1_data = []
y2_data = []


time = np.linspace(t[0],t[-1],100)
for t1 in time:
    d1 = y1(t1)
    d2 = y2(t1)
    y1_data.append(d1)
    y2_data.append(d2)

vm_t = []
tt = []
for i in range(len(t)-1):
    vm = (y[i+1]-y[i])/(t[i+1]-t[i])
    vm_t.append(vm)
    tt.append(t[i])


vmin = round(abs(np.max(vm_t)),2)
vmax = round(abs(np.min(vm_t)),2)

print("============================================================")
print("b) O modelo com resistência do ar descreve melhor os dados")
print("c) valor mínimo: "+str(vmin)+"m/s       Valor máximo: "+str(vmax)+" m/s")
print("============================================================")

plt.scatter(t,y,color='black')
plt.plot(time,y1_data,color='blue')
plt.plot(time,y2_data,color='red')
plt.xlabel("Tempo (s)", fontsize='15')
plt.ylabel("Posição (m)", fontsize='15')
plt.savefig("plot_exercicio1_ab.png")
plt.show()

plt.scatter(tt,vm_t, color='green')
plt.xlabel("Tempo (s)", fontsize='15')
plt.ylabel("Velocidade média (m/s)", fontsize='15')
plt.savefig("plot_exercicio1_c.png")
plt.show()