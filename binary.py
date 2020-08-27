#BINARY
a=int(input("Enter a number:"))
b=''
while (a!=0):
    c=a%2
    a=a//2    
    b=b+str(c)  
print(b[::-1])

    
