import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

gas = ct.Solution('gri30.xml')

npoints = 50

T0 = 300.0
P0 = 101325.0

# T(Phi)

phi = np.linspace(0.3, 3.5, npoints)
tad0 = np.zeros(npoints)

for i in range(npoints):
    gas.set_equivalence_ratio(phi[i], 'CH4:1.0', 'O2:1.0, N2:3.76')
    gas.TP = T0, P0
    gas.equilibrate('HP')
    tad0[i] = gas.T
    # print('At phi = {0:12.4g}, Tad = {1:12.4g}'.format(phi[i], tad[i]))
    
print('T(Phi)')
fig, ax = plt.subplots()
ax.plot(phi, tad0)
ax.set(xlabel='Equivalence ratio [-]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for Phi1

P = np.linspace(0.1*ct.one_atm, ct.one_atm*5, npoints)
phi1 = 0.5
tad11 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T0, P[i]
    gas.set_equivalence_ratio(phi1, 'CH4:1.0', 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    tad11[i] = gas.T
    # print('At P = {0:12.4g}, Tad = {1:12.4g}'.format(P[i], tad[i]))

print('T(p) for Phi1')
fig, ax = plt.subplots()
ax.plot(P/100000, tad11)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for Phi2

phi2 = 1
tad12 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T0, P[i]
    gas.set_equivalence_ratio(phi2, 'CH4:1.0', 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    tad12[i] = gas.T
    # print('At P = {0:12.4g}, Tad = {1:12.4g}'.format(P[i], tad[i]))

print('T(p) for Phi2')
fig, ax = plt.subplots()
ax.plot(P/100000, tad12)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for Phi3

phi3 = 2
tad13 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T0, P[i]
    gas.set_equivalence_ratio(phi3, 'CH4:1.0', 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    tad13[i] = gas.T
    # print('At P = {0:12.4g}, Tad = {1:12.4g}'.format(P[i], tad[i]))

print('T(p) for Phi3')
fig, ax = plt.subplots()
ax.plot(P/100000, tad13)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for Phi4

phi4= 3
tad14 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T0, P[i]
    gas.set_equivalence_ratio(phi4, 'CH4:1.0', 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    tad14[i] = gas.T
    # print('At P = {0:12.4g}, Tad = {1:12.4g}'.format(P[i], tad[i]))

print('T(p) for Phi4')
fig, ax = plt.subplots()
ax.plot(P/100000, tad14)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

#T(p) for all Phi values

fig, ax = plt.subplots()
plt.plot(P/100000, tad11, label='$ \Phi1 $')
plt.plot(P/100000, tad12, label='$ \Phi2 $')
plt.plot(P/100000, tad13, label='$ \Phi3 $')
plt.plot(P/100000, tad14, label='$ \Phi4 $')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for Phi1

T = np.linspace(273, 2000, npoints)
tad21 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T[i], P0
    gas.set_equivalence_ratio(phi1, 'CH4:1.0', 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    tad21[i] = gas.T
    # print('At T = {0:12.4g}, Tad = {1:12.4g}'.format(T[i], tad[i]))

print('T(T) for Phi1')
fig, ax = plt.subplots()
ax.plot(T, tad21)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for Phi2

T = np.linspace(273, 2000, npoints)
tad22 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T[i], P0
    gas.set_equivalence_ratio(phi2, 'CH4:1.0', 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    tad22[i] = gas.T
    # print('At T = {0:12.4g}, Tad = {1:12.4g}'.format(T[i], tad[i]))

print('T(T) for Phi2')
fig, ax = plt.subplots()
ax.plot(T, tad22)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for Phi3

T = np.linspace(273, 2000, npoints)
tad23 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T[i], P0
    gas.set_equivalence_ratio(phi3, 'CH4:1.0', 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    tad23[i] = gas.T
    # print('At T = {0:12.4g}, Tad = {1:12.4g}'.format(T[i], tad[i]))

print('T(T) for Phi3')
fig, ax = plt.subplots()
ax.plot(T, tad23)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for Phi4

T = np.linspace(273, 2000, npoints)
tad24 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T[i], P0
    gas.set_equivalence_ratio(phi4, 'CH4:1.0', 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    tad24[i] = gas.T
    # print('At T = {0:12.4g}, Tad = {1:12.4g}'.format(T[i], tad[i]))

print('T(T) for Phi4')
fig, ax = plt.subplots()
ax.plot(T, tad24)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

#T(T) for all Phi values

fig, ax = plt.subplots()
plt.plot(T, tad21, label='$ \Phi1 $')
plt.plot(T, tad22, label='$ \Phi2 $')
plt.plot(T, tad23, label='$ \Phi3 $')
plt.plot(T, tad24, label='$ \Phi4 $')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()
