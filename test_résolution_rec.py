from résolution_rec import est_valide, remplir_grille
from résolution_exhaustif import lignes_compatibles


def test_est_valide():
    grille = [[0 for i in range(9)] for j in range(9)]
    assert est_valide(grille, 0, 0, 1)
    grille1 = [
        [1, 2, 5, 9, 7, 3, 6, 4, 8],
        [6, 3, 4, 5, 1, 8, 2, 9, 7],
        [7, 9, 8, 2, 6, 4, 1, 3, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert not est_valide(grille1, 0, 2, 3)
    assert est_valide(grille1, 3, 0, 4)
    assert not est_valide(grille1, 8, 2, 5)


def test_remplir_grille():
    grille = [[0 for i in range(9)] for j in range(9)]
    remplir_grille(grille)
    assert lignes_compatibles(grille)
