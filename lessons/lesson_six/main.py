# Use Input

# Input is the string data type
user_name = input("what is thyr name?: ")

print("Hello " + user_name)

user_age = int(input(user_name + " How old are you?: "))

isOld = False

if user_age >= 50:
    isOld = True
elif user_age <= 50:
    isOld = False

messageIfOld = ""

if isOld:
    messageIfOld = "you are old"
else:
    messageIfOld = "you are not old"

print("You are " + str(user_age) + " and " + messageIfOld)
