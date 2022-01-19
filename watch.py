import time
while(True):
    try:
        print(time.asctime(time.localtime(time.time()))[-13:-5],end='\r')
    except KeyboardInterrupt:
        print("watch closed")
        break