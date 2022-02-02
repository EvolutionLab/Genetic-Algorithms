
geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?."
target = "Hello World!"

import random

def generate_parent (length):
    genes = []
    
    while len(genes) < length:
        
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
        
    return ''.join(genes)

#例如，此时产生的基因长度是56
gene = generate_parent(56)


def get_fitness(guess):
    
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)

#通过适合度函数得到fitness value
guess = get_fitness(gene)




def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    return ''.join(childGenes)

parent = generate_parent(56)
print(parent)
newParent = mutate(parent)
print(newParent)



























