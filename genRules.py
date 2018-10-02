from candidateGen import candidateGen

def genRules(supports, skylines, minConfidence):
	rules = set()

	for itemset in skylines:
		if len(itemset) < 2:
			continue
		
		currentRules = set()
		for item in itemset:
			leftside = itemset.difference([item])
			rightside = item
			confidence = supports[itemset] / supports[frozenset([item])]
			print('confidence', confidence)
			if confidence >= minConfidence:
				currentRules.update({(leftside, rightside)})

		rules.update(currentRules)
	
	return rules

def main():
	print('genRules')

if __name__ == '__main__':
	main()

