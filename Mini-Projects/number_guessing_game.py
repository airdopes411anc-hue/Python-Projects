import random
high=100
low=1
print(f"============== WELCOME TO THIS GAME THE RANGE IS {low}-{high} ===============")
y=random.randint(low,high)
g=0
while True:
    x=input("enter a no.: ")
    if x.isdigit():
        x=int(x)
        g+=1
        if x>high:
            print("go less out of range\n")
        elif x<low:
            print("go more out of range\n")
        elif x>y:
            print("go less\n")
        elif x<y:
            print("go high\n")
        elif x==y:
            print("correct")
            print(f"No. of Guess = {g}")
            break
    else:
        print("INVALID")