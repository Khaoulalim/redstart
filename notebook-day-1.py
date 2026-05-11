import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return np, plt, sci


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell
def _():
    l=2 
    M=1
    g=1
    print(l,M,g)
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le booster est soumis à deux forces principales :

    * le poids, dirigé vers le bas,
    * la force exercée par le réacteur.

    La poussée du réacteur a une intensité $f$.
    Sa direction dépend de l’inclinaison du booster $\theta$ ainsi que de l’orientation du moteur $\phi$.

    L’angle total de la poussée est donc :

    $$
    \theta + \phi
    $$

    Pour obtenir les composantes horizontale et verticale de cette force, on projette le vecteur de poussée sur les axes $x$ et $y$.

    On obtient alors :

    $$
    f_x = -f \sin(\theta + \phi)
    $$

    $$
    f_y = f \cos(\theta + \phi)
    $$

    Le signe négatif dans $f_x$ vient du fait que lorsque l’angle est positif, la poussée est dirigée vers la gauche.
    """)
    return


@app.cell(hide_code=True)
def _(np):
    def force(f,theta,phi):
        fx = -f * np.sin(theta + phi)
        fy =  f * np.cos(theta + phi)
        return fx,fy


    return (force,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On applique la deuxième loi de Newton au centre de masse du booster.

    Deux forces agissent sur le booster :

    * la poussée du réacteur $(f_x, f_y)$,
    * le poids $(0, -Mg)$.

    ### Selon l’axe horizontal $x$

    La somme des forces selon $x$ vaut :

    $$
    M \ddot{x} = f_x
    $$

    Or :

    $$
    f_x = -f \sin(\theta + \phi)
    $$

    Donc :

    $$
    M \ddot{x} = -f \sin(\theta + \phi)
    $$

    Finalement :

    $$
    \ddot{x} = -\frac{f}{M}\sin(\theta + \phi)
    $$

    ---

    ### Selon l’axe vertical $y$

    La somme des forces selon $y$ vaut :

    $$
    M \ddot{y} = f_y - Mg
    $$

    Or :

    $$
    f_y = f \cos(\theta + \phi)
    $$

    Donc :

    $$
    M \ddot{y} = f \cos(\theta + \phi) - Mg
    $$

    Finalement :

    $$
    \ddot{y} = \frac{f}{M}\cos(\theta + \phi) - g
    $$

    Ces deux équations différentielles décrivent l’évolution du centre de masse du booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable J.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le booster est modélisé comme une tige rigide homogène de masse $M$ et de longueur totale $l$.

    Le moment d’inertie d’une tige homogène par rapport à son centre de masse est :

    $$
    J = \frac{1}{12} M l^2
    $$

    Dans notre cas :

    - $M = 1 \ \text{kg}$
    - $l = 2 \ \text{m}$

    On remplace :

    $$
    J = \frac{1}{12} \times 1 \times 2^2
    $$

    $$
    J = \frac{4}{12}
    $$

    $$
    J = \frac{1}{3}
    $$

    Ainsi :

    $$
    J = \frac{1}{3} \ \text{kg}.\ \text{m}^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l**2 / 12
    print(f"Moment d'inertie : J= {J:.4f} kg·m²")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pour trouver l’équation de l’angle \(\theta\), on étudie la rotation du booster autour de son centre de masse.

    On applique la deuxième loi de Newton en rotation :

    \[
    J \ddot{\theta} = \tau
    \]

    où \(\tau\) représente le moment des forces.

    Le moteur est placé à la base du booster. Comme le centre de masse est au milieu de la tige, la distance entre le centre de masse et le moteur vaut :

    \[
    \frac{l}{2}
    \]

    Le vecteur position du moteur est donc :

    \[
    r = \frac{l}{2}(\sin\theta,-\cos\theta)
    \]

    La force du moteur vaut :

    \[
    F =
    (-f\sin(\theta+\phi),\ f\cos(\theta+\phi))
    \]

    Le moment de cette force est donné par :

    \[
    \tau = r_x f_y - r_y f_x
    \]

    En remplaçant :

    \[
    \tau =
    \frac{l}{2}\sin\theta \cdot f\cos(\theta+\phi)
    -
    \left(
    -\frac{l}{2}\cos\theta
    \right)
    \left(
    -f\sin(\theta+\phi)
    \right)
    \]

    On obtient :

    \[
    \tau =
    \frac{lf}{2}
    \left[
    \sin\theta\cos(\theta+\phi)
    -
    \cos\theta\sin(\theta+\phi)
    \right]
    \]

    Avec l’identité trigonométrique :

    \[
    \sin a \cos b - \cos a \sin b
    =
    \sin(a-b)
    \]

    on trouve :

    \[
    \tau =
    \frac{lf}{2}\sin(-\phi)
    \]

    et comme :

    \[
    \sin(-\phi)=-\sin(\phi)
    \]

    alors :

    \[
    \tau =
    -\frac{lf}{2}\sin(\phi)
    \]

    Donc l’équation différentielle finale est :

    \[
    J\ddot{\theta}
    =
    -\frac{lf}{2}\sin(\phi)
    \]

    Finalement :

    \[
    \ddot{\theta}
    =
    -\frac{lf}{2J}\sin(\phi)
    \]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On définit l’état du système par :

    \(x\) position horizontale,
    \(v_x\) vitesse horizontale,
    \(y\) position verticale,
    \(v_y\) vitesse verticale,
    \(\theta\) angle du booster,
    \(\omega\) vitesse angulaire.

    Donc le vecteur d’état est :

    \[
    s = (x, v_x, y, v_y, \theta, \omega)
    \]

    On a donc 6 variables, ce qui donne :

    \[
    n = 6
    \]


    On cherche ensuite une fonction \(F\) telle que :

    \[
    \dot{s} = F(s, f, \phi)
    \]


    En utilisant les équations de Newton vues avant, on obtient :

    - pour \(x\) :
    \[
    \dot{x} = v_x
    \]
    \[
    \dot{v_x} = -\frac{f}{M} \sin(\theta + \phi)
    \]

    - pour \(y\) :
    \[
    \dot{y} = v_y
    \]
    \[
    \dot{v_y} = \frac{f}{M} \cos(\theta + \phi) - g
    \]

    - pour la rotation :
    \[
    \dot{\theta} = \omega
    \]
    \[
    \dot{\omega} = -\frac{l f}{2J} \sin(\phi)
    \]


    Donc finalement, le champ de vecteurs est :

    \[
    F(s,f,\phi) =
    (x', v_x', y', v_y', \theta', \omega')
    \]

    avec :

    \[
    (x', v_x', y', v_y', \theta', \omega')
    =
    \left(
    v_x,
    -\frac{f}{M}\sin(\theta + \phi),
    v_y,
    \frac{f}{M}\cos(\theta + \phi) - g,
    \omega,
    -\frac{l f}{2J}\sin(\phi)
    \right)
    \]
    """)
    return


