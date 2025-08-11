from résolution_exhaustif import lignes_compatibles, genere_ligne

grille = [genere_ligne()]

for i in range(8):
    verif = False
    while not verif:
        grille.append(genere_ligne())
        verif = lignes_compatibles(grille)
        if not verif:
            del grille[-1]


print(grille)
