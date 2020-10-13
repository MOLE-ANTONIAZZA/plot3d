from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations


# domaine
x = np.arange(0,14,0.1)
y = np.arange(0,3.0,0.1)
X,Y = np.meshgrid(x,y)

# declaration figure
fig = plt.figure()
# declaration de la figure en 3d avec option projection dans la fonction add_subplot
# ax = fig.add_subplot(111, projection='3d')
ax = plt.axes(projection='3d')

# declaration de la geometrie
g_x = [0, 12]
g_y = [0, 2.2]
# g_z = [0, 2.4]
for s, e in combinations(np.array(list(product(g_x,g_y))), 2):
    ax.plot3D(*zip(s,e), color="k")

# declaration du foyer
f_x = [5.3, 5.8]
f_y = [0.8, 1.3]
f_z = [0.0, 0.5]

for s, e in combinations(np.array(list(product(f_x,f_y))), 2):
    ax.plot3D(*zip(s,e), color="k")

# position dans le plan des donnees
xpos = [0,1.7,3.1,3.1,4.1,4.1,6.4,6.4,8.7,8.7] #dim=10
ypos = [0,1.6,2.0,0.2,0.2,2.0,0.2,2.0,0.2,2.0] #dim=10

# generation de donnees pour le troisieme axe (a remplacer par la temperature, ou l'erreur absolue sur les températures
zpos = np.zeros(10)
dz = [np.random.random(10) for i in range(5)]
_zpos = zpos
# couleurs identiques aux figures de Temperatures(temps)
colors = ['C4', 'C3', 'C2', 'C1', 'C0']

# tracer des donnees
for i in range(5):
    ax.bar3d(xpos, ypos, _zpos, 0.1, 0.1, dz[i], color=colors[i])
    _zpos += dz[i]

# declaration des entetes des axes
ax.set_xlabel('Position x')
ax.set_ylabel('Position y')
ax.set_zlabel('Erreur absolue')
ax.set_title('Erreur sur les températures ')

plt.show()
