import numpy
from scipy.optimize import linprog

from tools import get_player_matrix, get_tuple_matrix

numpy.set_printoptions(linewidth=numpy.inf)

#Calculates mixed Nash equilibrium for Player 1
def mixed_nash_P1(matrix):
    # separate the main matrix to 2 different matrices for the ease of calculation
    matrix1 = get_player_matrix(matrix, 1)
    matrix2 = get_player_matrix(matrix, 2)

    # the matrix which will contain the system of linear equations
    equations = numpy.ones((len(matrix[0]), len(matrix[0])), dtype='i')
    # last line of the matrix contains the sigmas (sum of possibilities) sum = 1

    # k is the index used in the equations matrix
    k = 0
    # loop player 2 matrix to extract independent linear equations
    for i in range(len(matrix[0])-1):
        if k is len(matrix[0])-1:
            break
        result = numpy.subtract(matrix2[:,[i]], matrix2[:,[i+1]])
        equations[[k],:] = result[:, None].T
        k += 1

    # add the vector of coefficient to solve the matrix
    sigmaArray = numpy.zeros((len(matrix[0])))
    sigmaArray[-1] = 1 # sum of possibilities = 1
    print(numpy.linalg.solve(equations, sigmaArray))


#Calculate mixed Nash equilibrium for Player 2
def mixed_nash_P2(matrix):
    # separate the main matrix to 2 different matrices for the ease of calculation
    matrix1 = get_player_matrix(matrix, 1)
    matrix2 = get_player_matrix(matrix, 2)

    # the matrix which will contain the system of linear equations
    equations = numpy.ones((len(matrix), len(matrix)), dtype='i')
    # last line of the matrix contains the sigmas (sum of possibilities) sum = 1

    # k is the index used in the equations matrix
    k = 0
    for i in range(len(matrix)-1):
        if k is len(matrix)-1:
            break
        equations[[k],:] = numpy.subtract(matrix1[[i],:], matrix1[[i+1],:])
        k += 1

    # add the vector of coefficient to solve the matrix
    sigmaArray = numpy.zeros((len(matrix)))
    sigmaArray[-1] = 1 # sum of possibilities = 1
    print(numpy.linalg.solve(equations, sigmaArray))


# Calculer l'equilibre de Nash mixte avec l'algorithm SIMPLEX
def mixed_nash_simplex(matrix, strategies):
    matrix1 = get_player_matrix(matrix, 1)
    A = numpy.zeros((len(matrix)+2, len(matrix)+1), dtype='i')
    for row in range(len(matrix1)):
        for col in range(len(matrix1)):
            A[row,col] = matrix1[row,col]
    temp = numpy.ones(len(matrix)+1)
    temp[-1] = 0
    A[[len(matrix)],:] = temp
    A[[len(matrix)+1],:] = temp*-1
    temp = numpy.ones(len(matrix)+2)
    temp[-1] = 0
    temp[-2] = 0
    temp = temp.T
    A[:,len(matrix)] = temp

    b = numpy.zeros(len(matrix)+2)
    b[-2] = 1
    b[-1] = -1
    c = numpy.zeros(len(matrix)+1)
    c[0] = 1

    result = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    print(strategies)
    print('Optimal value:', result.fun, '\nX:', result.x)
