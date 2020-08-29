import mixed_algorithms as mixedalg
import pure_algorithms as purealg
import tools

maxTroops = 7
matrix = tools.create_matrix(maxTroops)
strategies = tools.generate_strategies(maxTroops)

purealg.weakly_dominated_strategies(matrix, strategies)
purealg.strictly_dominated_strategies(matrix, strategies)
purealg.pure_nash(matrix, strategies)
purealg.safe_profiles(matrix, strategies)
purealg.optimum_pareto(matrix)

mixedalg.mixed_nash_P1(matrix)
mixedalg.mixed_nash_P2(matrix)
