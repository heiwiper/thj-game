import numpy


def create_matrix(maxTroops):
    strategies = generate_strategies(maxTroops)
    # construction de la matrice de jeu
    matrix = []
    for i in range(len(strategies)):
        list2 = []
        for j in range(len(strategies)):
            gain1 = 0  # nombre de gain du premier joueur
            gain2 = 0  # nombre de gain du second joueur
            firstTroopsP1 = strategies[i][0]
            secondTroopsP1 = strategies[i][1]
            thirdTroopsP1 = strategies[i][2]
            firstTroopsP2 = strategies[j][0]
            secondTroopsP2 = strategies[j][1]
            thirdTroopsP2 = strategies[j][2]

            if(firstTroopsP1 > firstTroopsP2):
                gain1 += 1
                gain2 -= 1
            elif(firstTroopsP1 < firstTroopsP2):
                gain1 -= 1
                gain2 += 1

            if(secondTroopsP1 > secondTroopsP2):
                gain1 += 1
                gain2 -= 1
            elif(secondTroopsP1 < secondTroopsP2):
                gain1 -= 1
                gain2 += 1

            if(thirdTroopsP1 > thirdTroopsP2):
                gain1 += 1
                gain2 -= 1
            elif(thirdTroopsP1 < thirdTroopsP2):
                gain1 -= 1
                gain2 += 1
            list2.append((gain1, gain2))
        matrix.append(list2)
    for i in range(len(matrix)):
        print(matrix[i])
    return matrix


# generer toures les strategies possibles
def generate_strategies(maxTroops):
    strategies = []  # les strategies possibles
    for i in range(maxTroops+1):
        firstTroops = i
        for j in range(maxTroops-i+1):
            secondTroops = j
            thirdTroops = maxTroops - (i+j)
            strategies.append((firstTroops, secondTroops, thirdTroops))

    # Affichage des strategies
    print("Liste des strategies possibles :")
    for i in range(len(strategies)):
        print(strategies[i])
    return strategies


# transform tuple matrix to two matrices
def get_player_matrix(matrix, player):
    if player == 1:
        player = 0
    else:
        player = 1
    matrixPlayer = numpy.zeros((len(matrix), len(matrix[0])), dtype='i')
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrixPlayer[r, c] = matrix[r][c][player]
    return matrixPlayer


#  transform two players matrices to tuple matrix
def get_tuple_matrix(matrix1, matrix2):
    matrix = []
    for r in range(len(matrix1)):
        tempList = []
        for c in range(len(matrix1[r])):
            tempList.append((matrix1[r, c], matrix2[r, c]))
        matrix.append(tempList)
    for i in range(len(matrix)):
        print(matrix[i])
    return matrix
