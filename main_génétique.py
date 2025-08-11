from sudoku_génétique import SudokuGA
from sudoku import Sudoku
from résolution_exhaustif import liste_to_matrice, lignes_compatibles
from support import l3
from marquage_au_crayon import MarquageAuCrayon

s = Sudoku(l3)
m = MarquageAuCrayon(s)
i = 0
while not lignes_compatibles(liste_to_matrice(s.liste)) and i < 200:
    m.marquage()
    i += 1

if lignes_compatibles(liste_to_matrice(s.liste)):
    print("la solution a été trouvé par le marqueur au crayon, c'est la suivante :", s.liste)
else:
    sga = SudokuGA(5000, 0.1, 10, 50, 0.25, l3)
    sga.genere_pop()
    j = 0
    while not sga.est_une_solution() and j < sga.max_nb_generation:
        sga.trier_par_fitness()
        futur_parents = sga.selection_parents()
        sga.genere_nouvelle_pop(futur_parents)
        sga.faire_muter()
        j += 1
    if sga.est_une_solution():
        print("c'est la solution")
        print("c'est la solution :", liste_to_matrice(sga.pop[0].liste))
    else:
        print(
            "après",
            j,
            "générations, le meilleur être est",
            liste_to_matrice(sga.pop[0].liste),
        )

    print("le fitness est de : ", sga.pop[0].fitness())
