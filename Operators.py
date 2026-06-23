 
# Operators in Python
# 1.Arithmetic Operators(+,-,*,/,%,**,//(floar division))
'''() - Brackets
** - Exponent (right to left : 2**2**3 = 2**(2**3))
* , /,//,% - Multiplication, Division, Floar Division, Modulus
+ , - - Addition, Subtraction  '''

a=12
b=20
print(a+b)
print(a+b+97)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)

# 2. Comparision Operators --> always return true or false.(==,>,<,>=,<=,!=)
 
a=89
b=76
print(a==b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)

# 3. Logical Operators(and (&), or(|), not)

print("logical and Operator: ",a>b & b>8)
print("logical or Operator: ",a>b | b>8)
print("logical not Operator: ",not a>b)

# 4.Assignment Operators(+=,-=,*=,/=,%=,//=,**=)

a=3
a += 2
print(a)

a=4
b -= 2
print(b)

f=7
f *= 4
print(f)

g = 8
g **= 2
print(g)

r = 9
r //= 2
print(r)

