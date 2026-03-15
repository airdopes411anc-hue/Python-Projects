"""Create a program using user defined function that accepts the shopping amount as a parameter and
calculates discount and net amount payable on the basis of the following conditions:
Net Payable Amount = Total Shopping Amount – discount"""

"""Shopping Amount    Discount Offered
>=500 and <1000            5%
>=1000 and <2000           8%
>=2000                     10%"""


def discount(amt):

    if amt >= 500 and amt < 1000:
        dis = 0.05 * amt
        tamt = amt - dis
    elif amt >= 1000 and amt < 2000:
        dis = 0.08 * amt
        tamt = amt - dis
    elif amt >= 2000:
        dis = 0.1 * amt
        tamt = amt - dis
    else:
        tamt = amt
    print(tamt)


amt = int(input("enter your amount: "))

discount(amt)
