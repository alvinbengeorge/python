set1, set2 = set([int(i) for i in input("Enter set 1: ").split()]), set([int(i) for i in input("Enter set 2: ").split()])
print(set1.isdisjoint(set2))
print(not any(i in set2 for i in set1))