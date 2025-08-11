from résolution_rec import remplir_grille
from random import randint
from résolution_exhaustif import devenir_jouable
from rich import print


def afficher_sudoku_carre(grille, f):
    H = "┌───────┬───────┬───────┐"
    HM = "├───────┼───────┼───────┤"
    B = "└───────┴───────┴───────┘"

    def ligne(i):
        return (
            "│ "
            + " │ ".join(
                " ".join(
                    str(grille[i][j]) if grille[i][j] != 0 else "."
                    for j in range(k, k + 3)
                )
                for k in (0, 3, 6)
            )
            + " │"
        )

    f.write(H)
    f.write("\n")
    for i in range(9):
        f.write(ligne(i))
        f.write("\n")
        if i in [2, 5]:
            f.write(HM)
            f.write("\n")
    f.write(B)


def affiche_grille_jeu(grille):
    f = open("sudoku_jeu.txt", "w", encoding="utf-8")
    afficher_sudoku_carre(grille, f)
    f.close()
    f = open("sudoku_jeu.txt", "r", encoding="utf-8")
    texte = f.read()
    print(texte)


def mélange(T):
    for i in range(len(T)):
        j = randint(i, len(T) - 1)
        T[i], T[j] = T[j], T[i]


grille = [[0 for i in range(9)] for j in range(9)]
f2 = open("sudoku_jeu.txt", "w", encoding="utf-8")
afficher_sudoku_carre(grille, f2)
f2.close()
remplir_grille(grille)

grille_jouable = devenir_jouable(grille, 55)
liste_fixes = []

for i in range(9):
    for j in range(9):
        if grille_jouable[i][j] != 0:
            liste_fixes.append((i, j))


print("Voici la grille que je cache !")
affiche_grille_jeu(grille_jouable)

f = open("sudoku_à_faire.txt", "w", encoding="utf-8")
afficher_sudoku_carre(grille_jouable, f)
f.close()

f1 = open("sudoku_fini.txt", "w", encoding="utf-8")
afficher_sudoku_carre(grille, f1)
f1.close()

satisfait = False

while not satisfait:
    demande = ""
    while demande != "l" and demande != "c" and demande != "b":
        demande = input(
            "Voulez vous vérifier une ligne (l), une colonne (c) ou un bloc (b) ? Saississez, s'il vous plait, l'une des trois lettres 'l', 'c' ou 'b'.\n"
        )
    if demande == "l":
        ligne = 10
        while ligne > 9 or ligne < 0:
            ligne = int(
                input("Saisissez l'indice de la ligne que vous voulez vérifier.\n")
            )
        T = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        mélange(T)  # on a bien une permutation "aléatoire"
        liste = grille[ligne]
        res = []
        grille_a_montrer = []
        for i in range(9):
            res.append(T[liste[i] - 1])
        for i in range(9):
            if i == ligne:
                grille_a_montrer.append(res)
            else:
                grille_a_montrer.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        print("Je sais résoudre un sudoku, regarde :")
        affiche_grille_jeu(grille_a_montrer)
    elif demande == "c":
        colonne = 10
        while colonne > 9 or colonne < 0:
            colonne = int(
                input("Saisissez l'indice de la colonne que vous voulez vérifier.\n")
            )
        T = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        mélange(T)
        liste = [grille[i][colonne] for i in range(9)]
        res = []
        grille_a_montrer = [[0 for i in range(9)] for j in range(9)]
        for i in range(9):
            res.append(T[liste[i] - 1])
        for i in range(9):
            for j in range(9):
                if j == colonne:
                    grille_a_montrer[i][j] = str(res[i])
        print("Je sais résoudre un sudoku, regarde :")
        affiche_grille_jeu(grille_a_montrer)

    elif demande == "b":
        bloc = 10
        while bloc > 9 or bloc < 0:
            bloc = int(input("Saisissez l'indice du bloc que vous voulez vérifier.\n"))
        T = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        mélange(T)
        liste = []
        bloc_ligne = (bloc // 3) * 3
        bloc_col = (bloc % 3) * 3
        for a in range(3):
            for b in range(3):
                liste.append(grille[bloc_ligne + a][bloc_col + b])
        res = []
        grille_a_montrer = [[0 for i in range(9)] for j in range(9)]
        for i in range(9):
            res.append(T[liste[i] - 1])
        a = 0
        for i in range(9):
            for j in range(9):
                if (i // 3) * 3 + j // 3 == bloc:
                    grille_a_montrer[i][j] = str(res[a])
                    a += 1
        print("Je sais résoudre un sudoku, regarde :")
        affiche_grille_jeu(grille_a_montrer)
    satisf = ""
    while satisf != "o" and satisf != "n":
        satisf = input(
            "Etes-vous convaincus ? Veuillez saisir 'o' pour oui et 'n' pour toujours pas.\n"
        )
    if satisf == "o":
        satisfait = True
    elif satisf == "n":
        satisfait = False
