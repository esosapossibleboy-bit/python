#!/usr/bin/env python3
import sys

def downcase_it(my_string):
    return my_string.lower()

# sys.argv[0] is the program name
# sys.argv[1:] are the real parameters

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        print(downcase_it(arg))