a= int(input("enter the first number: "))
n=int(input("enter the no. of terms: "))
d= int(input("enter the common difference: "))

an= a+(n-1)*d
print("the last term of the AP series is: ",an) 

s=(n/2)*(2*a+(n-1)*d)
print("the sum of the AP series is: ",s)

if n>0:
    print("the AP series is: ")
    for i in range(n):
        term= a+i*d
        print(term)
if n<=0:
    print("plz enter a positive integer")
