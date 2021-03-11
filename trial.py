from math import *
from random import *
from time import *
lim=int(input("Enter a limit: "))
a=randint(1,lim)
start=time()
print("Started")
num=randint(1,lim)
while True:
	change=a-num
	change_abs=abs(change)*2
	ra=randint(0,change_abs)
	print("Number: ",num)
	print("Change: ",change)
	if change<0:
		num=num-ra
	elif change>0:
		num=num+ra
	if change==0:
		break
end=time()
print(a)
print(num)
print(end-start)
