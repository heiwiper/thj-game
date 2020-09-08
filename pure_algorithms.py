import copy

import numpy

from tools import (create_matrix, generate_strategies, get_player_matrix,
                   get_tuple_matrix)

numpy.set_printoptions(linewidth=numpy.inf)


def strictly_dominated_strategies(matrix, strategies):
    matrix1 = get_player_matrix(matrix, 1)
    matrix2 = get_player_matrix(matrix, 2)
    strategies1 = copy.deepcopy(strategies)
    strategies2 = copy.deepcopy(strategies)

    no_dominated_strategy = False
    while no_dominated_strategy is False:
        no_dominated_strategy = True
        print("Player 1 strictly dominated strategies are:")
        for i in range(len(matrix1)):
            for j in range(len(matrix1)):
                if i is not j:
                    strictly_dominated = True
                    x = 0;
                    while strictly_dominated is True and x < len(matrix2[0]):
                        if matrix1[i, x] >= matrix1[j, x]:
                            strictly_dominated = False
                        x += 1
                    if strictly_dominated is True:
                        print("{} is strictly dominated by {}".format(strategies1[i], strategies1[j]))
                        no_dominated_strategy = False
                        matrix1 = numpy.delete(matrix1, i, axis=0)
                        matrix2 = numpy.delete(matrix2, i, axis=0)
                        del strategies1[i]
                        break
            if strictly_dominated is True:
                break

        print("Player 2 strictly dominated strategies are:")
        for i in range(len(matrix2[0])):
            for j in range(len(matrix2[0])):
                if i is not j:
                    strictly_dominated = True
                    x = 0;
                    while strictly_dominated is True and x < len(matrix1):
                        if matrix2[x, i] >= matrix2[x, j]:
                            strictly_dominated = False
                        x += 1
                    if strictly_dominated is True:
                        print("{} is strictly dominated by {}".format(strategies2[i], strategies2[j]))
                        no_dominated_strategy = False
                        matrix1 = numpy.delete(matrix1, i, axis=1)
                        matrix2 = numpy.delete(matrix2, i, axis=1)
                        del strategies2[i]
                        break
            if strictly_dominated is True:
                break
    print("Strategies and matrix after eliminating strictly dominated strategies")
    print("Player 1 strategies:")
    print(strategies1)
    print("Player 2 strategies:")
    print(strategies2)
    print()
    m = get_tuple_matrix(matrix1, matrix2)
    for i in range(len(m)):
        print(m[i])

def weakly_dominated_strategies(matrix, strategies):
    matrix1 = get_player_matrix(matrix, 1)
    matrix2 = get_player_matrix(matrix, 2)
    strategies1 = copy.deepcopy(strategies)
    strategies2 = copy.deepcopy(strategies)

    no_dominated_strategy = False
    while no_dominated_strategy is False:
        no_dominated_strategy = True
        print("Player 1 weakly dominated strategies are:")
        for i in range(len(matrix1)):
            for j in range(len(matrix1)):
                if i is not j:
                    weakly_dominated = True
                    x = 0;
                    while weakly_dominated is True and x < len(matrix2[0]):
                        if matrix1[i, x] > matrix1[j, x]:
                            weakly_dominated = False
                        x += 1
                    if weakly_dominated is True:
                        print("{} is weakly dominated by {}".format(strategies1[i], strategies1[j]))
                        no_dominated_strategy = False
                        matrix1 = numpy.delete(matrix1, i, axis=0)
                        matrix2 = numpy.delete(matrix2, i, axis=0)
                        del strategies1[i]
                        break
            if weakly_dominated is True:
                break

        print("Player 2 weakly dominated strategies are:")
        for i in range(len(matrix2[0])):
            for j in range(len(matrix2[0])):
                if i is not j:
                    weakly_dominated = True
                    x = 0;
                    while weakly_dominated is True and x < len(matrix1):
                        if matrix2[x, i] > matrix2[x, j]:
                            weakly_dominated = False
                        x += 1
                    if weakly_dominated is True:
                        print("{} is weakly dominated by {}".format(strategies2[i], strategies2[j]))
                        no_dominated_strategy = False
                        matrix1 = numpy.delete(matrix1, i, axis=1)
                        matrix2 = numpy.delete(matrix2, i, axis=1)
                        del strategies2[i]
                        break
            if weakly_dominated is True:
                break
    print("Strategies and matrix after eliminating weakly dominated strategies")
    print("Player 1 strategies:")
    print(strategies1)
    print("Player 2 strategies:")
    print(strategies2)
    print()
    m = get_tuple_matrix(matrix1, matrix2)
    for i in range(len(m)):
        print(m[i])


