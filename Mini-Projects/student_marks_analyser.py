'''Student Marks Analyzer
Features:
Input marks of 5 students
Store in list
Find highest
Find average
Show grade
Use at least 2 functions
'''
def highest(marks):
    return max(marks)

def avg(marks):
    return sum(marks)/len(marks)

lst=[]

for i in range(1,6):
    a=int(input(f"Enter marks of student {i} :"))
    lst.append(a)


print(f"highest marks is {highest(lst)}")
print(f"Average marks is {avg(lst)}")


