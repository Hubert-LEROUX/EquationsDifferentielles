# https://fr.wikipedia.org/wiki/Attracteur_de_R%C3%B6ssler

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import integrate as si
import numpy as np


def fLor(Y,t, sigma=14, rho=30, beta=3):
    return (sigma*(Y[1]-Y[0]), 
            rho*Y[0]-Y[1]-Y[0]*Y[2], 
            Y[0]*Y[1]-beta*Y[2])

def fRos(Y,t, a=0.2, b=0.2, c=5.7):
    return (-Y[1]-Y[2], 
            Y[0]+a*Y[1],
            b+Y[2]*(Y[0]-c))

def fUeda(Y,t, k=0.05, B=7.5):
    return (Y[1],
            -Y[0]**3-k*Y[1]+B*np.sin(Y[2]),
            1)

def fChaoticFlow(Y, t, A=2.017):
    return (Y[1],
            Y[2],
            -A*Y[2]+Y[1]**2-Y[0])

def fPiecewiseFlow(Y, t, A=0.6):
    return (Y[1],
            Y[2],
            -A*Y[2]+Y[1]-abs(Y[0])+1)


def attracteur(ci, f, args=(), name="Lorenz", delta_t=100, nb_points=10_000, lw=0.1):
    t = np.linspace(0, delta_t, nb_points)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # ax.set_facecolor('black')

    for y0 in ci:
        Y = si.odeint(f, y0, t, args=args)
        # plt.plot(Y[: , 0],  Y[: , 1], Y[: , 2], label=str(y0), lw=lw, c="gray")
        plt.plot(Y[: , 0],  Y[: , 1], Y[: , 2], label=str(y0), lw=lw)
        
    # ax.legend()


    # plt.title(f"Attracteur de {name}")
    
    # fontsize_labels = 5
    # ax.set_xlabel("Intensité du mouvement de convection", size=fontsize_labels)
    # ax.set_ylabel("Différence de température entre les courants ascendants et descendants", size=fontsize_labels)
    # ax.set_zlabel("Ecart du profil de température vertical par rapport à un profil linéaire", size=fontsize_labels)

    plt.grid(False)
    plt.axis(False)
    plt.show()

if __name__ == "__main__":
    plt.rcParams['figure.dpi'] = 800
    
    #! Attracteur de Lorenz
    attracteur([(10,0,0)], fLor, (14,30,3), nb_points=1_000_000, lw=0.02)
    
    
    #! Attracteur de Rössler
    # attracteur([(0.5,0.5,0.5)], fRos, args=(0.1,0.1,18),  name="Rössler", delta_t=1_000, nb_points=100_000, lw=0.05)
    
    
    #! Attracteur de Ueada
    # attracteur([(0.5,0.5,0.5)], fUeda,  name="Ueda", delta_t=10_000, nb_points=1_000_000, lw=0.1)
    
    
    #! "Simplest quadratic dissipative chaotic flow"
    # attracteur([(0.5,0.4,0.1), (0.5,0.4001,0.1)], fChaoticFlow,  name="Chaotic Flow", delta_t=1_000, nb_points=100_000, lw=0.1)
    # attracteur([(0.5,0.4,0.1)], fChaoticFlow,  name="Chaotic Flow", delta_t=1_000, nb_points=100_000, lw=0.1)


    #! "Simplest piecewise linear dissipative chaotic flow"
    # for a in range(10):
    #     for b in range(10):
    #         attracteur([(a/10,b/10,0.5)], fPiecewiseFlow,  name="Piecewise Flow", delta_t=1_000, nb_points=100_000, lw=0.1)
    #         print()
    #         print()
    #         print()
    #         print(a,b)
    #         print()
    #         print()
    #         print()

    # attracteur([(-5/10,2/10,3)], fPiecewiseFlow,  name="Piecewise Flow", delta_t=1_000, nb_points=1000_000, lw=0.1)
    


