from sudoku import Sudoku, fusion_blocs
from random import choice


class SudokuGA:
    def __init__(
        self,
        pop_taille,
        taux_conservation,
        nb_enfant,
        max_nb_generation,
        taux_mutation,
        liste
    ):
        self.pop_taille = pop_taille
        self.pop = [Sudoku(liste) for _ in range(self.pop_taille)]
        self.taux_conservation = taux_conservation
        self.nb_enfant = nb_enfant
        self.max_nb_generation = max_nb_generation
        self.taux_mutation = taux_mutation

    def genere_pop(self):
        for i in range(self.pop_taille):
            self.pop[i].remplissage_aléatoire()

    def trier_par_fitness(self):
        for i in range(self.pop_taille):
            min_index = i
            for j in range(i + 1, self.pop_taille):
                if self.pop[j].fitness() < self.pop[min_index].fitness():
                    min_index = j
            self.pop[i], self.pop[min_index] = self.pop[min_index], self.pop[i]

    def selection_parents(self):
        parents = []
        for i in range(int(self.taux_conservation * self.pop_taille)):
            parents.append(self.pop[i])
        return parents

    def genere_nouvelle_pop(self, parents):
        nouvelle_pop = []
        for _ in range(len(parents)):
            père = choice(parents)
            mère = choice(parents)
            for _ in range(self.nb_enfant):
                L = fusion_blocs(père.bloc, mère.bloc)
                nouvelle_pop.append(Sudoku(L))
        self.pop = nouvelle_pop

    def faire_muter(self):
        for i in range(self.pop_taille):
            self.pop[i].mutation(self.taux_mutation)

    def est_une_solution(self):
        verif = self.pop[0].fitness() == 0
        return verif
