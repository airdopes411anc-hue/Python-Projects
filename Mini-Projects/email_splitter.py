mail=[]
domain=[]
username=[]

n=int(input("enter the amount of students :"))
for i in range(1,n+1):
    email=input(f"Enter the email of student {i}")
    mail.append(email)
    m=email.split("@")
    domain.append(m[1])
    username.append(m[0])

print(tuple(mail))
print(tuple(domain))
print(tuple(username))