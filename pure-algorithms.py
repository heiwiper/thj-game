import copy

import numpy

numpy.set_printoptions(linewidth=numpy.inf)

print("Veuillez entrer le nombre de troupes")
# s = int(input()) # nombre de troupes
max_troops = 2
max_battlefields = 3 # nombre de champ de batailles
strategies = [] # toutes les strategies possibles

for i in range(max_troops+1):
    first_troops = i
    for j in range(max_troops-i+1):
        second_troops = j
        third_troops = max_troops - (i+j)
        strategies.append((first_troops, second_troops, third_troops))

# Affichage des strategies
print("Liste des strategies possibles :")
for i in range(len(strategies)):
    print(strategies[i])

len_strategies = len(strategies)

class Player:
    def __init__(self):
        self.matrix = numpy.zeros((len_strategies, len_strategies), dtype='i')
        self.strategies = strategies
        self.first_troops = 0
        self.second_troops = 0
        self.third_troops = 0
    def print(self):
        print(self.matrix)
        print()


player1 = Player()
player2 = Player()

# Remplissage de la matrice de chaque joueur
for i in range(len_strategies):
    for j in range(len_strategies):
        gain1 = 0
        gain2 = 0
        player1.first_troops = strategies[i][0]
        player1.second_troops = strategies[i][1]
        player1.third_troops = strategies[i][2]
        player2.first_troops = strategies[j][0]
        player2.second_troops = strategies[j][1]
        player2.third_troops = strategies[j][2]

        if(player1.first_troops > player2.first_troops):
            gain1 += 1
            gain2 -= 1
        elif(player1.first_troops < player2.first_troops):
            gain1 -= 1
            gain2 += 1

        if(player1.second_troops > player2.second_troops):
            gain1 += 1
            gain2 -= 1
        elif(player1.second_troops < player2.second_troops):
            gain1 -= 1
            gain2 += 1

        if(player1.third_troops > player2.third_troops):
            gain1 += 1
            gain2 -= 1
        elif(player1.third_troops < player2.third_troops):
            gain1 -= 1
            gain2 += 1

        player1.matrix[i, j] = gain1
        player2.matrix[i, j] = gain2

player1.print()
player2.print()

def delete_strictly_dominated_strategies(player1, player2):
    # creer des copies
    temp_player1 = copy.deepcopy(player1)
    temp_player2 = copy.deepcopy(player2)

    no_dominated_strategy = False
    while no_dominated_strategy is False:
        no_dominated_strategy = True
        print("Player 1 strictly dominated strategies are:")
        for i in range(len(temp_player1.strategies)):
            for j in range(len(temp_player1.strategies)):
                if i is not j:
                    weakly_dominated = True
                    x = 0;
                    while weakly_dominated is True and x < len(temp_player2.strategies):
                        if temp_player1.matrix[i, x] >= temp_player1.matrix[j, x]:
                            weakly_dominated = False
                        x += 1
                    if weakly_dominated is True:
                        print("{} is strictly dominated by {}".format(temp_player1.strategies[i], temp_player1.strategies[j]))
                        no_dominated_strategy = False
                        temp_player1.matrix = numpy.delete(temp_player1.matrix, i, axis=0)
                        temp_player2.matrix = numpy.delete(temp_player2.matrix, i, axis=0)
                        del temp_player1.strategies[i]
                        break
            if weakly_dominated is True:
                break

        print("Player 2 strictly dominated strategies are:")
        for i in range(len(temp_player2.strategies)):
            for j in range(len(temp_player2.strategies)):
                if i is not j:
                    weakly_dominated = True
                    x = 0;
                    while weakly_dominated is True and x < len(temp_player1.strategies):
                        if temp_player2.matrix[x, i] >= temp_player2.matrix[x, j]:
                            weakly_dominated = False
                        x += 1
                    if weakly_dominated is True:
                        print("{} is strictly dominated by {}".format(temp_player2.strategies[i], temp_player2.strategies[j]))
                        no_dominated_strategy = False
                        temp_player1.matrix = numpy.delete(temp_player1.matrix, i, axis=1)
                        temp_player2.matrix = numpy.delete(temp_player2.matrix, i, axis=1)
                        del temp_player2.strategies[i]
                        break
            if weakly_dominated is True:
                break
    print("Matrix after eliminating strictly dominated strategies")
    temp_player1.print()
    temp_player2.print()

def delete_weakly_dominated_strategies(player1, player2):
    #creer des copies
    temp_player1 = copy.deepcopy(player1)
    temp_player2 = copy.deepcopy(player2)

    no_dominated_strategy = False
    while no_dominated_strategy is False:
        no_dominated_strategy = True
        print("Player 1 dominated strategies are:")
        for i in range(len(temp_player1.strategies)):
            for j in range(len(temp_player1.strategies)):
                if i is not j:
                    weakly_dominated = True
                    x = 0;
                    while weakly_dominated is True and x < len(temp_player2.strategies):
                        if temp_player1.matrix[i, x] > temp_player1.matrix[j, x]:
                            weakly_dominated = False
                        x += 1
                    if weakly_dominated is True:
                        print("{} is weakly dominated by {}".format(temp_player1.strategies[i], temp_player1.strategies[j]))
                        no_dominated_strategy = False
                        temp_player1.matrix = numpy.delete(temp_player1.matrix, i, axis=0)
                        temp_player2.matrix = numpy.delete(temp_player2.matrix, i, axis=0)
                        del temp_player1.strategies[i]
                        break
            if weakly_dominated is True:
                break

        print("Player 2 dominated strategies are:")
        for i in range(len(temp_player2.strategies)):
            for j in range(len(temp_player2.strategies)):
                if i is not j:
                    weakly_dominated = True
                    x = 0;
                    while weakly_dominated is True and x < len(temp_player1.strategies):
                        if temp_player2.matrix[x, i] > temp_player2.matrix[x, j]:
                            weakly_dominated = False
                        x += 1
                    if weakly_dominated is True:
                        print("{} is weakly dominated by {}".format(temp_player2.strategies[i], temp_player2.strategies[j]))
                        no_dominated_strategy = False
                        temp_player1.matrix = numpy.delete(temp_player1.matrix, i, axis=1)
                        temp_player2.matrix = numpy.delete(temp_player2.matrix, i, axis=1)
                        del temp_player2.strategies[i]
                        break
            if weakly_dominated is True:
                break
        print("Matrix after eliminating weakly dominated strategies")
        temp_player1.print()
        temp_player2.print()

delete_strictly_dominated_strategies(player1, player2)
delete_weakly_dominated_strategies(player1, player2)
