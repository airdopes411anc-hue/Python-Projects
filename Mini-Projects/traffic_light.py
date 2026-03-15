'''Write a program that simulates a traffic light . The program should consist of the following:
1. A user defined function trafficLight( ) that accepts input from the user, displays an error message 
if the user enters anything other than RED, YELLOW, and GREEN. Function light() is called and following is 
displayed depending upon return value from light().
a) “STOP, your life is precious” if the value returned by light() is 0.
b) “Please WAIT, till the light is Green “ if the value returned by light() is 1
c) “GO! Thank you for being patient” if the value returned by light() is 2.
2. A user defined function light() that accepts a string as input and returns 0  when the input is RED, 
1 when the input is YELLOW and 2 when the input is GREEN. The input should be passed as an argument.
3. Display “ SPEED THRILLS BUT KILLS” after the function trafficLight( ) is executed.'''

x=input("enter the signal colour: ").lower()

def light(x):
    if x=="green":
        return(2)
    if x=="red":
        return(0)
    if x=="yellow":
        return(1)
    
y = light(x)

def trafic_light(x):
    lst=["green","red","yellow"]
    if x in lst:
        pass
    else:
        print("error")

    if y==0:
            print("STOP, your life is precious")
    if y==1:
            print("Please WAIT, till the light is Green")
    if y==2:
            print("GO! Thank you for being patient")
    print("SPEED THRILLS BUT KILLS")
    
light(x)
trafic_light(x)