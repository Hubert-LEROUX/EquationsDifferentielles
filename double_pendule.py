from tools import rk4 
import numpy as np
from scipy import integrate as si
from matplotlib import pyplot as plt

def double_pendule(ci, l1, l2, m1, m2, g=9.81, delta_t=5, nb_points=1_000):
    """.git/
    Résout l'équation du pendule double
    """
    t = np.linspace(0,delta_t, nb_points) # Les points du temps
    
    def rhs(y,t):
        """
        Renvoie l'equa diff sous forme de tableau numpy:
        Y' = rhs(Y,t)
        """
        theta1 = y[0]
        theta2 = y[2]

        dtheta1 = y[1]
        dtheta2 = y[3]

        c, s = np.cos(theta1-theta2), np.sin(theta1-theta2)

        ddtheta1 = (m2*g*np.sin(theta2)*c - m2*s*(l1*dtheta1**2*c + l2*dtheta2**2) -
             (m1+m2)*g*np.sin(theta1)) / l1 / (m1 + m2*s**2)
        ddtheta2 =  ((m1+m2)*(l1*dtheta1**2*s - g*np.sin(theta2) + g*np.sin(theta1)*c) + 
             m2*l2*dtheta2**2*s*c) / l2 / (m1 + m2*s**2)

        return (dtheta1, 
                ddtheta1,
                dtheta2,
                ddtheta2)

    for y0 in ci:
        y = si.odeint(rhs, y0, t)

        # Il faut retrouver x1,y1,x2,y2
        x1 = l1*np.sin(y[:,0])
        y1 = - l1*np.cos(y[:,0])

        x2 = x1 + l2*np.sin(y[:,2])
        y2 = y1 - l2*np.cos(y[:,2])

        # plt.plot(x1, y1, label = f"Masse1-{y0}")
        plt.plot(x2, y2, label = f"Masse2-{y0}")
    
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    plt.title("Pendule double")

    plt.show()



if __name__ == "__main__":
    double_pendule([[1.5, 0.0, 0.0,0.0], [1.5, 0.0, 0.01,0.0], [1.5, 0.0, 0.02,0.0]], l1=1, l2=0.5, m1=2, m2=1)


