# Authors:		Derek Lance
# 				Patrick Farrell
# Course:   	CSC 466
# Assignment: 	Lab 1
# Term:			Fall 2018

from itertools import combinations
import tests
import data

# Set F of frequent itemsets of size k
# Returns an array of candidate itemsets of size k + 1
def candidateGen(F, k):
	C = set()

	for f1, f2 in combinations(F, 2):
		c = f1.union(f2)
		flag = False

		if len(c) == k + 1:
			flag = True
		for s in combinations(c, len(c) - 1):
			if not set(s) in F:
				flag = False
		if flag == True:
			C.add(c)

	return C

# Input:    Market basket data set, T           (list of frozensets)
#           set of all possible items, I        (set)
#           minimum support value required for an itemset to be considered
#           a frequent itemset, minSup          (float)
#
# Output:   A set of all frequent itemsets (size 2 or larger) of items from I
#            found in T
#           Data format is a dictionary where each key is a frozenset of the
#           frequent itemset and the value is the support of that itemset
def apriori(T, I, minSup):

    # Generate frequent itemsets of size 1
    F = [frozenset({i}) for i in I if support(T, frozenset({i})) >= minSup]
    frequentItemsets = {}
    k = 2
    n = len(T)

    # While there are still possible candidates
    while F:

        # Set up working copy of gen k frequent itemsets and get the candidates
        # Initialize the counts for each generated candidate
        f = set(F)
        candidates = candidateGen(f, k-1)
        count = [0 for i in range(len(candidates))]

        # Calculate the number of occurences of each generated candidate in
        # the overall market basket data
        for marketbasket in T:
            for i, candidate in enumerate(candidates):
                if candidate.issubset(marketbasket):
                    count[i] += 1

        # Set F to be all candidates in the current gen s.t. the support of the
        # candidate is greater than or equal to the specified minimum support
        # value
        F = [candidate for i, candidate in enumerate(candidates) if (count[i] / n) >= minSup ]


        # Add gen k to the master frequentItemsets dict with its support value
        # and increment the gen counter, k
        for fq in F:
            frequentItemsets[fq] = (support(T, fq))
        k += 1


    return frequentItemsets

# Input:    Collection of frequent itemsets, F                      (dict)
# Ouput:    A skyline collection of frequent itemsets of F          (dict)
#           i.e. removes all sets in F that are a subset of another set in F
def skylineFrequentItemsets(F):

    """
    Copy all itemsets in F into 2 new structures
    For each itemset in the first copy
        if it is subset of any other itemset
            remove it from the second copy

    for each itemset in the second copy
        Copy it into the new dict and store its support as the value

    return new dict

    """


    keysT = list(F.keys()).copy()
    keys = keysT.copy()
    #print(keysT)
    #print(keys)

    fD = {}
    for itmsetA in keys:
        #print("OUTER: {}".format(itmsetA))
        for itmsetB in keys:
            #print("\tINNER: {}".format(itmsetB))
            if not (itmsetA == itmsetB) and itmsetA.issubset(itmsetB):
                #print("\t\tREMOVING {} ".format(itmsetA))
                if itmsetA in keysT:
                    keysT.remove(itmsetA)
        #print(">>{}".format(keysT))

    #print(keysT)
    #rint(keys)
    for skyline in keysT:
        fD[skyline] = F[skyline]

    return fD


# Input:    A collection of marketbaskets T and a specific itemset items
# Ouput:    The support value of items in T (% of all marketbaskets in T
#           containing items)
def support(T, items):
    numBaskets = 0
    for marketbasket in T:
        if items.issubset(marketbasket):
            #print("{} IN {}".format(items, marketbasket))
            numBaskets += 1
    return (numBaskets / len(T))

def getCont():
    c = input("\nContinue? Y / N\n\t")
    if c.lower() == 'y':
        return True
    else:
        return False

def main():

    cont = True

    while cont:


        minSup = float(input("Enter minimum support value: "))
        minConf = float(input("Enter minimum confidence value: "))
        file = input("Enter data filename to use: ")

        print("\nRunning association rules mining on\n\n\t{} with a minSup of\t{}\t and a minConf of\t{}".format(file, minSup, minConf))

        T = data.readDataInput(file)
        goods = data.buildGoods("goods.csv")

        fqItmsets = apriori(T, range(50), minSup)
        skyFQ = skylineFrequentItemsets(fqItmsets)

        writeFile = input("\n\nFilename to write output to: ")
        with open("{}".format(writeFile), "w") as f:
            f.write("Frequent itemsets: \n\n")

            for itmset in skyFQ:
                f.write("< ")
                for itm in itmset:
                    f.write(" {} {} ".format(data.foodFlavor(goods, itm), data.foodName(goods, itm)))
                f.write(" >\t\tSUPPORT: {}\n".format(skyFQ[itmset]))

        cont = getCont()

    return



if __name__ == "__main__":
	main()
	F = {'1', '2'}
	f = {'1'}
