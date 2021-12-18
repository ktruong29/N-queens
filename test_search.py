from search import *
import pygame

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
    print(test_genetic_algorithm(5))

    # * BELOW * Future implementation of automatic 2d array approach for graphics processing
    # We went with a simpler approach to generate graphics, but has to be configured manually every time

    # testBoard = test_genetic_algorithm(5)  # creates 1d array of queens positions

    pygame.init()
    tile = 50  # tile size in pixels

    # number_of_rows = len(testBoard)
    # number_of_columns = len(testBoard)
    # arr_2d = []
    # for x in range(number_of_rows):
    #    column_elements = []
    #    for y in range(number_of_columns):
    #        column_elements.append(0)
    #    arr_2d.append(column_elements)
    # print(arr_2d)  # creates 2d array

    gameBoard = [ # hard coded 5 queens solution
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0],
    ]
    (width, height) = (len(gameBoard[1]) * tile, len(gameBoard) * tile)
    window = pygame.display.set_mode((width, height))
    pygame.display.flip()


    def makeBoard():
        window.fill((0, 0, 0))

        for i in range(len(gameBoard)):
            for j in range(len(gameBoard[0])):
                if gameBoard[i][j] == 0:
                    pygame.draw.rect(window, (255, 255, 255), (j * tile, i * tile, tile, tile))
                elif gameBoard[i][j] == 1:
                    pygame.draw.rect(window, (0, 0, 0), (j * tile, i * tile, tile, tile))

        pygame.draw.line(window, (0, 0, 0), (50, 0), (50, 1000))
        pygame.draw.line(window, (0, 0, 0), (100, 0), (100, 1000))
        pygame.draw.line(window, (0, 0, 0), (150, 0), (150, 1000))
        pygame.draw.line(window, (0, 0, 0), (200, 0), (200, 1000))
        pygame.draw.line(window, (0, 0, 0), (250, 0), (250, 1000))
        pygame.draw.line(window, (0, 0, 0), (300, 0), (300, 1000))

        pygame.draw.line(window, (0, 0, 0), (0, 50), (1000, 50))
        pygame.draw.line(window, (0, 0, 0), (0, 100), (1000, 100))
        pygame.draw.line(window, (0, 0, 0), (0, 150), (1000, 150))
        pygame.draw.line(window, (0, 0, 0), (0, 200), (1000, 200))
        pygame.draw.line(window, (0, 0, 0), (0, 250), (1000, 250))
        pygame.draw.line(window, (0, 0, 0), (0, 300), (1000, 300))
        pygame.display.update()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False  # quit on key stroke q

        makeBoard()
