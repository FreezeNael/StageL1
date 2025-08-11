from random import choice


def occurence(liste, c):
    compteur = 0
    for e in liste:
        if e == c:
            compteur += 1
    return compteur


def lignes_compatibles(grille):
    for i in range(1, len(grille)):
        ligne = i - 1
        while ligne >= 0:
            for j in range(9):
                if grille[i][j] == grille[ligne][j]:
                    return False
                elif (i % 3 == 1 and ligne > i - 2) or (i % 3 == 2 and ligne > i - 3):
                    if j % 3 == 1:
                        for k in grille[i][j - 1: j + 2]:
                            if k in grille[ligne][j - 1: j + 2]:
                                return False
            ligne -= 1
    return True


def genere_ligne():
    ligne = []
    B = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for _ in range(9):
        c = choice(B)
        ligne.append(c)
        B.remove(c)
    return ligne


def matrice_to_liste(matrice):
    L = []
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            L.append(matrice[i][j])
    return L


def devenir_jouable(grille, n):
    liste = matrice_to_liste(grille)
    B = [i for i in range(80)]
    for _ in range(n):
        c = choice(B)
        while liste[c] == 0:
            c = choice(B)
        liste[c] = 0
        B.remove(c)
    return liste_to_matrice(liste)


def liste_to_matrice(liste):
    M = []
    for i in range(9):
        L = []
        for j in range(9):
            L.append(liste[j + 9 * i])
        M.append(L)
    return M
