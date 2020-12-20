import time
a="Hurricane Gonzalo formed on October 12, 2014, and became the first Category 4 Atlantic hurricane since Hurricane Ophelia in 2011."
print(a)
start=time.time()
print("_"*100)
print("TYPE THIS^^^, in 1 line")
s=input()
end=time.time()
t=end-start
l=len(a)
l1=len(s)
if l1<l:
     
c=0
w=0
for i in range(0,1):
    if s[i]==a[i]:
        c=c+1
    else:
        w=w+1
print("Correct characters: ",c)
print("Wrong character: ",w)
print("Time: ",t)
print(l)
print(l1)


