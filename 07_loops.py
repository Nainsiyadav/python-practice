
# For loop 
# For loop with integers
'''for i in range(0,51,2):
   print(i)

# Printing multiplication table 
n = int(input("please enter you number you want to print multiplication table :- "))
for i in range(n,n*10+1,n):
    print(i)

# For loop with Strings
# Method-1
a="students"
for i in a:
    print(i)

# Method-2
a=str(input("please enter your String :-"))
for i in range(len(a)):
    print(f"{i} : {a[i]}")'''



# Break and Continue 
'''1. break Statement------
The break statement immediately stops the loop and moves execution to the first statement after the loop.'''
# Example:
for i in range(0,11):
    if i==4:
        break
    print(i) 

'''2. continue Statement
The continue statement skips the current iteration and moves to the next iteration of the loop.'''
# Example :
for i in range(1,11):
    if i==4:
        continue
    print(i)

'''The else block runs only if the loop finishes normally (without a break).
Example 1: else with break'''
for i in range(0,11,1):
    if i==6:
        break
    print(i)
else:
    print("No break was used ")

# else with continue
for i in range(0,11,1):
    if i==4:
        continue
    print(i)
else:
    print("No continue was used ")


