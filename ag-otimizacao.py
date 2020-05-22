import math
import random

# Operador BLX-Alpha
alpha = 4
beta = random.uniform(-1*(alpha), 1+alpha)

# Variáveis
population_size = 20
generations = 1000
crossover_probability = 0.90
mutation_probability = 0.05

# Estatícas
num_gens = 0
num_crossovers = 0
num_mutations = 0


class Agent:
    def __init__(self):
        self.value = float(format(random.uniform(-10, 10)))
        self.fitness = -1

    def __str__(self):
        return f'Valor: {self.value}, Fitness: {self.fitness}'


def check_converged(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)


def ga():
    global num_gens
    agents = init_agents(population_size)
    for generation in range(generations):
        # print('Generation ' + str(generation))
        num_gens = generation

        pop_final =  agents = fitness(agents)
        agents = selection(agents)
        agents = crossover(agents)
        agents = mutation(agents)
    return pop_final


# Inicializa a população.
def init_agents(population_size):
    return [Agent() for _ in range(population_size)]


# Determina o fitness de cada agente por meio da função objetivo.
def fitness(agents):
    for agent in agents:
        agent.fitness = (math.sin(pow(agent.value, 2))) / \
            (3-(math.cos(math.e))-agent.value)

    return agents


# Seleciona os 20% melhores da população, baseado no valor de "fitness".
def selection(agents):
    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)
    # print('\n'.join(map(str, agents)))
    agents = agents[:int(0.2 * len(agents))]

    return agents


def crossover(agents):
    global num_crossovers

    offspring = []

    for _ in range((population_size - len(agents)) // 2):
        parent1 = random.choice(agents)
        parent2 = random.choice(agents)

        child1 = Agent()
        child2 = Agent()

        # Crossover utilizando operador BLX-Alpha.
        if random.uniform(0, 1) <= crossover_probability:
            child1.value = parent1.value + beta*(parent2.value - parent1.value)
            child2.value = parent2.value + beta*(parent1.value - parent2.value)
            num_crossovers = num_crossovers + 1
        else:
            child1.value = parent1.value
            child2.value = parent2.value

        offspring.append(child1)
        offspring.append(child2)

    agents.extend(offspring)

    return agents


def mutation(agents):
    global num_mutations

    for agent in agents:
        if random.uniform(0.0, 1.0) <= mutation_probability:
            agent.value = agent.value * random.uniform(0.8, 1.2)
            num_mutations += 1

    return agents


# The file itself
if __name__ == '__main__':
    agents = ga()
    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)

    print(f'População final:\n' + '\t' + '\n\t'.join(map(str, agents)) + '\n' )

    print(
        f'Variáveis:\n'
        f'\tNúmero máximo de gerações: {generations}\n'
        f'\tTamanho da população:{population_size}\n'
        f'\tProbabilidade de crossover: {crossover_probability*100}%\n'
        f'\tProbabilidade de mutação: {mutation_probability*100}%\n\n'
    )

    print(
        f'Resultados:\n'
        f'\tGerações: {num_gens}\n'
        f'\tNúmero de crossovers:  {num_crossovers}\n'
        f'\tNúmero de mutações: {num_mutations}\n\n'
        f'\tIndivíduo mais apto:\n\t\t{agents[0]}\n'
    )
    