def pure_nash(matrix, strategies):
    # recherche de l'equilibre de nash
    br1 = [] # meilleur reponse pour le joueur 1
    br2 = [] # meilleur reponse pour le joueur 2

    # recherches des meilleurs reponses pour le joueur 2
    for i in range(len(strategies)):
        max = 0
        for j in range(len(strategies)):
            if(max<matrix[i][j][1]):
                max = matrix[i][j][1]
        for j in range(len(strategies)):
            if(matrix[i][j][1] == max):
                br1.append((strategies[i],strategies[j]))

    # recherches des meilleurs reponses pour le joueur 1
    for j in range(len(strategies)):
        max = 0
        for i in range(len(strategies)):
            if(max<matrix[i][j][0]):
                max = matrix[i][j][0]
        for i in range(len(strategies)):
            if(matrix[i][j][0] == max):
                br2.append((strategies[i], strategies[j]))

    print("L'equilibre de nash :")
    print( set(br1) & set(br2) )


def safe_strategies(matrix, strategies, player):
    if player == 1:
        player = 0
    elif player == 2:
        player = 1
    safeStrategies = [] # strategies securisees

    # recherche des strategies securisees du joueur 1
    minimum = [] # le minimum que le joueur risque d'avoir dans chaque cas (x, min)
    for i in range(len(strategies)):
        min = 0
        for j in range(len(strategies)):
            if (min>matrix[i][j][player]):
                min = matrix[i][j][player]
        minimum.append((strategies[i], min))
    # recherche du maximum qu'il peut avoir
    max = 0
    for i in range(len(minimum)):
        if(max < minimum[i][1]):
            max = minimum[i][1]
    for i in range(len(minimum)):
        if( max == minimum[i][1]):
            safeStrategies.append(minimum[i][0])
    print("Les strategies securisees du joueur {} : ".format(player+1))
    print(safeStrategies)
    return safeStrategies


def safe_profiles(matrix, strategies):
    # recherche des profils securises
    safeProfiles = [] # profils securises
    safeStrategies1 = safe_strategies(matrix, strategies, 1)
    safeStrategies2 = safe_strategies(matrix, strategies, 2)
    for i in range(len(safeStrategies1)):
        for j in range(len(safeStrategies2)):
            safeProfiles.append((safeStrategies1[i], safeStrategies2[j]))

    print("Les profils securises :")
    print(safeProfiles)


# recherche de l'optimum de pareto
def optimum_pareto(matrix):
    optimums_pareto = []
    def first_optimum_pareto(optimums_pareto):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                value = matrix[i][j]
                is_optimum_pareto = True
                ii = 0
                jj = 0
                while ii <len(matrix) and is_optimum_pareto == True:
                    while jj < len(matrix) and is_optimum_pareto == True:
                        if (value[0] >= matrix[ii][jj][0] and value[1]>=matrix[ii][jj][1])== False:
                            is_optimum_pareto = False
                        jj+=1
                    ii+=1
                if(is_optimum_pareto):
                    optimums_pareto.append((i,j))
                    return

    def search_optimum_pareto(optimums_pareto):
        first_optimum_pareto(optimums_pareto)
        if optimums_pareto!=[]:
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    x = optimums_pareto[0][0]
                    y = optimums_pareto[0][1]
                    if( (i==x and j==y)==False  ):
                        if matrix[i][j][0] == matrix[x][y][0] and matrix[i][j][1] == matrix[x][y][1]:
                            optimums_pareto.append((i,j))

    search_optimum_pareto(optimums_pareto)
    print("optimum de pareto :")
    print(optimums_pareto)


    print("pareto dominance :")
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for x in range(len(matrix)):
                for y in range(len(matrix)):
                    if (matrix[i][j][0] >= matrix[x][y][0] and matrix[i][j][1] >= matrix[x][y][1]) and (matrix[i][j][0] > matrix[x][y][0] or matrix[i][j][1] > matrix[x][y][1]):
                        print("(",i,",",j,") >","(",x,",",y,")")
                    elif (matrix[i][j][0] <= matrix[x][y][0] and matrix[i][j][1] <= matrix[x][y][1]) and (matrix[i][j][0] < matrix[x][y][0] or matrix[i][j][1] < matrix[x][y][1]):
                        print("(",i,",",j,") <","(",x,",",y,")")
