from itertools import combinations

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

def main():
	F = {
		frozenset(['a']),
		frozenset(['b']),
		frozenset(['c']),
		frozenset(['d'])
	}
	print(candidateGen(F, 1))

if __name__ == "__main__":
	main()
	F = {'1', '2'}
	f = {'1'}