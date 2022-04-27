import numpy as np
from matplotlib import pyplot as plt

# =========== DIFFERENTES METHODES DE RESOLUTION ===========

def euler(f,y0,t):
    Y = np.array([y0]*len(t))
    # print(Y)
    for k in range(1, len(t)):
        Y[k]=(f(t[k-1],Y[k-1]) * (t[k]-t[k-1])) + Y[k-1]
        # print((f(t[k-1],Y[k-1]) * (t[k]-t[k-1])) + Y[k-1])
        # print(Y[k])
    return Y 

def rk2(f, y0, t):
    Y = np.array([y0]*len(t))
    # print(Y)
    for k in range(1, len(t)):
        y_euler = (f(t[k-1],Y[k-1]) * (t[k]-t[k-1])) + Y[k-1]
        a = f((t[k]+t[k-1])/2, (y_euler+Y[k-1])/2)
        Y[k]=a * (t[k]-t[k-1])+Y[k-1]
        # print(Y[k])
    return Y 

def rk4(f, y0, t):
    Y = np.array([y0]*len(t))
    for k in range(0, len(t)-1):
        h = t[k+1]-t[k]
        k1 = f(t[k], Y[k])
        k2 = f(t[k]+h/2,Y[k]+(h*k1)/2)
        k3 = f(t[k]+h/2,Y[k]+(h*k2)/2)
        k4 = f(t[k]+h,Y[k]+h*k3)
        Y[k+1] = Y[k] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    return Y 


# =====================================================


if __name__ == "__main__":
    def compare(solution_exacte,phi_,a,b,y0):
        for N in [10**k for k in range(2,6)]:
            interval = np.linspace(a,b, N)
            Y = solution_exacte(interval)
            Y_euler = euler(phi_, y0, interval)
            Y_rk2 = rk2(phi_, y0, interval)
            Y_rk4 = rk4(phi_, y0, interval)


            # print(Y_tilde)

            plt.plot(interval, Y, "r-")
            plt.plot(interval, Y_euler, "b-")
            plt.plot(interval, Y_rk2, "g-")
            plt.plot(interval, Y_rk4, "y-")

            plt.title(f"Approximation de l'exp avec {N} points")
            plt.show()

    def compare_bis(solution_exacte,phi_,a,b,y0):
        for N in [10**k for k in range(2,6)]:
            interval = np.linspace(a,b, N)
            # print(interval)
            # print(solution_exacte(interval))
            # Y = [y[0] for y in solution_exacte(interval)]
            Y_euler = [y[0] for y in euler(phi_, y0, interval)]
            Y_rk2 = [y[0] for y in rk2(phi_, y0, interval)]
            Y_rk4 = [y[0] for y in rk4(phi_, y0, interval)]
            

            # print(Y_tilde)

            # plt.plot(interval, Y, "r-")
            plt.plot(interval, Y_euler, "b-")
            plt.plot(interval, Y_rk2, "g-")
            plt.plot(interval, Y_rk4, "y-")

            plt.title(f"Approximation de l'exp avec {N} points")
            plt.show()


    def phi_exp(t,y):
        return y

    def phi_q5(t,y):
        return (np.cos(t)-y)/(t+1)

    def sol_q5(t):
        return (np.sin(t)-0.5)/(t+1)

    def phi_q6(t,y):
        return 3*(y/t)-5/(t**3)

    def sol_q6_lambda_0(t):
        return 1/(t**2)

    def sol_q6(l):
        return lambda t: l*t**3+t**(-2)

    def phi_q10(t,Y):
        return np.array([Y[1],-np.sin(Y[0])])


    # compare(np.exp, phi_exp, 0,10, 1.0)
    # compare(sol_q5, phi_q5, 0, 10, -0.5)
    # compare(sol_q6_lambda_0, phi_q6, 1.0,10,1.0)

    # Pendule
    # print("hello")
    print(np.array([1.0,1.0])[0])
    compare_bis(lambda x: np.array([1.0,1.0]), phi_q10, 0.0, 100.0, np.array([3.1,0.0]))



