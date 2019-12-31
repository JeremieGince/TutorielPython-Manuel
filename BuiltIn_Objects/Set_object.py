if __name__ == '__main__':
    A: set = {0, 1, 5, 6, 8}  # Creation du set A
    B: set = {2, 5, 8, 7, 5, 9}  # Creation du set B

    print(A, B)  # Affichage des set A et B

    # Acceder aux item dans le set A
    for x in A:
        print(x)

    # Ajout d'un item au set A
    A.add(11)
    print(A)
    A.add(6)
    print(A)

    # ajout de plusieurs items au set B
    B.update([2, 9, 11, 10, 25, 33])
    print(B)

    # On enleve un item du set B
    B.discard(33)
    print(B)
