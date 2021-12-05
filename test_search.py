from search import *

'''
--------------------------------------------------------------
Generic algorithm approach
--------------------------------------------------------------
1. INITIAL POPULATION
    - Randomly generate a set of k states (initial population)
2. FITNESS FUNCTION
    - Each state is rated by the objective function (fitness function) and return the least number
      of attacking pairs within the population.
3. SELECTION
    - For the reproduction stage, each pair is randomly selected based on the probabilities returned 
      by the fitness function.
4. CROSSOVER
    - For each pair, a crossover point is chosen randomly
5. MUTATION
    - Randomly mutate an element within a state
'''
def test_genetic_algorithm(n):
    # Queens Problem
    gene_pool = range(n)

    '''
    1. INITIAL POPULATION
        o- Return a list (vector) of randomly generate k states (initial population) 
    '''
    population = init_population(100, gene_pool, n)

    '''
    2. FITNESS FUNCTION
        o- Return non_attacking pairs
    '''
    def fitness(q):
        non_attacking = 0
        for row1 in range(len(q)):
            for row2 in range(row1 + 1, len(q)):
                col1 = int(q[row1])
                col2 = int(q[row2])
                row_diff = row1 - row2
                col_diff = col1 - col2

                if col1 != col2 and row_diff != col_diff and row_diff != -col_diff:
                    non_attacking += 1
        return non_attacking

    solution = genetic_algorithm(population, fitness, gene_pool=gene_pool, f_thres=25)
    return solution


if __name__ == '__main__':
    print(test_genetic_algorithm(4))