@app.cell
def _(M, force, g, l, np):
    def F(s, f, phi):
        x, vx, y, vy, theta, omega = s
        fx, fy = force(f, theta, phi)
        return np.array([
            vx,
            fx / M,
            vy,
            fy / M - g,
            omega,
            (-l * f * np.sin(phi)) / 2J
        ])

    return (F,)


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    plt.show()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dans cette question, on construit une fonction `redstart_solve` qui permet de simuler l’évolution du booster dans le temps à partir de ses équations différentielles.

    L’idée est de transformer le système physique en un problème numérique que l’on peut résoudre avec un solveur d’équations différentielles.


    On commence par définir la dynamique du système.

    À chaque instant \(t\), l’état du booster est donné par :

    \[
    (x, v_x, y, v_y, \theta, \omega)
    \]

    et la fonction `f_phi(t, y)` fournit les paramètres de contrôle :

    - la force \(f\)
    - l’angle \(\phi\)



    On applique ensuite la deuxième loi de Newton :

    - la force est décomposée avec la fonction `force(f, theta, phi)`
    - on obtient les accélérations selon \(x\) et \(y\)
    - on ajoute la gravité sur l’axe vertical

    Cela donne le système :

    - \( \dot{x} = v_x \)
    - \( \dot{v_x} = f_x / M \)
    - \( \dot{y} = v_y \)
    - \( \dot{v_y} = f_y / M - g \)
    - \( \dot{\theta} = \omega \)
    - \( \dot{\omega} = (-l f \sin(\phi)) / 2J \)


    Ensuite, on utilise `solve_ivp` de SciPy pour résoudre numériquement ce système sur l’intervalle de temps donné.

    On active aussi `dense_output=True` pour pouvoir évaluer la solution à n’importe quel instant.



    La fonction retourne une fonction `sol(t)` qui permet d’obtenir directement l’état du système à tout moment :

    \[
    (x(t), v_x(t), y(t), v_y(t), \theta(t), \omega(t))
    \]
    """)
    return


@app.cell
def _(F, sci):

    def redstart_solve(t_span, y0, f_phi, max_step=0.01):

        def fun(t, y):

            f, phi = f_phi(t, y)
            return F(y, f, phi)

        # Résolution avec sortie dense pour interpolation
        result = sci.solve_ivp(
            fun=fun,
            t_span=t_span,
            y0=y0,
            dense_output=True,
            max_step=max_step
        )

        return result.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dans cette question, on étudie le cas le plus simple du modèle : la chute libre du booster.

    On considère qu’il n’y a aucun moteur, donc aucune force de propulsion. Le seul effet qui agit sur le système est la gravité.


    On part de l’équation du mouvement vertical :

    \[
    \ddot{y} = -g
    \]

    Avec les conditions initiales :

    - \(y(0) = 10\)
    - \(v_y(0) = 0\)



    En intégrant cette équation, on obtient :

    \[
    y(t) = 10 - \frac{1}{2} g t^2
    \]

    On cherche ensuite le moment où le centre de masse atteint la hauteur \(y = \ell\), avec \(\ell = 2\).

    Donc :

    \[
    10 - \frac{1}{2} t^2 = 2
    \]

    ce qui donne :

    \[
    t = 4 \ \text{s}
    \]



    Ensuite, on vérifie ce résultat numériquement en utilisant la fonction `redstart_solve`.

    On simule l’évolution du système dans le temps et on extrait la trajectoire \(y(t)\).

    On trace alors :

    - la courbe de \(y(t)\)
    - la droite horizontale \(y = \ell\)
    - le point où la courbe coupe cette droite



    Le but est de comparer la solution théorique avec la simulation numérique pour vérifier que le modèle est correct.

    Le résultat obtenu est cohérent : le centre de masse atteint bien \(y = \ell\) autour de \(t = 4\) secondes.
    """)
    return


