import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('indata.csv', sep=';', decimal = ',')
rho = 1.225 #[kg/m^3]
tid = data['Tid'].values
vind = data['Wind'].values
Pturbin = np.array([])
Cp = 0.45
Cpteoretisk = 16/27
Ct = 0.8 #Trust koefficient
k = 1 
h = 56.5 #Höjd torn [m]
Rtorn = 3.25 #[m]
dd = 2*Rtorn #Delningsdiamater [m]
nb = 100 #Antal skruvar [st]
Td = 199.38 #Turbindiameter [m]
Pmax = 10e6 #Max effekt [W]
tf = 175e-3 #Flänstjocklek [m]
bf = 300e-3 #Flänsbredd [m]
Mt = 230.2e3 #Tornmassa [kg]
Mn = 250e3 #Nacellmassa [kg]
Mtb = 48e3 #Bladmassa [kg]
tfl = 55.01e-3 #Väggtjocklek vid fläns [m]
g = 9.82 #[m/s^2]
Di = 2*Rtorn + bf #Innerdiameter [m]
Do = Di + 2*tfl #Ytterdiameter [m]
As = np.pi*(Do**2 - Di**2)/4 #Tvärsnittsarea [m^2]
Ws = np.pi*(Do**4 - Di**4)/(32*Do) #Böjmotstånd [m^3]
Mtot = (Mt + Mn + 3*Mtb) #Kraftverketstotala massa [m]
N = Mtot*g #Normalspänning [Pa]


A = (np.pi*Td**2)/4
Pturbin = 0.5*rho*A*Cpteoretisk*(vind**3)
Pmark = Pmax*(Cp/Cpteoretisk)
vmark = (Pmark/(0.5*rho*A*Cp))**(1/3) #Märkvind
Ftryck_mark = 0.5*rho*Ct*A*vmark**2 #Märktryck, beror på märkvind
Ftryck = np.array([])
for v in vind:  #Bestämmer tryck beroende på vind
    if v < vmark: # ändrade tecken 
        Ftryck = np.append(Ftryck, 0.5*rho*Ct*A*v**2)
    else:
        Ftryck = np.append(Ftryck, Ftryck_mark*(vmark/v)**k)
M = h*Ftryck

sig_b = M/Ws
print(max(sig_b))
sig_n = N/As
print((sig_n))

sig_tot_bak = sig_b + sig_n
sig_tot_fram = sig_b - sig_n
Aseg = As/nb
Fn_tryck = sig_tot_bak * Aseg
Fn_drag = sig_tot_fram * Aseg
Fn_tryck_max = max(Fn_tryck)
Fn_drag_max = max(Fn_drag)
print(Fn_tryck_max*10e-3, 'kN', Fn_drag_max*10e-3, 'kN')



def f_delta(skruv, hylsa, d0):
    Eskruv = skruv[0]
    Askruv = skruv[1]
    Lskruv = skruv[2]
    Ehylsa = hylsa[0]
    Ahylsa = hylsa[1]
    Lhylsa = hylsa[2]
    
    cs = (Eskruv*Askruv)/Lskruv
    ck = (Ehylsa*Ahylsa)/Lhylsa
    F = np.array(list((range(5000))))
    deltas = F/cs
    deltak = -1*(F/ck) + d0
    plt.plot(deltas, F)
    plt.plot(deltak, F)
    plt.show()
    return(cs, ck)
f_delta([210*10**9, 1, 1], [210*10**9, 1, 0.8], 0.2)

