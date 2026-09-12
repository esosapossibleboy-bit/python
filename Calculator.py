#!/usr/bin/env python3

first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))

print("Thank you!")
print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")

# to match example 10 / 2 = 5 and not 5.0
if first % second == 0:
    print(f"{first} / {second} = {first // second}")
else:
    print(f"{first} / {second} = {first / second}")

print(f"{first} * {second} = {first * second}")