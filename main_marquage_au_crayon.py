from marquage_au_crayon import MarquageAuCrayon
from sudoku import Sudoku
from résolution_exhaustif import lignes_compatibles, liste_to_matrice
from support import l3

s = Sudoku(l3)
m = MarquageAuCrayon(s)

while not lignes_compatibles(liste_to_matrice(s.liste)):
    m.marquage()

print(s.liste)
