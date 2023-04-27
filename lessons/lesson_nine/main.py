# If statements = conditional

age = int(input("How old are you?: "))

# Any indented code under the if statement the code block is for the if statement
# elif is else if.
# else is the last resort
# To check if something is equal do == as one = is for assigning something.
# You can just rearrange if statements but gets messy so just operators
if age != 100 and age >= 16:
    print("You are an adult!")
elif age == 100:
    print("Blimey you are old!")
elif age >= 13:
    print("You are a teenager")
elif age < 0:
    print("How are you alive!!")
else:
    print("You are a child")