@app.cell
def _(g, l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]  # [x, vx, y, vy, theta, omega]

        def f_phi(t, y):
            return np.array([0.0, 0.0])  # [f, phi]

        sol = redstart_solve(t_span, y0, f_phi)

        # Temps théorique
        t_theory = np.sqrt(2 * (y0[2] - l) / g)
        print(f"Temps théorique t* = √18 = {t_theory:.4f} s")

        # Vérification numérique
        y_at_theory = sol(t_theory)[2]
        print(f"y(t*) = {y_at_theory:.6f} m (devrait être ≈ 1.0)")

        # Graphique
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(t, y_t, 'b-', linewidth=2, label=r"$y(t)$")
        ax.axhline(y=l, color='grey', linestyle='--', label=r"$y=\ell=1$")
        ax.axvline(x=t_theory, color='red', linestyle=':', linewidth=2, label=f"$t^* = \\sqrt{{18}} \\approx {t_theory:.2f}$s")
        ax.set_title("Free Fall Test")
        ax.set_xlabel("time $t$ (s)")
        ax.set_ylabel("height $y$ (m)")
        ax.set_xlim([0, 5])
        ax.set_ylim([0, 11])
        ax.grid(True)
        ax.legend()

        # Point d'intersection
        ax.plot(t_theory, l, 'ro', markersize=10)

        plt.tight_layout()
        plt.show()  # ← IMPORTANT pour afficher

        return fig

    # EXÉCUTION
    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell
