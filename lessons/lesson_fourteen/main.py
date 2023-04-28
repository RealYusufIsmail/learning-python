# Collections = single "variables" used to store multiple values
# List = [] order and changeable. Duplicates ok. Can add and remove
# Sets = {} unordered and imutable. No duplicates. Can add and remove
# Tuple = () ordered and unchangeable

# Lists

# Each value in collection are called elements
fruits = ["apple", "orange", "banana", "coconut"]

# Displays the attributes and methods
# print(dir(fruits))

# Explains those attributes and methods
# print(help(fruits))

# Returns the number of elements
# print(len(fruits))

# Whether the value is in list. Returns a boolean.
# print("banana" in fruits)

# Can change the value of list
# fruits.insert(1, "rearranger")

# To access elements use indexing
# print(fruits[::-1])

# common convection
# for fruit in fruits:
# print(fruit)

# Reassigns value of apple to carrot
# fruits[0] = "carrot"

# Adds a value to the list at the end of it.
# fruits.append("carrot")

# print(fruits) # ['apple', 'orange', 'banana', 'coconut', 'carrot']

# Removes a value
# fruits.remove("apple")

# swaps a value for another
# fruits.insert(0, "cake")

# Sorts the values in alphabetical order
# fruits.sort()

# Reverses the order that there were placed in
# fruits.reverse()

# This is reverse alphabetical order
# fruits.reverse()
# fruits.sort()

# Clears a list
# fruits.clear()

# Returns the index of a named fruit within the list
# fruits.index("apple") # 0

# can count the number of the same objects as they can be duplicated
# fruits.count("apple")

# Sets

# Can not have duplicates - not ordered. Works well with constants
sweets = {"cakes", "chocolates", "biscuits"}

# Displays the attributes and methods
# print(dir(sweets))

# Explains those attributes and methods
# print(help(sweets))

# Returns the number of elements
# print(len(sweets))

# Whether the value is in list. Returns a boolean.
# print("cakes" in sweets)

# can not use indexing in sets as they are unordered.

# Can add values
# sweets.add("white_chocolate")

# Can remove values
# sweets.remove("cakes")

# Remove first element in list when printed. Will not be the same removed element each time.
# sweets.pop()

# Clears the set
# sweets.clear()

# Able to copy the values to a new set
# newSet = sweets.copy()

# print(sweets)

# Tuple

# Can not be changed and always ordered. Can have duplicates and much falser
cars = ("bmw", "tesla", "volvo")

# Displays the attributes and methods
# print(dir(cars))

# Explains those attributes and methods
# print(help(cars))

# Returns were that car is
# cars.index("bmw")

# counts the number of the given value
# cars.count("bwm")

print(cars)