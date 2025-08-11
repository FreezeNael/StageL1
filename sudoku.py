from random import randint, choice


def fusion_blocs(blocs1, blocs2):
    # Choisir blocs 0 à 4 depuis blocs1, le reste depuis blocs2
    blocs_fusion = {}
    for i in range(9):
        if i <= 4:
            blocs_fusion[i] = blocs1[i]
        else:
            blocs_fusion[i] = blocs2[i]
    # Préparer une grille vide (liste plate de 81 zéros)
    grille = [0] * 81
    # Insérer les valeurs des blocs fusionnés dans la grille
    for i in range(9):
        start_row = (i // 3) * 3
        start_col = (i % 3) * 3
        for k in range(9):
            row = start_row + k // 3
            col = start_col + k % 3
            index = row * 9 + col
            grille[index] = blocs_fusion[i][k]
    return grille


def n_repetition(liste):
    compteur = 0
    B = [False for _ in range(len(liste))]
    for i in range(len(liste)):
        if B[liste[i] - 1]:
            compteur += 1
        B[liste[i] - 1] = True
    return compteur


class Sudoku:
    def __init__(self, valeurs_initiales):
        self.liste = valeurs_initiales
        ligne = []
        colonne = []
        for i in range(9):
            L1 = []
            L2 = []
            for j in range(9):
                L1.append(self.liste[j + 9 * i])
                L2.append(self.liste[i + 9 * j])
            ligne.append(L1)
            colonne.append(L2)
        self.ligne = ligne
        self.colonne = colonne
        blocs = [[] for i in range(9)]
        valeurs_fixes = []
        for i in range(81):
            c = self.liste[i]
            ligne = i // 9
            col = i % 9
            bloc = (ligne // 3) * 3 + (col // 3)
            blocs[bloc].append(c)
            if c != 0:
                valeurs_fixes.append(i)
        self.bloc = blocs
        self.valeurs_fixes = valeurs_fixes

    def maj(self):
        grille = [0 for _ in range(81)]
        for i in range(9):
            ligne_départ = (i // 3) * 3
            collone_départ = (i % 3) * 3
            for k in range(9):
                ligne = ligne_départ + k // 3
                col = collone_départ + k % 3
                indice = ligne * 9 + col
                grille[indice] = self.bloc[i][k]
        self.liste = grille

    def remplissage_aléatoire(self):
        for i in range(9):
            B = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(9):
                if self.bloc[i][j] == 0:
                    c = choice(B)
                    while c in self.bloc[i]:
                        c = choice(B)
                    B.remove(c)
                    self.bloc[i][j] = c
        self.maj()

    def fitness(self):
        compteur = 0
        for i in range(9):
            a = n_repetition(self.ligne[i])
            b = n_repetition(self.colonne[i])
            res = a + b
            compteur += res
        return compteur

    def mutation(self, taux):
        for _ in range(int(taux * 81)):
            bloc = randint(0, 8)
            c1 = randint(0, 8)
            c2 = randint(0, 8)
            while c2 == c1:
                c2 = randint(0, 8)
            self.bloc[bloc][c1], self.bloc[bloc][c2] = (
                self.bloc[bloc][c2],
                self.bloc[bloc][c1],
            )
            self.maj()
