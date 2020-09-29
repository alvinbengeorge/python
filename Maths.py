t=0
for i in range(1,10):
    if i==2 or i==3 or i==4 or i==5 or i==0:
        continue
    for j in range(1,10):
        if j==2 or j==3 or j==4 or j==5 or j==0:
            continue
        for k in range(1,10):
            if k==2 or k==3 or k==4 or k==5 or k==0:
                continue
            t=t+1
print(t)
