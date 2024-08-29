# Homework-03

# from typing import List
# import random


# numbers: List[int] = []

# for i in range(0, 100):
#     numbers.append(random.randint(1, 1000))

# print(numbers)

# maximum_number = numbers[0]
# for i in range(1, len(numbers) - 1):
#     if numbers[i] > maximum_number:
#         maximum_number = numbers[i]

# print(maximum_number)


# Homework-02

# from typing import List, Union

# my_list: List[Union[int, str]] = [1, 3, 5, 6, "Peyman"]


# Homework-01

from typing import Dict, List, Union
from pprint import pprint


def format_name(person: Dict[str, Union[str, int]]):
    print(person["first_name"].upper() + " " + person["last_name"].upper())


def calculate_age(birth_year: int) -> int:
    """
    Calculate age based given birth year

    Parameters
    ----------
    birth_year : int
        birth year

    Returns
    -------
    int
        age
    """
    return 1403 - birth_year


persons: List[Dict[str, Union[str, int]]] = []
total_input: int = int(input("Please insert input numbers: "))

for i in range(0, total_input):
    first_name: str = input("Please enter your first name: ")
    last_name: str = input("Please enter your last name: ")
    birth_year: int = int(input("Please enter your birth year: "))

    person: Dict[str, Union[str, int]] = {
        "first_name": first_name,
        "last_name": last_name,
        "birth_year": birth_year,
    }

    persons.append(person)


pprint(persons)


for person in persons:
    format_name(person=person)
    print(calculate_age(birth_year=person["birth_year"]))
    print("=====================================")
