def minimum(arr):
    return min(arr)


def maximum(arr):
    return max(arr)


print(maximum([2, 3, 21, 51]))


## Use range method to get a number until the last i.e 5 - 1 (as computer starts at 0) and step in this case -1

def reverse_seq(n):
    arr = []
    for i in range(n, 0, -1):
        arr.append(i)
    return arr

def abbrev_name(name : str):
    first_letter = name[0]
    last_letter = name[name.find(" ") + 1]

    return first_letter.capitalize() + "." + last_letter.capitalize()

print(abbrev_name("Yusuf Ismail"))


def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    else:
        return "green"

def StringChallenge(strParam):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    count = 0
    for char in strParam:
        if char in consonants:
            count += 1
    return count

print(StringChallenge("Hello World"))

a = 10
b = 24
print(a + b)

def count_number_of_fours_in_string(str):
    count = 0
    for char in str:
        if char == "4":
            count += 1
    return count

print(count_number_of_fours_in_string("283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796"))

# Return string in alphabetical order
def alphabet_soup(str):
    return str.swapcase()

print(alphabet_soup("hello"))

def MathChallenge(num : int):
    # check if is power of 2
    if num & (num - 1) == 0:
        return True
    else:
        return False

print(MathChallenge(6))
