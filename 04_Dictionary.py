# PYTHON DICTIONARY 

# A dictionary stores data in key-value pairs

d = {"name": "Nainsi", "age": 20, "course": "BCA"}

print("Original Dictionary:", d)


# 1. ACCESSING VALUES

# get() - safely access value
print("Name:", d.get("name"))

# direct access
print("Age:", d["age"])


# 2. ADDING / UPDATING VALUES

# Adding new key-value
d["marks"] = 90
print("After adding:", d)

# update() - update dictionary
d.update({"age": 21})
print("After update:", d)


# 3. REMOVING ELEMENTS

# pop() - removes specific key
d.pop("marks")
print("After pop:", d)

# popitem() - removes last inserted item
d.popitem()
print("After popitem:", d)

# del keyword
del d["age"]
print("After delete:", d)

# clear() - removes all items
temp = {"a": 1, "b": 2}
temp.clear()
print("After clear:", temp)


# 4. DICTIONARY METHODS

# keys() - returns all keys
print("Keys:", d.keys())

# values() - returns all values
print("Values:", d.values())

# items() - returns key-value pairs
print("Items:", d.items())


# 5. COPY DICTIONARY

new_dict = d.copy()
print("Copy:", new_dict)


# 6. DEFAULT VALUE

# setdefault() - returns value, if not present adds key
d.setdefault("city", "Mumbai")
print("After setdefault:", d)



# 7. LENGTH

print("Length:", len(d))


# 10. NESTED DICTIONARY

students = {
    "student1": {"name": "A", "marks": 80},
    "student2": {"name": "B", "marks": 90}
}

print("Nested Dictionary:", students)


