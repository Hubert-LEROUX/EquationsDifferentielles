from tools import rk4 
import numpy as np
from scipy import integrate as si
from matplotlib import pyplot as plt

def pendule(l, alpha=0, m=1,theta_0=0.0, dtheta_0=1.0,g=9.81, delta_t=20, nb_points=1_000):
    """.git/
    Résout l'équation du pendule 
    @param l : longueur du pendule (en m)
    @param alpha: coefficient de frottements (frottements laminaires)
    @param m: masse (en kg)
    @param g : intentsité du champ de pesanteur (en m.s^(-2))
    @theta_0 : Angle initial selon la verticale (en radians)
    @dtheta_0 : Vitesse angulaire initiale (en radians par seconde)
    @delta_t : Intervalle de temps (en s)
    """
    equation = r"$\ddot{\theta}+\frac{g}{l}\sin(\theta)=0$"
    t = np.linspace(0,delta_t, nb_points) # Les points du temps
    
    def rhs(y,t):
        """
        Renvoie l'equa diff sous forme de tableau numpy:
        Y' = rhs(Y,t)
        """
        return (y[1], -((g*np.sin(y[0]))/l + (alpha/(l*m))*y[1]))

    y = si.odeint(rhs, (theta_0, dtheta_0), t)
    # Tableau numpy contenant les valeurs -> theta et thetap_point en fonction du temps

    plt.plot(t, y[:, 0], label = r"$\theta$")
    plt.plot(t, y[:, 1], label = r"$\dot{\theta}$")
    plt.grid(True)
    plt.legend()
    plt.title(equation)

    plt.xlabel("Temps (en s)")
    plt.ylabel("Radians ou Radian/s")
    plt.show()


if __name__ == "__main__":
    pendule(1.0, 0.1, 1,3.13, 0.0)
