import mixed_algorithms as mixedalg
import pure_algorithms as purealg
import tools

print("Veuillez entrer le nombre de troupes")
troops_number = int(input()) # nombre de troupes

matrix = tools.create_matrix(troops_number)
strategies = tools.generate_strategies(troops_number)
while(True):
    print("Voici la matrice des strategies:\n")
    print(strategies)
    print()
    for row in range(len(matrix)):
        print(matrix[row])
    print("Choisiser une operation a executer:\n")
    print("1. Elimination des strategies faiblement dominees.\n")
    print("2. Elimination des strategies strictement dominees.\n")
    print("3. Calculer l'equilibre de Nash pure.\n")
    print("4. Calculer les profiles securisees.\n")
    print("5. Calculer l'optimum de pareto.\n")
    print("6. Calculer l'equilibre de Nash mixte. (Methode classique) !! NE FONCTIONNE PAS !!\n")
    print("7. Calculer l'equilibre de Nash mixte. (Algorithm SIMPLEX)\n")
    choice = int(input())
    if choice == 1 :
        purealg.weakly_dominated_strategies(matrix, strategies)
    elif choice == 2 :
        purealg.strictly_dominated_strategies(matrix, strategies)
    elif choice == 3 :
        purealg.pure_nash(matrix, strategies)
    elif choice == 4 :
        purealg.safe_profiles(matrix, strategies)
    elif choice == 5 :
        purealg.optimum_pareto(matrix)
    elif choice == 6 :
        mixedalg.mixed_nash_P1(matrix)
        mixedalg.mixed_nash_P2(matrix)
    elif choice == 7 :
        mixedalg.mixed_nash_simplex(matrix, strategies)
