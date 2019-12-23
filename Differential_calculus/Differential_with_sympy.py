import os
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import sympy
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import axes3d, Axes3D
from sympy.utilities.lambdify import lambdastr


if __name__ == '__main__':
    x, y = sp.symbols("x, y")

    G = 9 * x ** 2 + 3 * x + 1
    g = sp.diff(G, x)
    X = np.linspace(-10, 10, 1_000)
    plt.plot(X, [G.evalf(subs={"x": i}) for i in X], label=f"G = {G}")
    plt.plot(X, [g.evalf(subs={"x": i}) for i in X], label=f"g := G' = {g}")
    plt.grid()
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig(os.getcwd() + "/diff_exemple_G_and_g.png", dpi=300)
    plt.show()

    F = x**2 - y**2
    grad_F = [sp.diff(F, x_i) for x_i in (x, y)]
    print(f"grad_F = {grad_F}")

    X = np.linspace(-5, 5, 50)
    Y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(X, Y)
    F_lambdify = sp.lambdify((x, y), F, modules="numpy")
    print(f"Grad_F = {lambdastr((x, y), grad_F)}")
    Z = F_lambdify(X, Y)
    grad_F_lambdify = sp.lambdify((x, y), grad_F, modules="numpy")

    fig = plt.figure()
    ax = Axes3D(fig)

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    # add gradient
    grad_Z = grad_F_lambdify(X, Y)
    ax.quiver(X, Y, Z, grad_Z[0], grad_Z[1], F_lambdify(*grad_Z), length=0.2, normalize=True,
              label=f"Vecteur directionnel du gradient")

    # Customize the z axis.
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.legend()
    plt.savefig(os.getcwd() + "/diff_exemple_F.png", dpi=300)
    plt.show()
