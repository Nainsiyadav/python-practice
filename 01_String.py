# PYTHON STRINGS - ALL CONCEPTS
# A string is a sequence of characters enclosed in quotes

s = "hello world"
# 1. CASE CHANGING METHODS
print("Uppercase:", s.upper())       # HELLO WORLD
print("Lowercase:", s.lower())       # hello world
print("Title Case:", s.title())      # Hello World
print("Capitalize:", s.capitalize()) # Hello world
print("Swapcase:", s.swapcase())     # HELLO WORLD -> hello world


# 2. REMOVE SPACES
s2 = "  hello  "
print("Strip:", s2.strip())          # remove spaces both sides


# 3. REPLACE
print("Replace:", s.replace("l", "x"))  # hexxo worxd


# 4. SPLIT & JOIN
text = "a b c"
print("Split:", text.split())        # ['a', 'b', 'c']

lst = ['a', 'b', 'c']
print("Join:", " ".join(lst))        # a b c


# 5. FIND & COUNT
print("Find index:", s.find("l"))    # first index of 'l'
print("Count:", s.count("l"))       # number of times 'l' appears


# 6. STARTSWITH & ENDSWITH
print("Startswith:", s.startswith("he"))  # True
print("Endswith:", s.endswith("ld"))      # True


# 7. STRING CONTENT
# Strings can contain:
# Letters -> "hello"
# Numbers -> "1234"
# Symbols -> "@#%!"
# Spaces -> "hello world"


# 8. INDEXING
text = "Python"
print("First character:", text[0])   # P
print("Fourth character:", text[3])  # h

# Negative indexing
print("Last character:", text[-1])   # n


# 9. SLICING
print("Slice 1:", text[1:4])  # yth
print("Slice 2:", text[:3])   # Pyt
print("Slice 3:", text[3:])   # hon


# 10. IMMUTABLE
# Strings cannot be changed
name = "Nainsi"
# name[0] = "B"  ❌ Error


# 11. LENGTH
print("Length:", len("Python"))  # 6


# END OF STRING CONCEPTS
