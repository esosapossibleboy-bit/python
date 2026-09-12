#!/usr/bin/env python3

def greetings(name="noble stranger"):
    # check type
    if not isinstance(name, str):
        print("Error! It was not a name.")
        return
    print(f"Hello, {name}.")

# Test like in the subject
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)