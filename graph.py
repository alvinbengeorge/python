import time
import math
a=float(input("Enter 1 unit: "))
b=int(input("Enter the size of the graph: "))
start=time.time()
for j in range(b,-b,-1):
    for i in range(-b,b,1):
        y=j*a
        x=i*a
        #enter the formula in the "if statement"
        if 2**x==y:
            print(" .", end="")
        elif x==0 and y==0:
            print(" O", end="")
        elif x==0:
            print(" |",end="")
        elif y==0:
            print(" -",end="")
        else:
            print("  ", end="")      
    print()
end=time.time()
print("Runtime: ",end-start)


    

    
