'''Create a program using user defined function named login that accepts userid and password as parameters 
(login(uid,pwd)) that displays a message “account blocked” in case of  three wrong attempts. The login 
is successful if the user enters user ID as "ADMIN" and password as "St0rE@1". On successful login, 
display a message “login successful”    '''

def login(uid,pwd):
    if uid=="ADMIN" and pwd=="St0rE@1":
        print("GOOD")
        return True
    if t==3:
        print("Account blocked")
        return False


t=0
while t<3:
    uid=input("enter the user id: ")
    pwd=input("enter the password: ")
    if login(uid,pwd):
        break
    
    t=t+1
    if t == 3:
        print("account blocked")



