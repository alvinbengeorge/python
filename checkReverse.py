l = [int(i) for i in input("Enter: ").split(" ")]
check = lambda li: li == sorted(li) or li == sorted(li, reverse=True)
print(check(l))