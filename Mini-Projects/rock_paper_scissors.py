import random
options=("rock","paper","sissor")

r=True

while r:
    y=0
    x=random.choice(options)
    while y not in options:
        y=input("enter choice : ").lower()
        

    if x==y:
        print("tie")
    elif y== "rock" and x=="sissor":
        print("win")
    elif y== "paper" and x=="rock":
        print("win")
    elif y== "sissor" and x=="paper":
        print("win")
    else:
        print("womp womp")

    again=input("vapis harega ?? (y/n)")
    if not again=="y":
        r=False
print ("hatt")