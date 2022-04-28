from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import integrate as si
import numpy as np


class Astre:
    def __init__(self, pos, m, r, v=np.zeros(3), name=None):
        """.git/
        @param pos: position np array (1,3)
        @param m: la masse de l'astre
        @param r: le rayon de l'astre
        @param v: le vecteur vitesse np array (1,3)
        """
        self.position = pos
        self.mass = m 
        self.radius = r 
        self.speed = v 
        self.name = name

        self.historique_positions = [pos]

    # def modifier_position(self, new_position):
    #     self.historique_positions.append(self.position)
    #     self.position = new_position

    def __str__(self):
        return f"""===============
Nom:\t{self.name}
Position\t{self.position}
Vitesse\t{self.speed}
Masse:\t{self.mass}
Rayon:\t{self.radius}\n
"""
    
def norm(v):
    """
    Norme euclidéene
    """
    return np.sqrt(np.dot(v,v))

def simulator(astres, delta_t=24*3600, nb_points=1_000_000, time_factor=100):
    G= 6.67e-11
    t = np.linspace(0, delta_t, nb_points)

    fig = plt.figure()

    ax = fig.gca(projection='3d')
    
    y0 = np.hstack([np.hstack((a.position, a.speed)) for a in astres])
    # print(y0)

    def fGrav(Y,t):
        # On recopie les valeurs dans la liste des astres
        dY = Y.copy()
        for i_astre, astre in enumerate(astres):
            astre.position = np.array([Y[6*i_astre+k] for k in range(3)])
            # print(astre.position)
            astre.speed = np.array([Y[6*i_astre+3+k] for k in range(3)])

        for i_astre, astre in enumerate(astres):
            #* 1. On calcule l'accélération
            a = np.zeros(3)
            for i_satellite, satellite in enumerate(astres):
                if i_astre != i_satellite: # S'ils sont bien différents
                    # 2ème loi de Newton, on ajoute la force exercé par l'astre b divisé par la masse de a
                    vAstreSatellite = satellite.position-astre.position 
                    # print(vAstreSatellite)
                    a += + (G * satellite.mass / (norm(vAstreSatellite)**3))*vAstreSatellite
            
            for k in range(3):
                dY[6*i_astre+k]=astre.speed[k]
                dY[6*i_astre+3+k]=a[k]

        return dY



    Y = si.odeint(fGrav, y0, t)

    for i_astre, astre in enumerate(astres):

        # print("\n".join(str(p) for p in astre.historique_positions))
        
        xs = [y[6*i_astre] for y in Y]
        ys = [y[6*i_astre+1] for y in Y]
        zs = [y[6*i_astre+2] for y in Y]
        # print(xs)
        plt.plot(xs, ys, zs, lw=1, label=astre.name)

    # plt.axis(False)
    # plt.grid(False)
    plt.legend()
    plt.show()


if __name__ == "__main__":

    Terre = Astre(np.array((0,0,0)),m=5.97e24,r=6.4e6,v=np.array((0,0,0)), name="Terre")
    dTL=3.8e8
    periodeLune = 28*24*3600
    vLune = (-2*np.pi*dTL)/periodeLune
    Lune =  Astre(np.array((dTL,0,0)),m=7.3e22,r=1.7e6, v=np.array((0,vLune,0)), name="Lune")
    Darklune =  Astre(np.array((-dTL/2,0,0)),m=7.3e22,r=1.7e6, v=np.array((0,0,vLune)), name="DarkLune")

    simulator([Terre, Lune, Darklune], delta_t=5*periodeLune)