from sudoku import Sudoku, fusion_blocs
from résolution_exhaustif import occurence
from support import l1, l3, fit_50


def test_ligne():
    s = Sudoku(l3)
    assert s.ligne[0] == [0, 0, 2, 0, 9, 0, 0, 0, 0]
    assert s.ligne[2] == [8, 0, 3, 5, 6, 0, 7, 0, 9]


def test_colonne():
    s = Sudoku(l3)
    assert s.colonne[0] == [0, 9, 8, 5, 0, 0, 7, 4, 3]
    assert s.colonne[5] == [0, 0, 0, 2, 0, 0, 0, 5, 7]


def test_bloc():
    s = Sudoku(l3)
    assert s.bloc[8] == [0, 5, 2, 0, 0, 3, 0, 0, 0]
    assert s.bloc[0] == [0, 0, 2, 9, 1, 0, 8, 0, 3]


def test_valuers_fixes():
    s = Sudoku(l3)
    assert s.valeurs_fixes[(0, 2)] == 2
    assert s.valeurs_fixes[(1, 0)] == 9
    assert s.valeurs_fixes[(7, 5)] == 5


def test_maj():
    s = Sudoku(l3)
    s.maj()
    for i in range(81):
        assert l3[i] == s.liste[i]


def test_remplissage_aléatoire():
    s1 = Sudoku(l3)
    s1.remplissage_aléatoire()
    for i in range(9):
        for j in range(9):
            assert occurence(s1.bloc[i], s1.bloc[i][j]) == 1


def test_fitness():
    s1 = Sudoku(fit_50)
    s2 = Sudoku(l1)
    assert s1.fitness() == 50
    assert s2.fitness() == 0


def test_bloc_fusion():
    s1 = Sudoku(l3)
    s2 = Sudoku(fit_50)
    n_liste = fusion_blocs(s1.bloc, s2.bloc)
    for i in range(81):
        if i <= 26:
            assert n_liste[i] == s1.liste[i]
        elif i >= 51:
            assert n_liste[i] == s2.liste[i]
    assert n_liste[32] == s1.liste[32]
    assert n_liste[33] == s2.liste[33]
    assert n_liste[41] == s1.liste[41]
    assert n_liste[42] == s2.liste[42]


def test_mutation():
    s1 = Sudoku(l3)
    s1.remplissage_aléatoire()
    s1.mutation(0.25)
    for i in range(9):
        for j in range(9):
            assert occurence(s1.bloc[i], s1.bloc[i][j]) == 1
