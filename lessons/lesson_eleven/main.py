# Functions stops you from repeating code
# Python use : instead of {}

def happy_eid(name: str):
    print("Eid Mubarak " + name)
    print("May Allah grant us another eid")
    print("Eid Mubarak " + name)
    print()


happy_eid("Yusuf")
happy_eid("Yusuf")
happy_eid("Yusuf")


# f at the start of the print means you can format the print and include values in brackets.
def display_invoice(username: str, amount: float, due_date: str):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
    print()


display_invoice("David", 200.50, "01/01")


# Return = a statement used to end a function and send a result back to the caller

def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z


def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    z = x / y
    return z


print(add(9, 10))
print()
print(subtract(9, 10))
print()
print(multiply(9, 10))
print()
print(divide(9, 10))
print()


def name(name: str, age: int):
    return name + " is " + str(age) + " years old"


print(name("Yusuf", 16))
print()


def create_name(first: str, last: str):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("Yusuf", "Ismail")

print(full_name)
