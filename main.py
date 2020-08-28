print("Veuillez entrer le nombre de troupes")
s = int(input()) # nombre de troupes
c = 3 # nombre de champ de batailles
strategies = [] # toutes les strategies possibles

for i in range(s+1):
    s1 = i
    for j in range(s-i+1):
        s2 = j
        s3 = s - (i+j)
        strategies.append((s1, s2, s3))

# Affichage des stratégies
print("Liste des stratégies possibles :")
for i in range(len(strategies)):
    print(strategies[i])

# construction de la matrice de jeu
matrix = []
for i in range(len(strategies)):
    list2 = []
    for j in range(len(strategies)):
        gain1 = 0 # nombre de gain du premier joueur
        gain2 = 0 # nombre de gain du second joueur
        s11 = strategies[i][0]
        s12 = strategies[i][1]
        s13 = strategies[i][2]
        s21 = strategies[j][0]
        s22 = strategies[j][1]
        s23 = strategies[j][2]
        if(s11>s21):
            gain1+=1
            gain2-=1
        elif(s11<s21):
            gain2+=1
            gain1-=1

        if(s12>s22):
            gain1+=1
            gain2-=1
        elif(s12<s22):
            gain2+=1
            gain1-=1
        if(s13>s23):
            gain1+=1
            gain2-=1
        elif(s13<s23):
            gain2+=1
            gain1-=1
        list2.append((gain1, gain2))
    matrix.append(list2)

# Affichage de la matrice du jeu
print("Affichage de la matrice de jeu  :")
for i in range(len(strategies)):
    for j in range(len(strategies)):
        print(matrix[i][j],end='')
    print()

# recherche de l'equilibre de nash
br1 = [] # meilleur réponse pour le joueur 1
br2 = [] # meilleur réponse pour le joueur 2

# recherches des meilleurs réponses pour le joueur 2
for i in range(len(strategies)):
    max = 0
    for j in range(len(strategies)):
        if(max<matrix[i][j][1]):
            max = matrix[i][j][1]
    for j in range(len(strategies)):
        if(matrix[i][j][1] == max):
            br1.append((strategies[i],strategies[j]))

# recherches des meilleurs réponses pour le joueur 1
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


# recherche des profils sécurisés
ps = [] # profils sécurisés
s1 = [] # stratégies sécurisées du joueur 1
s2 = [] # stratégies sécurisées du joueur 2

# recherche des stratégies sécurisées du joueur 1
minimum = [] # le minimum que le joueur risque d'avoir dans chaque cas (x, min)
for i in range(len(strategies)):
    min = 0
    for j in range(len(strategies)):
        if (min>matrix[i][j][0]):
            min = matrix[i][j][0]
    minimum.append((strategies[i], min))
# recherche du maximum qu'il peut avoir
max = 0
for i in range(len(minimum)):
    if(max < minimum[i][1]):
        max = minimum[i][1]
for i in range(len(minimum)):
    if( max == minimum[i][1]):
        s1.append(minimum[i][0])
print("Les stratégies sécurisées du joueur 1 : ")
print(s1)

# recherche des stratégies sécurisées du joueur 2
minimum = []
for j in range(len(strategies)):
    min = 0
    for i in range(len(strategies)):
        if (min>matrix[i][j][1]):
            min = matrix[i][j][1]
    minimum.append((strategies[j], min))
# recherche du maximum qu'il peut avoir
max = 0
for i in range(len(minimum)):
    if(max < minimum[i][1]):
        max = minimum[i][1]
for i in range(len(minimum)):
    if( max == minimum[i][1]):
        s2.append(minimum[i][0])
print("Les stratégies sécurisées du joueur 2 : ")
print(s2)

for i in range(len(s1)):
    for j in range(len(s2)):
        ps.append((s1[i], s2[j]))

print("Les profils sécurisés :")
print(ps)

# recherche de l'optimum de pareto
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
