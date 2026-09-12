#!/usr/bin/env python3
# 1. Original list from the exercise
original_list = [2, 8, 9, 48, 8, 22, -12, 2]

# 2. Filter elements > 2 and add 2 (from previous exercise logic)
incremented_list = [num + 2 for num in original_list if num > 2]

# 3. Mandatory Set requirement (used to check for duplicates)
unique_set = set(incremented_list)

# 4. Preserve insertion order for the display to match the terminal exactly
ordered_unique = []
for num in incremented_list:
    if num not in ordered_unique:
        ordered_unique.append(num)

# 5. Print matching the exact format of the screenshot
print(original_list)
print(f"{{{', '.join(map(str, ordered_unique))}}}")