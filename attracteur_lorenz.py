from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import integrate as si
import numpy as np

def fLor(Y,t, sigma=14, rho=30, b=3):
        return (sigma*(Y[1]-Y[0]), 
                rho*Y[0]-Y[1]-Y[0]*Y[2], 
                Y[0]*Y[1]-b*Y[2])

def attracteur(ci, sigma, rho, b, delta_t=100, nb_points=100_000):
    t = np.linspace(0, delta_t, nb_points)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # ax.set_facecolor('black')

    for y0 in ci:
        Y = si.odeint(fLor, y0, t, args=(sigma, rho, b))
        plt.plot(Y[: , 0],  Y[: , 1], Y[: , 2], label=str(y0), c="gray", lw=0.1)

        
    # ax.legend()


    # plt.title("Attracteur de Lorenz")
    
    # fontsize_labels = 5
    # ax.set_xlabel("Intensité du mouvement de convection", size=fontsize_labels)
    # ax.set_ylabel("Différence de température entre les courants ascendants et descendants", size=fontsize_labels)
    # ax.set_zlabel("Ecart du profil de température vertical par rapport à un profil linéaire", size=fontsize_labels)
    plt.axis(False)
    plt.grid(False)
    plt.show()


if __name__ == "__main__":
    attracteur([(10,0, 0)], fLor)
    # attracteur([(10,0, 0), (11, 0, 0), (12, 0, 0)], sigma=14, rho=30, b=3)