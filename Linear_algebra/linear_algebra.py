import sympy as sp
from sympy.interactive.printing import init_printing
import numpy as np


if __name__ == '__main__':
    init_printing(use_unicode=False, wrap_line=False)
    x, y, z, a, b, c = sp.symbols("x, y, z, a, b, c")
    A = sp.Matrix([[x, y, z], [a, b, c], [x+a, y+b, z+c]])
    sp.pprint(f"A = {A}")

    A_det = A.det()
    sp.pprint(f"det(A) = {A_det}")
    A_inv = A.pinv()
    sp.pprint(f"A^-1 = {A_inv}")

    chr()