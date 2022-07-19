from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import integrate as si
import numpy as np
import os
# import random as rd

def fCliffordAttractor(x,y, a=-1.4, b=1.6, c=1.0, d=0.7, *o):
    """.git/
    https://vedransekara.github.io/2016/11/14/strange_attractors.html
    https://examples.pyviz.org/attractors/attractors.html
    """
    return (np.sin(a*y)+c*np.cos(a*x),
            np.sin(b*x)+d*np.cos(b*y))

def fDeJong(x, y, a, b, c, d):
    return (np.sin(a * y) - np.cos(b * x),
           np.sin(c * x) - np.cos(d * y))

def fSvensson(x, y, a, b, c, d):
    return d * np.sin(a * x) - np.sin(b * y), \
           c * np.cos(a * x) + np.cos(b * y)

def fHopalong1(x, y, a, b, c, *o):
    # https://www.maplesoft.com/support/help/maple/view.aspx?path=MathApps/HopalongAttractor
    return y - np.sqrt(np.abs(b * x - c)) * np.sign(x), \
           a - x


def fHopalong2(x, y, a, b, c, *o):
    return y - 1.0 - np.sqrt(np.abs(b * x - 1.0 - c)) * np.sign(x - 1.0), \
           a - x - 1.0

def G(x, mu):
    return mu * x + 2 * (1 - mu) * x**2 / (1.0 + x**2)


def fGumowski_Mira(x, y, a, b, mu, *o):
    xn = y + a*(1 - b*y**2)*y  +  G(x, mu)
    yn = -x + G(xn, mu)
    return xn, yn

def fSymmetricIcon(x, y, a, b, g, om, l, d, *o):
    zzbar = x*x + y*y
    p = a*zzbar + l
    zreal, zimag = x, y
    
    for i in range(1, d-1):
        za, zb = zreal * x - zimag * y, zimag * x + zreal * y
        zreal, zimag = za, zb
    
    zn = x*zreal - y*zimag
    p += b*zn
    
    return p*x + g*zreal - om*y, \
           p*y - g*zimag + om*x



def attracteur(cis, f, args=(), name_output="Clifford", nb_iterations=1_000_000, s=0.001, c="red", facecolor="white", dpi=200, save=False):
    fig = plt.figure(num=None, figsize=(5, 5), dpi=dpi, facecolor=facecolor)
    ax = fig.add_subplot(111)

    for ci in cis:
        x,y = ci 
        xx = np.empty(nb_iterations+1)
        yy = np.empty(nb_iterations+1)

        xx[0]=x
        yy[0]=y

        for i in range(1,nb_iterations+1):
            x,y = f(x,y,*args)
            xx[i] = x
            yy[i] = y


        if len(cis)==1:
            ax.scatter(xx, yy, s=s, c=c)
        else:
            ax.scatter(xx, yy, s=s)
        # plt.plot(xx, yy,'.', markersize=s)
        
    # ax.legend()


    # plt.title(f"Attracteur de {name}")
    
    # fontsize_labels = 5
    # ax.set_xlabel("Intensité du mouvement de convection", size=fontsize_labels)
    # ax.set_ylabel("Différence de température entre les courants ascendants et descendants", size=fontsize_labels)
    # ax.set_zlabel("Ecart du profil de température vertical par rapport à un profil linéaire", size=fontsize_labels)

    plt.grid(False)
    plt.axis(False)
    plt.axis('equal')
    if save == True:
        plt.savefig(os.path.join("results", name_output), dpi=dpi)
    plt.show()


def random_attractors(f=fCliffordAttractor, name="Attractor", generator_args=lambda : tuple(np.round(np.random.rand(4)*4-2,3)), serie=1):
    s=0.0005
    nb_iterations = 10_000
    dpi = 80
    facecolor = "white"
    # precision = 3

    # fig, ax = plt.subplots(5,5, figsize=(12,12))
    fig, ax = plt.subplots(5,5,dpi=dpi, figsize=(12,12))
    
    for i in range(5):
        for j in range(5):

            args = generator_args()
            r,g,b = (np.random.random() for _ in range(3))

            # if i==j==0:
            #     args = (1.8, 0.0, 1.0, 0.1, -1.93, 5)

            print(*args)

            x,y = (0.5,0.5)
            xx = np.empty(nb_iterations+1)
            yy = np.empty(nb_iterations+1)
            xx[0]=x
            yy[0]=y
            for k in range(1,nb_iterations+1):
                x,y = f(x,y,*args)
                xx[k] = x
                yy[k] = y

            ax[i,j].scatter(xx, yy, s=s, color=(r,g,b), marker=".")
            # ax[i,j].plot(xx, yy, ".",  markersize=s, color=(r,g,b))

            ax[i,j].set_title(f"{args}", size=6)
            ax[i,j].axis("off")
            ax[i,j].axis("equal")
        
    # fig.tight_layout()
    fig.suptitle(name, fontsize=15)
    # plt.savefig(f"planches/{name}/{name}_{serie:03}")
    plt.savefig(f"planches/{name}/{name}_{serie:03}", dpi=dpi)
    # plt.show()
    plt.clf()

if __name__ == "__main__":

    # print(f"{2:03}")
    for k in range(0,100):
        print()
        print(k)
        print()
        # random_attractors(fHopalong2, name="hopalong2",serie=k)
        random_attractors(fGumowski_Mira, generator_args=lambda : tuple(np.round(np.random.rand(3)*4-2,3)),name="gumowski_mira",serie=k)




    # attracteur([(0.1,0.1)], fSymmetricIcon, args=(1.8, -1.2, 1.0, 0.1, -1.93, 5), nb_iterations=100_000,
    #             name_output=f"clifford_07", c="red", facecolor="white", s=0.01, dpi=80)

    # random_attractors(fSymmetricIcon, generator_args=lambda : tuple(np.round(np.random.rand(4)*4-2,2))+(np.random.random()+1.5, np.random.randint(1,5)), name="SymmetricIcon")
    
    