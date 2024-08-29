from typing import Dict, List
# from pprint import pprint
# from datetime import datetime

# persons = [
#     {"first_name": "Peyman", "last_name": "barjoueian", "age": 1370},
#     {"first_name": "Akbar", "last_name": "Asghari", "age": 1373},
# ]
# print(persons[0]["first_name"].upper() + " " + persons[0]["last_name"].upper())
# print(persons[1]["first_name"].upper() + " " + persons[1]["last_name"].upper())

# person1_age = 1403 - persons[0]["age"]
# person2_age = 1403 - persons[1]["age"]
# print(person1_age)
# print(person2_age)
# ages = [person1_age, person2_age]
# print(ages)
# result = (ages[0] + ages[1]) / len(ages)
# print(result)


x: int = 12
y: float = 12.5
w: str = "Peyman Barjoueian"
z: List[str] = ["Peyman", "Barjoueian", 12]
q: Dict[str, str] = {"fname": "Peyman", "age": 23}


# print(w)

x + y
z
q


# print(datetime.now().day)


# from persiantools.jdatetime import JalaliDateTime

# print(JalaliDateTime.now())


# file = open("message.txt", "w", encoding="utf-8")
# file.write("hello\n")
# file.write("world\n")
# file.close()


# import urllib.request

# # make a HTTP request
# req = urllib.request.urlopen("https://en.wikipedia.org")
# # read content as utf-8 string
# content = req.read().decode("utf-8")

# # save to file
# file = open("wikipedia.html", mode="w", encoding="utf-8")
# file.write(content)
# file.close()


# a = 2
# b = 5

# print(a == b)  # a is equal to b
# print(a != b)  # a not equal to b
# print(a < b)  # a is smaller than b
# print(a > b)
# print(a <= b)  # a is smaller than or equal to b
# print(a >= b)


# numbers = [2, 5, -3, 8, 1, -5]

# for number in numbers:
#     if number % 2 == 0:
#         print("Even")
#     else:
#         ...

# for i in range(-10, 1):
#     print(-i)


# def average(a, b):
#     m = (a + b) / 2
#     print(m)


# result = average(2, 3)


# print("What is your name?")
# # Comment
# name = input()
# # Comment
# print("Nice to meet you, " + name)
# # determine the length of the name
# name_length = len(name)
# print(name_length)

# from math import floor
# # import math
# # print(math.floor(3.6))
# print(floor(3.6))

# from pprint import pprint
# persons = [
#     {"first_name": "Peyman", "last_name": "barjoueian", "age": 1370},
#     {"first_name": "Akbar", "last_name": "Asghari", "age": 1373},
# ]

# pprint(persons)


# file = open("message.txt", "w", encoding="utf-8")
# file.write("hello\n")
# file.write("world\n")
# file.close()



# import urllib.request

# # make a HTTP request
# req = urllib.request.urlopen("https://en.wikipedia.org")
# # read content as utf-8 string
# content = req.read().decode("utf-8")

# # save to file
# file = open("wikipedia.html", mode="w", encoding="utf-8")
# file.write(content)
# file.close()


# import random

# print(random.randint(1, 6))
# print(random.choice(["heads", "tails"]))