#!/usr/bin/env python3

def add_one(param):
    param += 1
    # param is increased only INSIDE the function
    # you can print it here to check:
    # print(f"inside function: {param}")

var = 5
print(var)
add_one(var)
print(var)