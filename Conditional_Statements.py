# Conditional Statements
'''Real programs don't run the same code every time - 
they make decisions. Conditional statements let your program 
choose what to do based on a condition. they's why they're also 
called control flow statements.'''
# if statement
if True:
    print("Hello guys!")

# if-else statement
age = int(input("please enter your age : "))
if(age>=18):
    print("eligible for voting ")
else:
    print("not eligible for voting ")

# else-if statement

money = int(input("please enter your money :"))
if(money==10):
    print("i will have a chocobar")
elif(money==50):
    print("i will have manchurian")
elif(money==100):
    print("i will have one pizza")
elif(money==500):
    print("i will go mcd")
else:
    print("i will stay hungry")