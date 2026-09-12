#!/usr/bin/env python3

num_str = input("Give me a number: ")

num = float(num_str)

if num % 1 == 0:
    print("This number is an integer.")
else:
    print("This number is a decimal.")