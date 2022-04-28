from matplotlib import pyplot as plt 
import numpy as np
import os

# Avec l'aide de https://gist.github.com/t-makaro/59a75f1694da5bd05feab2d096c174c7

def chirikov(p, q, K):
    """
    Chirikov function
    """
    return ((p+K*np.sin(q)  )  % (2*np.pi), 
            (q+K*np.sin(q)+p)  % (2*np.pi))

def frame(K, nb_iterations=1_000, r=0.5):
    """.git/
    Réalise une frame
    @param K: le paramètre de la fonction chirikov
    @param nb_iterations
    @param r: resolution -> les graines sont espacées de 1
    """
    p0 = np.arange(0, 2*np.pi, r)
    q0 = np.arange(0, 2*np.pi, r)

    # On crée la grille
    P,Q = np.meshgrid(p0, q0)
    # print(P)
    # print(Q)

    # On reshape pour les mettre sous forme d'une liste
    nb_points = len(p0)*len(q0)
    P = P.reshape(nb_points) #? Attention la méthode ne s'effectue pas en place
    Q = Q.reshape(nb_points)

    # On associe à chaque point de départ sa couleur RGB
    colors = np.array([P/max(P), Q/max(Q), (P+Q)/max(P+Q)]).T

    #* On va maintenant itérer
    all_points_P = [P]
    all_points_Q = [Q]
    for _ in range(nb_iterations):
        P,Q = chirikov(P, Q, K=K)
        all_points_P.append(P)
        all_points_Q.append(Q)
    
    return (np.hstack(all_points_P), np.hstack(all_points_Q), np.vstack([colors]*(nb_iterations+1)))


def plot_chirikov(K, ouput_dir="frames/chirikov", nb_iterations=100, r=0.5):
    P,Q,colors = frame(K, nb_iterations=nb_iterations, r=r)

    plt.scatter(Q,P,s=0.1,c=colors)
    plt.title(f"Chirikov Standard Map K={K}")
    plt.axis('equal')

    # plt.show()
    name_file = f"standard_map_K_{K:2f}".replace('.', '_')
    print(name_file)
    file_output = os.path.join(ouput_dir, name_file)
    plt.savefig(file_output)



if __name__ == "__main__":
    # frame(0.5)
    # plot_chirikov(K=)
    plt.rcParams['figure.dpi'] = 150
    for K in np.arange(0,3,0.05):
        Ks=round(K, 2)
        plot_chirikov(Ks)
        print(Ks)

