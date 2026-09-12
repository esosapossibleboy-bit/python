#!/usr/bin/env python3
import sys

def shrink(my_string):
    print(my_string[:8])

def enlarge(my_string):
    # append Z until 8 chars
    while len(my_string) < 8:
        my_string += 'Z'
    print(my_string)

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else: # == 8
            print(arg)