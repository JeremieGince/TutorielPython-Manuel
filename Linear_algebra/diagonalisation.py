import sympy as sp

if __name__ == '__main__':
    j = complex(0, 1)
    A = sp.Matrix([
        [1, 0, -1],
        [0, 1, j],
        [-1, -j, 0]
    ])

    A_eigenvectors = A.eigenvects()

    print(f"A := {A}", '-'*25, sep='\n')
    for eigenvalue, multiplicity, eigenvector in A_eigenvectors:
        print(f"lambda = {eigenvalue}, m = {multiplicity}", eigenvector, '-'*175, sep='\n')

    E, a, theta = sp.symbols("E a theta")
    H = sp.Matrix([
        [E, a, 0],
        [a, E, a],
        [0, a, E]
    ])
    H_eigenvectors = H.eigenvects()

    print(f"H := {H}", '-' * 25, sep='\n')
    for eigenvalue, multiplicity, eigenvector in H_eigenvectors:
        print(f"lambda = {eigenvalue}, m = {multiplicity}", eigenvector, '-'*175, sep='\n')

    R = sp.Matrix([
        [1, 0, 0],
        [0, sp.cos(theta), -sp.sin(theta)],
        [0, sp.sin(theta), sp.cos(theta)]
    ])
    RHRinv = R*H*R.inv()
    RHRinv_eigenvectors = RHRinv.eigenvects()

    print(f"RHRinv := {RHRinv}", '-' * 25, sep='\n')
    for eigenvalue, multiplicity, eigenvector in RHRinv_eigenvectors:
        print(f"lambda = {eigenvalue}, m = {multiplicity}", eigenvector, '-' * 175, sep='\n')

    print(H.eigenvals(), RHRinv.eigenvals(), sep='\n')
    check = all([e in RHRinv.eigenvals() for e in H.eigenvals()])
    print(f"H.eigenvals() == RHRinv.eigenvals(): {check}")