import time
# for loop is like a while loop but is limited

# 0 - 9
# for i in range(10):
# print(i)

# 0 - 10
# for i in range(10 + 1):
# print(1)

# exclusive number is not included
# for i in range(50, 100):
# print(i)

# now with a third argument which is how many step to count by each time.

# for i in range(50, 100, 2):
# print(i)

# Prints each letter to a new line
# for i in "Yusuf Ismail":
# print(i)

# A countdown from 10 to 0
for seconds in range(10, -1, -1):
    print(seconds)
    time.sleep(1) # like Thread.sleep in java

print("Happy Eid")
