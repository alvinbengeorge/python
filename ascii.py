import time
for i in range(0,1000):
    time.sleep(0.1)
    print("\003c")
    print(i,chr(i),sep=":")
