from PIL import Image, ImageDraw
import numpy as np 
from matplotlib import pyplot as plt 

def henon(ci, a=1.4, b=0.3, N=100_000):

    def fHenon(x,y):
        return (1+y-a*x*x, b*x)

    def suite_henon(x0, y0, n):
        suite = [(x0,y0)]
        for _ in range(n):
            suite.append(fHenon(*suite[-1]))
        return suite

    for (x0, y0) in ci:
        suite = suite_henon(x0, y0, N)
        xs = [t[0] for t in suite]
        ys = [t[1] for t in suite]
        # plt.plot(xs,ys,"o-",label=str((x0,y0)), lw=0.1, markersize=0.2)
        plt.scatter(xs,ys,label=str((x0,y0)), s=0.2)

    plt.grid(True)
    plt.title(r"$x_{n+1} = 1+y_n-ax_n^2$ and $y_{n+1} =  bx_n$")
    plt.plot()
    plt.show()



def suite_n(u0, f, n):
    if n<=0: # Pour gérére les erreurs n<0 on les met ici
        return u0
    # Sinon
    return f(suite_n(u0, f, n-1))


def draw_x(name_output="chaos.png", longueur=4096, hauteur=4096, nb_points=500):
    black = (0,0,0)
    image = Image.new("RGB", (longueur, hauteur), "white")
    # image.putpixel((500,200), black)

    
    draw = ImageDraw.Draw(image)

    R = np.linspace(1, 1.42, longueur)
    for x, a in enumerate(R):

        def fHenon(u):
            x,y = u
            b=0.3
            return (1+y-a*x*x, b*x)

        terme = suite_n((0.5,0.5), fHenon, 500)
        for _ in range(nb_points):
            y = int((terme[0]+1.5)*(hauteur/3))
            image.putpixel((x,y), black)
            terme = fHenon(terme)
    # image.show()
    image.save(name_output, "PNG")

if __name__ == "__main__":
    # henon([(1,1), (0.5,0.5)])
    henon([(1,1)])
    # draw_x("henon_x.png", 4*4096,4*4096)