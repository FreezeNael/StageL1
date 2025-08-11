from random import randint


def mélange(T):
    for i in range(len(T)):
        j = randint(i, len(T) - 1)
        T[i], T[j] = T[j], T[i]


def est_valide(grille, ligne, col, val):

    if val in grille[ligne]:
        return False

    if val in [grille[i][col] for i in range(9)]:
        return False

    bloc_ligne = (ligne // 3) * 3
    bloc_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grille[bloc_ligne + i][bloc_col + j] == val:
                return False
    return True


def remplir_grille(grille, i=0, j=0):
    if i == 9:
        return True  # la grille est remplie

    if j == 9:
        return remplir_grille(grille, i + 1, 0)  # quand on arrive au bout d'une ligne

    T = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mélange(
        T
    )  # on utilise une permutation aléatoire pour que l'ordre des chiffres que l'on essaie de placer soit aléatoire

    for val in T:
        if est_valide(grille, i, j, val):
            grille[i][j] = val
            if remplir_grille(grille, i, j + 1):
                return True
            grille[i][j] = 0  # retour en arrière
    return False  # retour en arrière


# À chaque cellule (i, j) :

# On teste tous les chiffres possibles de 1 à 9 dans un ordre aléatoire.

# Si on trouve un chiffre valide, on avance à la case suivante.

# Sinon, on revient en arrière.
