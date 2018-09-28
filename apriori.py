# Authors:		Derek Lance
# 				Patrick Farrell
# Course:   	CSC 466
# Assignment: 	Lab 1
# Term:			Fall 2018

import main

# comments todo
def apriori(T, itemset, minSup):


    F = [frozenset({i}) for i in itemset if support(T, frozenset({i})) >= minSup]
    frequentItemsets = F
    k = 2
    n = len(T)

    while F:

        f = set(F)
        candidates = main.candidateGen(f, k-1)
        count = [0 for i in range(len(candidates))]

        for marketbasket in T:
            for i, candidate in enumerate(candidates):
                if candidate.issubset(marketbasket):
                    #print(i)
                    count[i] += 1

        F = [candidate for i, candidate in enumerate(candidates) if count[i] / n >= minSup ]
        for itemset in F:
            for i, itms in enumerate(frequentItemsets):
                if itms.issubset(itemset):
                    frequentItemsets.pop(i)
            frequentItemsets.append(itemset)
        k += 1


    return frequentItemsets

# comments todo
def support(T, items):

    numBaskets = 0

    for marketbasket in T:
        if items.issubset(marketbasket):
            numBaskets += 1

    return numBaskets / len(T)
