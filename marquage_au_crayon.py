class MarquageAuCrayon:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.bools = [[True for _ in range(9)] for i in range(81)]
        for i in range(81):
            val = self.sudoku.liste[i]
            if val != 0:
                ligne = i // 9
                col = i % 9
                bloc_ligne = (ligne // 3) * 3
                bloc_col = (col // 3) * 3

                for j in range(9):
                    self.bools[ligne * 9 + j][val - 1] = False

                for j in range(9):
                    self.bools[j * 9 + col][val - 1] = False

                for r in range(3):
                    for c in range(3):
                        index = (bloc_ligne + r) * 9 + (bloc_col + c)
                        self.bools[index][val - 1] = False

                self.bools[i] = [False] * 9
                self.bools[i][val - 1] = True

    def marquage(self):
        for i in range(81):
            compteur = 0
            L = []
            for j in range(9):
                if self.bools[i][j]:
                    compteur += 1
                    L.append(j)
            if compteur == 1:
                self.sudoku.liste[i] = L[0] + 1
                ligne = i // 9
                col = i % 9
                bloc_ligne = (ligne // 3) * 3
                bloc_col = (col // 3) * 3

                # ligne
                for j in range(9):
                    self.bools[ligne * 9 + j][L[0]] = False

                # colonne
                for j in range(9):
                    self.bools[j * 9 + col][L[0]] = False

                # bloc
                for r in range(3):
                    for c in range(3):
                        index = (bloc_ligne + r) * 9 + (bloc_col + c)
                        self.bools[index][L[0]] = False

                # La case elle-même n'autorise que sa valeur
                self.bools[i] = [False] * 9
                self.bools[i][L[0]] = True
