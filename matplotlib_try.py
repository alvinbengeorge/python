import matplotlib.pyplot as plt
import time
import psutil
from matplotlib import style 
style.use("fivethirtyeight")
i=0
x=[]
y=[]
x_d=[]
a=int(input("Enter observation time in seconds:"))
start=time.time()
fig=plt.figure()
while True:
    i=time.time()-start
    y=y+[psutil.cpu_percent(interval=0.1)]
    x=x+[i]
    x_d=x_d+[int(i)]
    if i>=a:
        break
print(x_d,y,sep="\n")
plt.plot(x,y)
plt.xlabel("Time")
plt.ylabel("CPU Usage")
    
plt.show()
