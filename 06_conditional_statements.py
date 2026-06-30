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



# Quezzzz
# Quezzz.1---->

a = int(input("please enter your first number : "))
b = int(input("please enter your second number :"))
if(a>b):
    print("a is greatest number ")
elif(b>a):
    print("b is greatest number ")
else:
    print("Both numbers are eqale ")

# Quezzz.2------>

gender = str(input("please enter your gender : "))
if(gender=="M" or gender=="m"):
    print("hlo! your are a male ")
elif(gender=="F" or gender=="f"):
    print("hlo! your are a female")
else:
    print("Sorry! i think you are transgender")

# Quezzz.3--->

n = int(input("please enter your number here : "))
if(n%2==0):
    print("your number is even ")
else:
    print("your number is odd ")


# Quezzz.4----->

year = int(input("please enter your year : "))
if(year%100==0 and year%400==0):
    print("your year is leap year")
elif(year%100 !=100 and year%400==0):
    print("your year is leap year")
else:
    print("your year is not a leap year")
