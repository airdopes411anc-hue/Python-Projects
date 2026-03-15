"""1, 1, 2, 3, 5, 8, 13, 21, 34, 55…"""



n =int(input("enter the no. of element : "))
a = 1
b = 0
lst = []
count=0
while count <n:
    lst.append(a)
    a,b=a+b,a
    count=count+1

for i in lst:
    print(i,end=",")

