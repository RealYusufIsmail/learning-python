# dictionaries(maps) = a collection of {key:values} pairs. Order and changeable

capitals = {
    "UK": "London",
    "USA": "Washington DC",
    "China": "Beijing"
}

# shows the functions of dictionaries
# dir(capitals)

# Explains the methods
# help(capitals)

# Get a value from the ky
# print(capitals.get("USA")) # If none is found None will be given

# if capitals.get("Japan"):
#    print("That capital exists")
# else:
#    print("That capital does not exists")

# Adds value to dictionary or updates values
# capitals.update({
#    "Germany": "Berlin"
# })

# Remove a key from the dictionary
#  capitals.pop("UK")

# Will remove the latest value i.e last
# capitals.popitem()

# Clears the full dictionary
# capitals.clear()

# Gets all the keys
keys = capitals.keys()

# Gets all the values.
values = capitals.values()

# Gets all the items in the dictionary i.e 2d list.
# like ('UK', 'London'). Just each individual value and key
items = capitals.items()

for key in keys:
    print(key)
    print()

for value in values:
    print(value)
    print()

for value, key in items:
    print(f"{key}: {value}")
    print()