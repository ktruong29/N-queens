from search import *

n_queens = NQueensProblem(4)

def test_genetic_algorithm(n):

    # Queens Problem
    gene_pool = range(n)
    population = init_population(50, gene_pool, n)

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
