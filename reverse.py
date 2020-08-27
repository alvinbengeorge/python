n=int(input("Enter number:"))
s=0
num=n
while n>0:
    rem=n%10
    s=s+(rem**3)
    n//=10
if num==s:
    print("Armstrong")
else:
    print("Not Armstrong")

    
