
# PYTHON TUPLES (ALL METHODS & OPERATIONS)

# A tuple is an ordered and immutable collection

t = (1, 2, 3, 4, 2)

print("Tuple:", t)

# 1. count()

# count() - counts how many times a value appears
print("Count of 2:", t.count(2))   # Output: 2

# 2. index()

# index() - returns index of first occurrence
print("Index of 3:", t.index(3))   # Output: 2

# 3. LENGTH

# len() - returns number of elements
print("Length:", len(t))

# 4. MAX, MIN, SUM

print("Max:", max(t))
print("Min:", min(t))
print("Sum:", sum(t))

# 5. SLICING

print("Slice 1:", t[1:4])   # (2, 3, 4)
print("Slice 2:", t[:3])    # (1, 2, 3)
print("Slice 3:", t[2:])    # (3, 4, 2)

# 6. IMMUTABLE PROPERTY

# Tuples cannot be changed
# t[0] = 10   ❌ Error


# 7. CONVERTING LIST TO TUPLE

lst = [10, 20, 30]
new_tuple = tuple(lst)
print("Converted Tuple:", new_tuple)