def _(M, g, l, np, plt, redstart_solve):
    def controlled_landing():
        # Conditions initiales
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]  # [x, vx, y, vy, theta, omega]

        # Coefficients de la trajectoire planifiée y(t) = a3*t³ + a2*t² + a1*t + a0
        # Contraintes : y(0)=10, ẏ(0)=-2, y(5)=1, ẏ(5)=0
        a3 = 0.064
        a2 = -0.28
        a1 = -2.0
        a0 = 10.0

        def y_plan(t):
            return a3*t**3 + a2*t**2 + a1*t + a0

        def dy_plan(t):
            return 3*a3*t**2 + 2*a2*t + a1

        def d2y_plan(t):
            return 6*a3*t + 2*a2

        # Commande : f(t) = ÿ(t) + g (car θ=φ=0 → ÿ = f - g)
        def f_phi(t, y):
            f = d2y_plan(t) + g
            # Vérifier que f ≥ 0
            if f < 0:
                print(f"ATTENTION : f({t}) = {f} < 0 !")
            return np.array([max(f, 0), 0.0])  # phi = 0

        # Simulation
        sol = redstart_solve([0, 5], y0, f_phi)

        # Vérification finale
        final = sol(5.0)
        print(f"=== Vérification ===")
        print(f"y(5)    = {final[2]:.6f}  (objectif: 1.0)")
        print(f"vy(5)   = {final[3]:.6f}  (objectif: 0.0)")
        print(f"theta(5)= {final[4]:.6f}  (objectif: 0.0)")

        # Graphiques
        t = np.linspace(0, 5, 500)
        states = sol(t)

        fig, axes = plt.subplots(2, 2, figsize=(12, 10))

        # Hauteur
        ax = axes[0, 0]
        ax.plot(t, states[2], 'b-', lw=2, label=r"$y(t)$")
        ax.plot(t, [y_plan(ti) for ti in t], 'r--', label=r"$y_{plan}(t)$")
        ax.axhline(y=l, color='grey', ls='--', label=r"$y=\ell=1$")
        ax.set_title("Hauteur"); ax.set_xlabel("t (s)"); ax.set_ylabel("y (m)")
        ax.legend(); ax.grid(True)

        # Vitesse verticale
        ax = axes[0, 1]
        ax.plot(t, states[3], 'b-', lw=2, label=r"$v_y(t)$")
        ax.plot(t, [dy_plan(ti) for ti in t], 'r--', label=r"$\dot{y}_{plan}(t)$")
        ax.axhline(y=0, color='grey', ls='--')
        ax.set_title("Vitesse verticale"); ax.set_xlabel("t (s)"); ax.set_ylabel(r"$v_y$ (m/s)")
        ax.legend(); ax.grid(True)

        # Commande
        ax = axes[1, 0]
        f_vals = [d2y_plan(ti) + g for ti in t]
        ax.plot(t, f_vals, 'g-', lw=2, label=r"$f(t)$")
        ax.axhline(y=M*g, color='grey', ls='--', label=r"$Mg = 1$")
        ax.set_title("Commande"); ax.set_xlabel("t (s)"); ax.set_ylabel("f (N)")
        ax.legend(); ax.grid(True)

        # Trajectoire x-y
        ax = axes[1, 1]
        ax.plot(states[0], states[2], 'b-', lw=2)
        ax.set_title("Trajectoire (x, y)"); ax.set_xlabel("x (m)"); ax.set_ylabel("y (m)")
        ax.set_aspect('equal'); ax.grid(True)

        plt.tight_layout()
        plt.show()  # ← ESSENTIEL pour l'affichage

        return fig

    # ========== APPEL DE LA FONCTION ==========
    controlled_landing()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.function
