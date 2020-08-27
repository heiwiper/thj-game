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
        elif(s11<s21):
            gain2+=1

        if(s12>s22):
            gain1+=1
        elif(s12<s22):
            gain2+=1

        if(s13>s23):
            gain1+=1
        elif(s13<s23):
            gain2+=1

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
