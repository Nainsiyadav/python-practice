
# ----------Type Conversion ------------

# you can convert a  value from one type to another tpye using these built-in functions.

# 1. Converting string value to int value
a  =   "8"
b = int(a) # tpye casting Strint To integer

print(type(a))  # it will return 'str' (string)

print(type(b))  # it will return 'int' (integer)

#2. Converting int to Float 
a=6
print(float(a))
print(type(a))

# 3. You  can convert any data type to string value
a=134
b=56.8
c=12+13j
d=True

print(str(a))
print(str(b))
print(str(c))
print(str(d))

# 4. Converting into boolean value

a=12
b=0
c=12.6
d=0.0
e=""
f="hello"

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))

