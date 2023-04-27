# While loop = a statement that will execute it's block of code as the as the condition remains

#name = ""
name = None

#while len(name) == 0:
    #name = input("Enter your name")

while not name:
    name = input("Enter your name: ")

print("Hello " + name)