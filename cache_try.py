from math import *
from random import *
from time import *
d={}
maximum=0
max_value=0
lim=int(input("Enter limit: "))
start=time()
for i in range(0,lim):
	a=i
	l=[]
	while (a!=0):
		if a!=i:
			l=l+[a]
		if d.get(a,None)!=None:
			l=l+d[a]
			break
		if a%2==0:
			a=a//2
		else:
			a=a*3+1
		if a==1:
			break
	d[i]=l
	#print(i,l,sep=": ")
	if len(l)>max_value:
		max_value=len(l)
		maximum=i
end=time()		
print("Maximum: ",maximum)
print("Maximum length: ",max_value)
print("List: ",d[maximum])
print("Time: ",(end-start))
