item=[]
price=[]
total=0


while True:
    items=input("enter items: (q to quit)  ")
    if items.lower()=="q":
        break
    else:
        prices=int(input("enter price: "))
        item.append(items)
        price.append(prices)

for items in item:
    print(items,end=" ")

for prices in price:
    total+=prices
print(total)


