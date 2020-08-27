import math
import time
num= int(input("Enter any number: "))
start =time.time()
lim=int(math.sqrt(num))+1
for i in range(2,lim):
    if num%i==0:
        print("Composite number")
        break
else:
    print("Prime number")
end=time.time()
print("Runtime: ", end-start)
