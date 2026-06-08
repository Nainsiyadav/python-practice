# PYTHON LIST METHODS 
# Creating a list
lst = [1, 2, 3, 4, 5]

# 1. ADDING ELEMENTS

# append() - adds element at the end
lst.append(6)
print("append:", lst)

# insert() - adds element at specific index
lst.insert(1, 10)
print("insert:", lst)

# extend() - adds multiple elements
lst.extend([7, 8])
print("extend:", lst)


# 2. REMOVING ELEMENTS

# remove() - removes specific value
lst.remove(10)
print("remove:", lst)

# pop() - removes element by index (last by default)
lst.pop()
print("pop:", lst)

# clear() - removes all elements
temp = [1, 2, 3]
temp.clear()
print("clear:", temp)


# 3. SEARCHING & COUNTING

# index() - returns index of element
print("index:", lst.index(3))

# count() - counts occurrences
lst.append(3)
print("count:", lst.count(3))

# 4. SORTING & REVERSING

# sort() - sorts list
lst.sort()
print("sort:", lst)

# reverse() - reverses list
lst.reverse()
print("reverse:", lst)

# 5. COPYING LIST

# copy() - creates a copy
new_list = lst.copy()
print("copy:", new_list)


# 6. OTHER IMPORTANT OPERATIONS

# length
print("length:", len(lst))

# max and min
print("max:", max(lst))
print("min:", min(lst))

# sum
print("sum:", sum(lst))


# 7. SLICING

nums = [10, 20, 30, 40, 50]

print("slice 1:", nums[1:4])   # [20, 30, 40]
print("slice 2:", nums[:3])    # [10, 20, 30]
print("slice 3:", nums[2:])    # [30, 40, 50]



