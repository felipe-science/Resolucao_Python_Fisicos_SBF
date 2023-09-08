import numpy as np

total_data = np.loadtxt("dados_moleculas.dat")

def R_cm(mi,xi,yi,zi):

    xcm = 0.0
    ycm = 0.0
    zcm = 0.0

    M = sum(mi)
    for i in range(len(xi)):
        xcm = xcm + mi[i]*xi[i]
        ycm = ycm + mi[i]*yi[i]
        zcm = zcm + mi[i]*zi[i]

    xcm = xcm/M
    ycm = ycm/M
    zcm = zcm/M

    return xcm, ycm, zcm


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





print(mi)
la = R_cm(mi,xi,yi,zi)
print(la)