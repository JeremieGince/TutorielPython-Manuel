import sympy as sp
from sympy.interactive.printing import init_printing


if __name__ == '__main__':
    init_printing(pretty_print=False, use_unicode=False, wrap_line=False, use_latex=True)

    f, g = sp.symbols('f g', cls=sp.Function)
    x = sp.symbols("x")

    edo_g = sp.Eq(3*g(x).diff(x) + x, 6)
    print(sp.pretty(edo_g))

    edo_g_solved = sp.dsolve(edo_g, g(x))
    print(sp.pretty(edo_g_solved))

    print('-' * 175)

    v = sp.Symbol("v", reel=True, positive=True)
    bessel_edo = sp.Eq((x**2)*f(x).diff(x, x) + x*f(x).diff(x) + (x**2 - v**2)*f(x), 0)
    print(sp.pretty(bessel_edo))

    bessel_edo_solved = sp.dsolve(bessel_edo, f(x))
    print(sp.pretty(bessel_edo_solved))

    print('-' * 175)

    psi = sp.symbols("psi", cls=sp.Function)
    t = sp.Symbol("t", reel=True, positive=True)
    omega0 = sp.Symbol("omega_0", reel=True)
    osc_hrm_edo = sp.Eq(psi(t).diff(t, t) + (omega0**2)*psi(t), 0)
    print(sp.pretty(osc_hrm_edo))

    osc_hrm_edo_solved = sp.dsolve(osc_hrm_edo, psi(t))
    print(sp.pretty(osc_hrm_edo_solved))

    print('-'*175)

    psi = sp.Function("psi")
    E, hbar, m, omega = sp.symbols("E hbar m omega", reel=True)
    V = (1/2)*m*(omega**2)*(x**2)
    quantum_osc_hrm_edo = sp.Eq((-(hbar**2)/(2*m))*psi(x).diff(x, x) + V*psi(x), E*psi(x))
    print(sp.pretty(quantum_osc_hrm_edo))
    print(sp.latex(quantum_osc_hrm_edo))

    quantum_osc_hrm_edo_solved = sp.dsolve(quantum_osc_hrm_edo, psi(x))
    print(sp.pretty(quantum_osc_hrm_edo_solved))
    print(sp.latex(quantum_osc_hrm_edo_solved))


