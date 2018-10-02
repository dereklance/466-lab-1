from candidateGen import candidateGen

def genRules(supports, minConfidence):
	rules = set()
	supports = {
		frozenset({0, 2, 5}): 0.04,
		frozenset({0, 2}): 0.06,
		frozenset({0, 5}): 0.06,
		frozenset({2, 5}): 0.06,
		frozenset({5}): 0.06,
		frozenset({2}): 0.06,
		frozenset({0}): 0.06
	}

	print(supports)
	for itemset in supports.keys():
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

