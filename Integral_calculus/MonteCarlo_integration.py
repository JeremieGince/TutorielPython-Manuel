import numpy as np
import sympy as sp
from sympy.utilities.lambdify import lambdastr
import itertools
import time


def monte_carlo_integration(integrand, bounds: list, n_sample: int = int(1e6)) -> float:
    """
    Compute the definite integral with a monte carlo integration algorithm
    :param integrand: the function to integrate (lambda or func)
    :param bounds: list of integral bounds ex: [[0, 10], [0, 2], [-10, 10]] (list)
    :param n_sample: number of sample to use (int)
    :return: the integral of the integrand (float)
    """
    np.random.seed(1)
    count_in_curve: int = 0

    def sampler():
        while True:
            yield [np.random.uniform(b0, b1) for [b0, b1] in bounds]

    x_rn0, x_rn1 = next(sampler()), next(sampler())
    f_min: float = np.min([integrand(*x_rn0), integrand(*x_rn1)])
    f_max: float = np.max([integrand(*x_rn0), integrand(*x_rn1)])

    for x in itertools.islice(sampler(), n_sample):
        f: float = integrand(*x)

        # Generate random point
        f_rn: float = np.random.uniform(f_min, f_max)

        # Increase the counter
        count_in_curve += 1 if 0 <= f_rn <= f else 0

        # update the domain size
        f_min = np.min([f_min, f])
        f_max = np.max([f_max, f])

    # Compute the hyper volume v of the statistical box
    v: float = np.prod([b1 - b0 for [b0, b1] in bounds]) * (f_max - f_min)
    return (count_in_curve / n_sample) * v


if __name__ == '__main__':
    bounds_x: list = [0, 9]
    bounds_y: list = [-10, 7]
    bounds_z: list = [0, 10]

    bounds: list = [bounds_x, bounds_y, bounds_z]

    def g(x, y, z):
        return 4*x**3 + y**2 + np.sqrt(z)

    start_time = time.time()

    P: float = monte_carlo_integration(g, bounds, n_sample=int(1e6))
    print(f"P = {P:.5e}")
    print(f"--- elapse time: {time.time() - start_time} s ---")

    x, y, z = sp.symbols("x, y, z")
    f = 4*x**3 + y**2 + sp.sqrt(z)
    print(f"f = {f}")
    f_lambdify = sp.lambdify((x, y, z), f)
    print(f"f_lambdify -> {lambdastr((x, y, z), f)}")

    for n in [int(1e1), int(1e3), int(1e6), int(1e8)]:
        start_time = time.time()
        P: float = monte_carlo_integration(f_lambdify, bounds, n_sample=n)
        print(f"P = {P:.5e} for {n:2e} samples")
        print(f"--- elapse time: {time.time() - start_time} s ---")
