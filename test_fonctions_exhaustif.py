from résolution_exhaustif import (
    lignes_compatibles,
    genere_ligne,
    occurence,
)


def test_lignes_compatibles():
    grille1 = [
        [1, 2, 5, 9, 7, 3, 6, 4, 8],
        [6, 3, 4, 5, 1, 8, 2, 9, 7],
        [7, 9, 8, 2, 6, 4, 1, 3, 5],
    ]
    grille2 = [
        [8, 7, 5, 6, 9, 4, 3, 2, 1],
        [5, 1, 6, 9, 4, 2, 8, 3, 7],
        [6, 3, 7, 5, 2, 9, 1, 4, 8],
    ]
    grille3 = [
        [6, 5, 2, 7, 9, 4, 8, 3, 1],
        [9, 1, 7, 3, 2, 8, 6, 4, 5],
        [8, 4, 3, 5, 6, 1, 7, 2, 9],
        [5, 9, 6, 1, 7, 2, 3, 8, 4],
        [1, 3, 4, 8, 5, 6, 2, 9, 7],
        [2, 7, 8, 9, 4, 3, 5, 1, 6],
        [7, 8, 1, 6, 3, 9, 4, 5, 2],
        [4, 6, 9, 2, 8, 5, 1, 7, 3],
        [3, 2, 5, 4, 1, 7, 9, 6, 8],
    ]
    grille4 = [
        [2, 7, 1, 4, 6, 8, 5, 9, 3],
        [8, 5, 9, 7, 3, 2, 4, 6, 1],
        [3, 4, 6, 9, 5, 1, 2, 7, 8],
        [6, 9, 3, 8, 4, 7, 1, 5, 2],
        [7, 8, 2, 5, 1, 3, 6, 4, 9],
        [4, 1, 5, 2, 9, 6, 3, 8, 7],
        [1, 3, 7, 6, 8, 4, 9, 2, 5],
        [9, 5, 8, 3, 2, 5, 7, 1, 4],
        [5, 2, 4, 1, 7, 9, 8, 3, 6],
    ]
    assert lignes_compatibles(grille1)
    assert not lignes_compatibles(grille2)
    assert lignes_compatibles(grille3)
    assert not lignes_compatibles(grille4)


def test_occurence():
    L = [1, 2, 4, 8, 6, 5, 3, 2]
    assert occurence(L, 1) == 1
    assert occurence(L, 2) == 2


def test_genere_ligne():
    L = genere_ligne()
    for c in L:
        assert occurence(L, c) == 1
        assert 1 <= c <= 9
