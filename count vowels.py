file = open(input("Enter filename to read: "),"r").read().lower()
vowels = ['a','e','i','o','u']
for i in vowels: 
    print(f"{i:}",file.count(i))
