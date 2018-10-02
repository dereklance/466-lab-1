# Authors:		Derek Lance
# 				Patrick Farrell
# Course:   	CSC 466
# Assignment: 	Lab 1
# Term:			Fall 2018


# Input:    File name (string) to be read into the program
#           File is expected to be in .csv format with m lines of n entries
# Output:   An mxn list of frozensets where each frozenset is a market basket
def readDataInput(filename):
    itemsets = []

    ''' Open file, read each line into data array'''
    with open("{}".format(filename)) as f:
        for line in f:
            marketbasket = [int(i) for i in line.split(',')]
            marketbasket.pop(0)             # remove id
            itemsets.append(frozenset(marketbasket))

    f.close()
    return itemsets

# Input:    File name (string) of the csv containing the key for goods
#           interpretation
# Output:   List of lists where each entry is a single good
#           Form [["FoodFlavor", "FoodName", "Price", "FoodType"]
#                [...,          ...,        ...,        ...     ]
#                [...,          ...,        ...,        ...     ]]
def buildGoods(filename):
    goods = []

    with open("{}".format(filename)) as f:
        f.readline()
        for line in f:
            l =[str(i).strip('"\' \n \"') for i in line.split(',')]
            l.pop(0)
            goods.append(l)

    f.close()
    return goods

def buildAuthors(filename):
    authors = []

    with open("{}".format(filename)) as f:

        for line in f:
            l =[i.strip('\n') for i in line.split(' | ')]
            authors.append(l[1])

    f.close()
    return authors

# input     List of goods with names and flavors stored and the good id
# Output    String name of the food with the given id
def foodName(goods, id):
    return goods[id][1]

def writeBakeryOutput(writeFile, F, I):
    with open("{}".format(writeFile), "w") as f:
        f.write("Frequent itemsets: \n\n")
        for itmset in F:
            f.write("< ")
            for itm in itmset:
                f.write(" {} {} ".format(foodFlavor(I, itm), foodName(I, itm)))
            f.write(" >\t\tSUPPORT: {}\n".format(F[itmset]))

def writeBingoOutput(writeFile, F, I):
    with open("{}".format(writeFile), "w") as f:
        f.write("Frequent itemsets: \n\n")
        for itmset in F:
            f.write("< ")
            for itm in itmset:
                f.write("{}\t".format(I[itm]))
            f.write(" >\t\tSUPPORT: {}\n".format(F[itmset]))




# input     List of goods with names and flavors stored and the good id
# Output    String flavor of the food with the given id
def foodFlavor(goods, id):
    return goods[id][0]

def itemName(goods, id):
    return foodFlavor(goods, id) + ' ' + foodName(goods, id)
