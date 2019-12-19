import sympy as sp
import numpy as np


if __name__ == '__main__':
    x = sp.Symbol('x')
    theta, phi = sp.symbols("theta phi")

    # Let's say we are given a symbolic function f and we want to know his primitive
    f = sp.cos(x + theta) + sp.sin(x + phi)
    print(f"f = {f}")

    # To obtain his primitive we can use the integrate method of sympy. It will compute a symbolic integral
    # with mathematical identities.
    F = sp.integrate(f, x)
    print(f"F = {F}")

    # We also able to obtain his evalution in x for 0 to pi.
    F_0_to_pi = sp.integrate(f, (x, 0, np.pi))
    print(f"F_0_to_pi = {F_0_to_pi}")

    # And we can eval it for theta = 0 and phi = pi/4
    F_0_to_pi_evalf = F_0_to_pi.evalf(subs={theta: 0, phi: np.pi/4})
    print(f"F_0_to_pi_evalf = {F_0_to_pi_evalf}")

    # Another way to find the primitive of f is to create an Integral object
    F = sp.Integral(f, x)
    print(f"F = {F}")

    # After we can find the primitive
    F = F.doit()
    print(f"F = {F}")

    # Let's say we are given another function with two independant variables
    y = sp.Symbol('y')
    g = sp.sin(x + theta)*sp.cos(y + phi) + sp.tan(x + theta) + sp.acos(y + phi)
    G = sp.integrate(g, x, y)
    print(f"G = {G}")
    # We are able to do a multiple definite integral
    G_evalf = sp.integrate(g, (x, 0, np.pi), (y, 0, 2*np.pi)).evalf(subs={theta: np.pi/2, phi: np.pi/6})
    print(f"G_evalf = {G_evalf}")
