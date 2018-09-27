# Authors:		Derek Lance
# 				Patrick Farrell
# Course:   	CSC 466
# Assignment: 	Lab 1
# Term:			Fall 2018


# Input:    File name (string) to be read into the program
#           File is expected to be in .csv format with m lines of n entries
# Output:   An mxn list of frozensets where each frozenset is a market basket
def readData(filename):
    itemsets = []

    ''' Open file, read each line into data array'''
    with open('{}'.format(filename)) as f:
        for line in f:
            marketbasket = [int(i) for i in line.split(',')]
            marketbasket.pop(0)             # remove receipt id
            itemsets.append(frozenset(line))

    f.close()
    return itemsets
