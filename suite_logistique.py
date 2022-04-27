from PIL import Image, ImageDraw
import numpy as np 

def suite_n(u0, f, n):
    if n<=0: # Pour gérére les erreurs n<0 on les met ici
        return u0
    # Sinon
    return f(suite_n(u0, f, n-1))


def draw_chaos(longueur=4096, hauteur=2048, name_output="chaos.png", nb_points=500):
    black = (0,0,0)
    image = Image.new("RGB", (longueur, hauteur), "white")
    # image.putpixel((500,200), black)

    draw = ImageDraw.Draw(image)

    R = np.linspace(2.9, 4, longueur)
    for x, r in enumerate(R):
        f = lambda x : r * x * (1-x)
        terme = suite_n(0.2, f, 500)
        for _ in range(nb_points):
            y = int(terme*hauteur)

            image.putpixel((x,y), black)

            terme = f(terme)
        


    # image.show()
    image.save(name_output, "PNG")

if __name__ == "__main__":
    size_x, size_y = 4096, 2048
    draw_chaos(size_x, size_y, f"chaos_{size_x}_{size_y}.png")