"""
1. show balence
2. deposit
3.withdraw
"""


def show_balence():
    print(f"balence is {balence} ")


def deposit():
    amount = int(input("enter the amount to input: "))
    if amount < 0:
        print("nice trick")
        return 0
    else:
        return amount


def withdraw():
    amount = int(input("enter the amount to withdraw"))
    if amount > balence:
        print("nah uh")
        return 0
    elif amount < 0:
        print("nice trick")
        return 0
    else:
        return amount


balence = 0
run = True

while run:
    print("=" * 20)
    print("1.show balence")
    print("2.deposit money ")
    print("3.withdraw money")
    print("4.exit")
    choice = input("enter the choice (1/2/3/4) :")
    if choice == "1":
        show_balence()
    elif choice == "2":
        balence += deposit()
    elif choice == "3":
        balence -= withdraw()
    elif choice == "4":
        run = False
    else:
        print("invaid choice")


print()

print("done")

