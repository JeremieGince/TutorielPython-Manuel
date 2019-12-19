import scipy as sc
from scipy.integrate import nquad


if __name__ == '__main__':
    # Let's say we are given a f function that we want to find its primitive.
    def f(x, y, z):
        return x**2 + y**2 + sc.cos(z)

    # Here we defined our integration bounds
    def bound_x(y, z):
        return [-10*y, 10*z]

    def bound_y(z):
        return [0, 5*z]

    def bound_z():
        return [0, sc.pi]

    # And we use the nquad function to find the definite integral of f
    P = nquad(f, [bound_x, bound_y, bound_z])
    print(f"P = {P[0]:.5e}, absolute error = {P[1]:.5e}")
