import numpy as np

total_data = np.loadtxt("dados_moleculas.dat")

def Ixx(mi,yi,zi):
    sum = 0
    for i in range(len(yi)):
        sum += mi[i]*((yi[i])**2+(zi[i])**2)
    return sum

def Iyy(mi,xi,zi):
    sum = 0
    for i in range(len(xi)):
        sum += mi[i]*((xi[i])**2+(zi[i])**2)
    return sum

def Izz(mi,xi,yi):
    sum = 0
    for i in range(len(xi)):
        sum += mi[i]*((xi[i])**2+(yi[i])**2)
    return sum

def Ixy(mi,xi,yi):
    sum = 0
    for i in range(len(xi)):
        sum += mi[i]*xi[i]*yi[i]
    return -sum

def Iyz(mi,yi,zi):
    sum = 0
    for i in range(len(yi)):
        sum += mi[i]*yi[i]*zi[i]
    return -sum

def Ixz(mi,xi,zi):
    sum = 0
    for i in range(len(xi)):
        sum += mi[i]*xi[i]*zi[i]
    return -sum


I_NH3 = np.zeros([3,3])
I_CH4 = np.zeros([3,3])
I_CH3Cl = np.zeros([3,3])
I_O3 = np.zeros([3,3])


#NH3
mi = []
xi = []
yi = []
zi = []
for i in range(0,4,1):

    atomo = total_data[i,:]
    
    mi.append(atomo[0])
    xi.append(atomo[1])
    yi.append(atomo[2])
    zi.append(atomo[3])  

I_NH3[0,0] = Ixx(mi,yi,zi)