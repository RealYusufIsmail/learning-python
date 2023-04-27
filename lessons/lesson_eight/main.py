# String slicing which extracts elements from a string
# filed [start:stop:step]
# If first is empty then it will be 0.
# If second is empty it will assume until the end.
# If step is empty it is one by default.

# Indexing[] Part

name = "Yusuf Ismail"

# Computers start from 0 not one. first number is inclusive
# first_name = name[0:5]

# If blank python assumes it is zero
first_name = name[0:5]

# Assumes you want every character from index 6 till the end
last_name = name[6:]

# Step is how much we increase the counting. One by default. Here will display every second character.
funky_name = name[0:5:2]

# Name in reversed
reversed_name = name[::-1]

# print(reversed_name)

# Slice function part

website_one = "https://google.com"
website_two = "https://youtube.com"

# Can add three values like the Indexing[].
# Will use negative indexing but moves from the end and starts at -1
# Will give us the website name
slice = slice(8, -4)

# Removes https:// and .com. Works!
print(website_one[slice])
print(website_two[slice])