def make_world(view_box, *objects):
    """
    Crée une scène SVG avec ciel, sol et cible d'atterrissage.

    Paramètres:
        view_box : [x_min, x_max, y_min, y_max]
        *objects : éléments SVG supplémentaires (booster, etc.)
    """
    x_min, x_max, y_min, y_max = view_box
    width = x_max - x_min
    height = y_max - y_min

    svg_string = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x_min} {y_min} {width} {height}" width="400" height="300">
    <g transform="translate(0, {y_min + y_max}) scale(1, -1)">
        <!-- Ciel -->
        <rect x="{x_min}" y="{y_min}" width="{width}" height="{height}" fill="lightblue" opacity="0.6"/>

        <!-- Sol -->
        <rect x="{x_min}" y="{y_min}" width="{width}" height="{abs(y_min)}" fill="saddlebrown"/>

        <!-- Cible d'atterrissage : 2m de large, centrée en x=0 -->
        <rect x="-1" y="0" width="2" height="0.15" fill="limegreen" stroke="darkgreen" stroke-width="0.02"/>

        <!-- Objets supplémentaires -->
        {''.join(str(obj) for obj in objects)}
    </g>
    </svg>'''

    return svg_string


@app.cell
def _(mo):
    # Test 1 : Monde vide
    scene1 = make_world([-3, 3, -2, 4])

    # Test 2 : Avec un carré noir sur la cible
    scene2 = make_world([-3, 3, -2, 4], 
        f'<rect x="-1" y="0" width="2" height="2" fill="black"/>')

    # Test 3 : Avec deux carrés
    scene3 = make_world([-3, 3, -2, 4],
        f'<rect x="-3" y="2" width="2" height="2" fill="red"/>',
        f'<rect x="1" y="2" width="2" height="2" fill="blue"/>')

    # Affichage côte à côte dans marimo
    mo.hstack([
        mo.Html(scene1),
        mo.Html(scene2),
        mo.Html(scene3)
    ], justify="space-around")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell
def _(M, g, l, np):
    def draw_booster(x, y, theta, f, phi):
        """
        Dessine un booster statique en SVG.

        Paramètres:
            x, y   : position du centre de masse
            theta  : angle du booster (rad)
            f      : amplitude de la force
            phi    : angle de la force par rapport à l'axe (rad)
        """
        w_body = 0.2       # largeur du corps
        h_body = 2 * l     # hauteur = longueur totale

        # Longueur de la flamme proportionnelle à f
        flame_len = (f / (M * g)) * (l / 2) if f > 0 else 0

        # La flamme pointe dans la direction opposée à la force
        # La force est à angle (theta + phi), la flamme à (theta + phi + pi)
        flame_angle = theta + phi + np.pi

        svg_booster = f'''<g transform="translate({x}, {y}) rotate({-np.degrees(theta)})">
            <!-- Corps du booster -->
            <rect x="{-w_body/2}" y="{-l}" width="{w_body}" height="{h_body}" 
                  fill="silver" stroke="black" stroke-width="0.05"/>

            <!-- Marqueur haut -->
            <rect x="{-w_body/2}" y="{l-0.2}" width="{w_body}" height="0.2" fill="darkgrey"/>

            <!-- Flamme du réacteur -->
            <g transform="translate(0, {l}) rotate({-np.degrees(phi + np.pi)})">
                <rect x="{-w_body/3}" y="0" width="{w_body/1.5}" height="{flame_len}" 
                      fill="orange" stroke="red" stroke-width="0.02" opacity="0.8"/>
            </g>
        </g>'''

        return svg_booster

    return (draw_booster,)


@app.cell
def _(M, draw_booster, g, l, mo, np):
    # Test des trois scénarios demandés
    test_scene_1 = make_world([-3, 3, -2, 4], 
        draw_booster(0, l/2, 0, 0, 0))

    test_scene_2 = make_world([-3, 3, -2, 4],
        draw_booster(0, l, 0, M * g, 0))

    test_scene_3 = make_world([-3, 3, -2, 4],
        draw_booster(-l/2, l, np.pi/4, 2 * M * g, np.pi/2))

    # Affichage
    mo.hstack([
        mo.Html(test_scene_1),
        mo.Html(test_scene_2),
        mo.Html(test_scene_3)
    ], justify="space-around")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell
def _(M, g, l, np):
    def animate_booster(x, y, theta, f, phi, T, n_frames=50):
        """
        Crée une animation SVG du booster.

        Paramètres:
            x, y, theta, f, phi : fonctions du temps t
            T                   : durée de l'animation (s)
            n_frames            : nombre de frames pour l'animation
        """
        # Échantillonnage temporel
        times = np.linspace(0, T, n_frames)

        # Calcul des keyframes
        positions = [f"{x(t):.4f},{y(t):.4f}" for t in times]
        rotations = [f"{-np.degrees(theta(t)):.2f}" for t in times]
        flames = [f"{(f(t)/(M*g))*(l/2):.4f}" for t in times]

        # Chaînes de valeurs pour SVG
        pos_values = ";".join(positions)
        rot_values = ";".join(rotations)
        flame_values = ";".join(flames)

        w_body = 0.2
        h_body = 2 * l

        svg_animation = f'''<g>
            <!-- Animation de translation -->
            <animateTransform attributeName="transform" type="translate"
                values="{pos_values}" dur="{T}s" repeatCount="indefinite" calcMode="linear"/>

            <!-- Animation de rotation (additive pour combiner avec translation) -->
            <animateTransform attributeName="transform" type="rotate"
                values="{rot_values}" dur="{T}s" repeatCount="indefinite" calcMode="linear" additive="sum"/>

            <!-- Corps du booster -->
            <rect x="{-w_body/2}" y="{-l}" width="{w_body}" height="{h_body}" 
                  fill="silver" stroke="black" stroke-width="0.05"/>

            <!-- Flamme avec animation de hauteur -->
            <g transform="translate(0, {l})">
                <rect x="{-w_body/3}" y="0" width="{w_body/1.5}" 
                      height="{flames[0]}" fill="orange" stroke="red" stroke-width="0.02" opacity="0.8">
                    <animate attributeName="height"
                        values="{flame_values}" dur="{T}s" repeatCount="indefinite" calcMode="linear"/>
                </rect>
            </g>
        </g>'''

        return svg_animation

    return (animate_booster,)


@app.cell
def _(M, animate_booster, g, l, mo, np):
    def test_animation_0():
        """Scénario de test pour l'animation."""
        T = 5.0

        def x(t): return -l/2 + l * (t / T)
        def y(t): return l/2 + l/2 * (t / T)
        def theta(t): return (t / T) * 2 * np.pi
        def f(t): return M * g * (t / T)
        def phi(t): return 2 * np.pi * (t / T)

        return animate_booster(x, y, theta, f, phi, T=T)

    # Affichage centré dans marimo
    mo.Html(
        make_world([-3, 3, -2, 4], test_animation_0())
    ).center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell
def _(M, animate_booster, g, np, redstart_solve):
    def create_simulation_animation(y0, f_phi_func, T=5.0):
        """
        Crée une animation à partir d'une simulation numérique.
        """
        # Simulation
        sol = redstart_solve([0, T], y0, f_phi_func)

        # Extraction des fonctions temporelles
        def x_fn(t): return float(sol(t)[0])
        def y_fn(t): return float(sol(t)[2])
        def theta_fn(t): return float(sol(t)[4])

        def f_fn(t): 
            f_val, _ = f_phi_func(t, sol(t))
            return float(f_val)

        def phi_fn(t):
            _, phi_val = f_phi_func(t, sol(t))
            return float(phi_val)

        return animate_booster(x_fn, y_fn, theta_fn, f_fn, phi_fn, T)

    # ============================================================
    # SCÉNARIO 1 : Chute libre
    # ============================================================
    y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

    def f_phi_free(t, y):
        return np.array([0.0, 0.0])

    anim_free = create_simulation_animation(y0, f_phi_free, T=5.0)

    # ============================================================
    # SCÉNARIO 2 : Poussée verticale équilibrée
    # ============================================================
    def f_phi_hover(t, y):
        return np.array([M * g, 0.0])

    anim_hover = create_simulation_animation(y0, f_phi_hover, T=5.0)

    # ============================================================
    # SCÉNARIO 3 : Poussée latérale
    # ============================================================
    def f_phi_drift(t, y):
        return np.array([M * g, np.pi/8])

    anim_drift = create_simulation_animation(y0, f_phi_drift, T=5.0)

    # ============================================================
    # SCÉNARIO 4 : Atterrissage contrôlé
    # ============================================================
    y0_land = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
    a3, a2 = 0.064, -0.28

    def f_phi_land(t, y):
        f = (6*a3*t + 2*a2) + g
        return np.array([max(f, 0), 0.0])

    anim_land = create_simulation_animation(y0_land, f_phi_land, T=5.0)
    return anim_drift, anim_free, anim_hover, anim_land


@app.cell
def _(anim_drift, anim_free, anim_hover, anim_land, mo):
    # Affichage des 4 animations
    mo.vstack([
        mo.hstack([
            mo.Html(make_world([-3, 3, -2, 4], anim_free)),
            mo.Html(make_world([-3, 3, -2, 4], anim_hover))
        ]),
        mo.hstack([
            mo.Html(make_world([-3, 3, -2, 4], anim_drift)),
            mo.Html(make_world([-3, 3, -2, 4], anim_land))
        ])
    ])
    return


if __name__ == "__main__":
    app.run()
