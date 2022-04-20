import numpy as np

class Individuo: 

    def __init__(self, chromosome = False ) -> None:
        self.chromosome = self.generate_chromosome() if not chromosome else chromosome
        self.fitness = 0

    def generate_chromosome(self) -> list:
        ''' Generate matriz 8X8 with 8 Queens, [1] - Queen '''
        random_chromosome = np.zeros(shape=(8,8),dtype=np.int64)
        coordinates = []
        while len(coordinates) < 8:
            x_coordinate, y_coordinate = np.random.randint(8, size=(2))
            random_cordinate = (x_coordinate, y_coordinate)
            if random_cordinate not in coordinates:
                coordinates.append(random_cordinate)
        
        for coordinate in coordinates:
            random_chromosome[coordinate[0]][coordinate[1]] = 1

        return random_chromosome

    def copy(self):
        temporary_individuo = Individuo(self.chromosome)
        temporary_individuo.fitness = self.fitness
        return temporary_individuo

    def __repr__(self) -> str:
        return f'chromossome:\n{self.chromosome}'