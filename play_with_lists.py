#!/usr/bin/env python3

# Define the original list of numbers as shown in the example
original_list = [2, 8, 9, 48, 8, 22, -12, 2]

# Create a new list by adding 2 to each value using a list comprehension
new_list = [num + 2 for num in original_list]

# Display both lists exactly as formatted in the example output
print(f"Original list: {original_list}")
print(f"New list: {new_list}")