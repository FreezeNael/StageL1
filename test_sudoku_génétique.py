from sudoku_génétique import SudokuGA
from support import l3, l2
from résolution_exhaustif import occurence


def test_genere_pop():
    sga = SudokuGA(50, 0.25, 4, 50, 0.1, l3)
    sga.genere_pop()
    for i in range(sga.pop_taille):
        for j in range(81):
            assert 1 <= sga.pop[i].liste[j] <= 9


def test_trier():
    sga = SudokuGA(50, 0.25, 4, 50, 0.1, l3)
    sga.genere_pop()
    sga.trier_par_fitness()
    for i in range(1, sga.pop_taille):
        assert sga.pop[i - 1].fitness() <= sga.pop[i].fitness()


def test_genere_nouvelle_pop():
    sga = SudokuGA(50, 0.2, 5, 50, 0.1, l3)
    sga.genere_pop()
    sga.trier_par_fitness()
    parents = sga.selection_parents()
    sga.genere_nouvelle_pop(parents)
    assert len(sga.pop) == sga.pop_taille


def test_faire_muter():
    sga = SudokuGA(50, 0.2, 5, 50, 0.1, l3)
    sga.genere_pop()
    sga.trier_par_fitness()
    parents = sga.selection_parents()
    sga.genere_nouvelle_pop(parents)
    sga.faire_muter()
    for i in range(sga.pop_taille):
        for j in range(9):
            for e in range(9):
                assert occurence(sga.pop[i].bloc[j], sga.pop[i].bloc[j][e]) == 1


def test_est_une_solution():
    sga = SudokuGA(50, 0.2, 5, 50, 0.1, l2)
    assert sga.est_une_solution()
