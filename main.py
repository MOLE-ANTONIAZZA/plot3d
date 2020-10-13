import matplotlib.pyplot as plt
import numpy as np

# domaine
x = np.arange(0,12,0.1)
y = np.arange(0,2.4,0.1)
X,Y = np.meshgrid(x,y)

# declaration figure
fig = plt.figure()
# declaration de la figure en 3d avec option projection dans la fonction add_subplot
ax = fig.add_subplot(111, projection='3d')

# position dans le plan des donnees
xpos = [0,1.7,3.1,3.1,4.1,4.1,6.4,6.4,8.7,8.7] #dim=10
ypos = [0,1.6,2.2,0.2,0.2,2.2,0.2,2.2,0.2,2.2] #dim=10

# generation de donnees pour le troisieme axe (à remplacer par la température, ou l'erreur absolue sur les températures
zpos = np.zeros(10)
dz = [np.random.random(10) for i in range(5)]
_zpos = zpos
# couleurs identiques aux figures de Temperatures(temps)
colors = ['m', 'r', 'g', 'y', 'b']

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
