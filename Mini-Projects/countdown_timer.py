import time
timer=int(input("time: "))
for i in range (timer,0,-1):
    sec=i%60
    mi=int(i/60)%60
    hr=int(i/3600)
    print(f"{hr}:{mi:02}:{sec:02}")
    time.sleep(1)
time.sleep(.2)
print("YAAAAAAAAAAAAAAAAAAAAAAAA")