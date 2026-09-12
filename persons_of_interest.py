#!/usr/bin/env python3

def famous_births(persons_dict):
    # Sort the dictionary values by date_of_birth
    # persons_dict.values() = [{"name": "...", "date_of_birth": "1815"}, ...]
    sorted_persons = sorted(persons_dict.values(), key=lambda person: person["date_of_birth"])

    for person in sorted_persons:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

# Test like in the PDF
if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

    famous_births(women_scientists)