import os
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import axes3d, Axes3D


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

    F = sp.cos(sp.sqrt(x**2 + y**2))
    f_x = sp.diff(F, x)
    f_y = sp.diff(F, y)

    X = np.linspace(-5, 5, 1_000)
    Y = np.linspace(-5, 5, 1_000)
    X, Y = np.meshgrid(X, Y)
    F_lambdify = sp.lambdify((x, y), F, modules="numpy")
    f_x_lambdify = sp.lambdify((x,), f_x, modules="numpy")
    f_y_lambdify = sp.lambdify((y,), f_y, modules="numpy")
    Z = F_lambdify(X, Y)

    fig = plt.figure()
    ax = Axes3D(fig)
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # add gradient
    ax.plot(X, f_x_lambdify(X))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.savefig(os.getcwd() + "/diff_exemple_F.png", dpi=300)
    plt.show()
