# Logical operators (and, or, not) = used to check if 2 or more conditional statements are true

temp = int(input("What is the temp outside?: "))

#if temp >= 0 and temp <= 30:
    #print("The temperature is fine today!")
    #print("go outside")
#elif temp < 0 or temp > 30 :
    #print("The temperature is bad today")
    #print("Stay inside")

# Not will flip things
if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today")
    print("Stay inside")
elif not(temp < 0 or temp > 30) :
    print("The temperature is fine today!")
    print("go outside")

## can also do 0 <= temp <= 30