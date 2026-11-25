import pandas as pd
import numpy as np
data = pd.read_csv('indata.csv', sep=';', decimal = ',')
rho = 1.225 #[kg/m^3]
tid = np.array(data['Tid'].values)
vind = np.array(data['Wind'].values)
Pturbin = np.array([])
Cp = 0.45
Cpteoretisk = 16/27
Ct = 0.8 #Trust koefficient
k = 1 
h = 1 #Höjd torn [m]
Rtorn = 1 #[m]
dd = 2*Rtorn #Delningsdiamater [m]
nb = 1 #Antal skruvar [st]
Td = 1 #Turbindiameter [m]
Pmark = 1 #Max effekt [MW]
tf = 1 #Flänstjocklek [m]
bf = 1 #Flänsbredd [m]
Mt = 1 #Tornmassa [kg]
Mn = 1 #Nacellmassa [kg]
Mtb = 1 #Bladmassa [g]
tfl = 1 #Väggtjocklek vid fläns [m]
g = 9.82 #[m/s^2]
Di = 2*Rtorn + bf #Innerdiameter [m]
Do = Di + 2*tfl #Ytterdiameter [m]
As = np.pi*(Do**2 - Di**2)/4 #Tvärsnittsarea [m^2]
Ws = np.pi*(Do**4 - Di**4)/(32*Do) #Böjmotstånd [m^3]
Mtot = (Mt + Mn + 3*Mtb) #Kraftverketstotala massa [m]
N = Mtot*g #Normalspänning [Pa]


A = (np.pi*Td**2)/4
Pturbin = 0.5*rho*A*Cp*vind**3

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
sig_n = N/As
sig_tryck = sig_b + sig_n #"bakom tornet"
sig_drag = sig_b - sig_n  #"framför tornet"

Aseg = As/nb
Fn_tryck = sig_tryck * Aseg
Fn_drag = sig_drag * Aseg
Fn_tryck_max = max(Fn_tryck)
Fn_drag_max = max(Fn_drag)
print(Fn_tryck_max, Fn_drag_max)