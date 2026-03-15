import time
import random

for i in range(101):
    print(f"Loading {i}%", end="\r", flush=True)
    time.sleep(0.033)
print()

def num():
    for i in range(3):
        a= random.randint(0,12)
        b= random.randint(0,12)
        ans=a+b
        a=int(input(f"{a}+{b}=? "))
        if a==ans:
            print("correct")
        else:
            print("no")
num()