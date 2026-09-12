#!/usr/bin/env python3

def average(class_dict):
    # sum of all scores / number of students
    if len(class_dict) == 0:
        return 0
    return sum(class_dict.values()) / len(class_dict)

# Test like in the PDF
if __name__ == "__main__":
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }

    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")