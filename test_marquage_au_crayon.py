from marquage_au_crayon import MarquageAuCrayon
from sudoku import Sudoku
from test_sudoku import liste1

# dico = {i: [True for _ in range(9)] for i in range(5)}
# print(dico)
# dico[4][5] = False
# print(dico)


def test_init():
    s = Sudoku(liste1)
    m = MarquageAuCrayon(s)
    assert m.bools[0] == [
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
    ]
    assert m.bools[25] == [
        False,
        True,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
    ]


def test_marquage():
    s = Sudoku(liste1)
    m = MarquageAuCrayon(s)
    assert m.bools[25] == [
        False,
        True,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
    ]
