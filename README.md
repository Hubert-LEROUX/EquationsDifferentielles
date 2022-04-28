# Equation différentielles


Ce projet contient quelques fameux problèmes de physiques ne pouvant se résoudre à la main comme le pendule simple. 
Il explore également les systèmes chaotiques comme le double pendule ou l'attracteur de Lorenz en passant par la suite logistique.
Ces projets sont souvent repris d'autres sources que je précise normalement au début des programmes.

## L'attracteur de Lorenz

<img src="results/attracteur_lorenz.png" 
        alt="Picture" 
        width="800" 
        height="600" 
        style="display: block; margin: 0 auto" />

$$\left\{\displaystyle{
    \begin{aligned}
        {\frac {\mathrm {d} x}{\mathrm {d} t}}&=\sigma (y-x),\\[6pt]
        {\frac {\mathrm {d} y}{\mathrm {d} t}}&=x(\rho -z)-y\\[6pt]
        {\frac {\mathrm {d} z}{\mathrm {d} t}}&=xy-\beta z
    \end{aligned}
}
\right.
$$

## Le pendule simple (avec ou sans frottements)

$$\ddot{\theta} + \frac{\alpha}{ml}\dot{\theta}+\frac{g}{l}\sin(\theta)=0$$


<img src="results/pendule_sans_frottements.png" 
        alt="Picture" 
        width="800" 
        height="600" 
        style="display: block; margin: 0 auto" />

<img src="results/pendule_avec_frottements.png" 
        alt="Picture" 
        width="800" 
        height="600" 
        style="display: block; margin: 0 auto" />



## Le pendule double 

https://fr.wikipedia.org/wiki/Pendule_double

$$\displaystyle{
    \begin{cases}
    l_{1}{\ddot {\theta }}_{1}\cos(\theta _{1}-\theta _{2})+l_{2}{\ddot {\theta }}_{2}-l_{1}{\dot {\theta }}_{1}^{2}\sin(\theta _{1}-\theta _{2})+g\sin(\theta _{2})=0\\
    (m_{1}+m_{2})l_{1}{\ddot {\theta }}_{1}+m_{2}l_{2}{\ddot {\theta }}_{2}\cos(\theta _{1}-\theta _{2})+m_{2}l_{2}{\dot {\theta }}_{2}^{2}\sin(\theta _{1}-\theta _{2})+(m_{1}+m_{2})g\sin(\theta _{1})=0
    \end{cases}}
$$


<img src="results/double_pendulum_delay_10.gif" 
        alt="Picture" 
        width="800" 
        height="600" 
        style="display: block; margin: 0 auto" />

<img src="results/double_pendule.png" 
        alt="Picture" 
        width="800" 
        height="600" 
        style="display: block; margin: 0 auto" />



-----------


=> Pour aller plus loin sur les pendules:
https://jakevdp.github.io/blog/2017/03/08/triple-pendulum-chaos/

----


# La suite logistique

https://fr.wikipedia.org/wiki/Suite_logistique

$$
\begin{cases} 
    x_{n+1} & = \mu \, x_n \, (1-x_n) \\ 
    x_0 &\in [0,1]
\end{cases}
$$



<img src="results/chaos_4096_2048.png" 
        alt="Picture" 
        width="800" 
        height="600" 
        style="display: block; margin: 0 auto" />


# Henon's map

https://en.wikipedia.org/wiki/H%C3%A9non_map



<img src="results/henon_x.png" 
        alt="Picture" 
        width="800" 
        height="600" 
        style="display: block; margin: 0 auto" />

$$
\begin{cases} 
    x_{n+1} & = 1+y_n-ax_n^2 \\ 
    y_{n+1} &=  bx_n
\end{cases}
$$

Ce qui revien pour x à
$$x_{n+2}=1+bx_n-ax_{n+1}^2$$

# Attractors

## Rössler

$$\begin{cases} 
{\dot {x}} (t) &=-y(t)-z(t) \\
{\dot {y}}(t) &=x(t)+ay(t) \\
{\dot {z}}(t) &=b+z(t)(x(t)-c)
-\end{cases}
$$


<img src="results/attracteur_rossler_epure_03.png 
        alt="Picture" 
        width="800" 
        height="600" 
        style="display: block; margin: 0 auto" />

## Ueda 

## Clifford


<img src="results/clifford_04.png" 
        alt="Picture" 
        width="800" 
        height="800" 
        style="display: block; margin: 0 auto" />

## Hopalong


<img src="results/hopalong1_01.png" 
        alt="Picture" 
        width="800" 
        height="600" 
        style="display: block; margin: 0 auto" />

<img src="results/hopalong2_01.png" 
        alt="Picture" 
        width="800" 
        height="600" 
        style="display: block; margin: 0 auto" />

## Simples chaotic flow


<img src="results/simplest_chaotic_flow_01.png" 
        alt="Picture" 
        width="800" 
        height="600" 
        style="display: block; margin: 0 auto" />

# Chirikov Standard map

- http://www.scholarpedia.org/article/Chirikov_standard_map
- https://en.wikipedia.org/wiki/Standard_map

<img src="results/standard_map.gif" 
        alt="Picture" 
        width="800" 
        height="600" 
        style="display: block; margin: 0 auto" />


# Bouncing balls
https://www.youtube.com/watch?v=6z4qRhpBIyA

# Simulation système planétaire

<img src="results/simulation_systeme_terre_lunes.png" 
        alt="Picture" 
        style="display: block; margin: 0 auto" />

# Autres projets 
- https://sprott.physics.wisc.edu/chaos/comchaos.htm
- https://rreusser.github.io/sketches/
- https://sprott.physics.wisc.edu/
- https://examples.pyviz.org/attractors/attractors.html
- https://vedransekara.github.io/2016/11/14/strange_attractors.html
- https://examples.pyviz.org/attractors/attractors.html
- https://www.maplesoft.com/support/help/maple/view.aspx?path=MathApps%2fGuide#Real%20Numbers
- https://www.youtube.com/watch?v=6z4qRhpBIyA
- https://www.youtube.com/watch?v=kbKtFN71Lfs

# Theory

- https://sprott.physics.wisc.edu/pubs/paper249/PAPER249.HTM
- https://en.wikipedia.org/wiki/Kaplan%E2%80%93Yorke_conjecture
- https://fr.wikipedia.org/wiki/Exposant_de_Liapounov