#!/usr/bin/env python3

def find_the_redheads(family_dict):
    # filter() keeps only names where value == "red"
    # list() converts filter object to list - both mandatory
    return list(filter(lambda name: family_dict[name] == "red", family_dict))

# Test like in the PDF:
if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))