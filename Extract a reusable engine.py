# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 12:40:49 2022

@author: plate
"""

import pandas as pd
pd.set_option('display.max_columns', None)    # 显示所有列
pd.set_option('display.max_rows', None)      # 显示所有行


import random
import datetime

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?."
target = "Hello" #12个占位符


def generate_parent (length):
    genes = []
    
    while len(genes) < length:
        #这个地方要使用extend，添加可迭代对象的元素到sample列表里面                                                                                                                                                
        # append是添加对象在列表里面    
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
        
    return ''.join(genes)


def get_fitness(guess):
    
    total = 0
    
    for expected, actual in zip(target, guess):
        if expected == actual:
            total = total + 1
    return total


random.seed()
startTime = datetime.datetime.now()
def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("guess:{0}\t fitness:{1}\t {2}".format(guess, fitness, str(timeDiff)))


random.seed()
startTime = datetime.datetime.now()
#initializing bestParent to a random sequence of letters
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
#calling the display function
display(bestParent)


def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    if newGene == childGenes[index]:
        childGenes[index] = alternate
    else:
        childGenes[index] = newGene
        
    return ''.join(childGenes)


def log_show(log):
    print('这条数据的分析结果是：{}'.format(log))
    log_file = open('C:\\Users\\plate\\Desktop\\测试结果.txt', 'a+')
    for k in range(0, 50000):
        log_file.write('这条数据的分析结果是：{}'.format(log))
    log_file.close()


while True:
    child = mutate(bestParent)
    #log_show(child)
    childFitness = get_fitness(child)
    #log_show(childFitness)
    #首先看新生成的孩子的匹配度是否高于父亲的匹配度
    #如果孩子的匹配程度大于父亲的匹配程度，则把该孩子作为下一代的父亲
    #如果孩子的匹配程度小于父亲的匹配程度，则继续寻找合适的孩子
    #由于每次只对一个基因进行突变，所以每次匹配度最多增加1
    #如果不是，直接舍弃掉
    if bestFitness >= childFitness:
        continue
    display(child)
    ##如果是，则把该孩子作为下一代的父亲    
    bestParent = child
    bestFitness = childFitness
    if childFitness >= len(bestParent):
        break
    

newGene, alternate = random.sample(geneSet, 2)
print(newGene, alternate)


































































