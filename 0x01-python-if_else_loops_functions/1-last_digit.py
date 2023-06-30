#!/usr/bin/python3
import random

# Generate a random number between -10000 and 10000
number = random.randint(-10000, 10000)

# Define unique strings to describe the number's properties
str1 = " and exceeds 5"
str2 = " and equals 0"
str3 = " and is below 6 but not 0"

# Determine the last digit of the number
if number < 0:
    last = number % -10
else:
    last = number % 10

# Print the description of the number based on its last digit
if last > 5:
    print("The last digit of {} is {}{}".format(number, last, str1))
elif last == 0:
    print("The last digit of {} is {}{}".format(number, last, str2))
else:
    print("The last digit of {} is {}{}".format(number, last, str3))
