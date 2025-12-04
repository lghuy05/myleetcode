# 1
# seq1 = [-3, -2, -1, 0, 1, 2, 3]
# seq2 = [i * (-10) if i < 0 else i + 15 for i in seq1]


# question 2
# 20 -40 80 -160 320 -640

# question 3
# sub = "Patience is a prize. end pursuit of perfection."


# question 4
# def petinfo(name, age, breed, *rules):
#     print(f"You will pet-sit {name}, a {age}-year-old {breed}")
#     print(f"Rules for {name}:")
#     for val in rules:
#         print(val)


# question 5
# p, q, r, s = 1, 2, 3, 5
# try:
#     somemath = lambda p, q, r, s: (p * q) / (r - s)
#     result = somemath(p, q, r, s)
# except ZeroDivisionError:
#     print("divide 0 is stupid bitch")
# else:
#     print(result)
# finally:
#     print("This segment is completed")
#
# question 6
# -6.0
# This segment is completed

# question 8
# 19 + 63 * 7 + 0 %

# question 9
with open("xmaswishlist.txt", "r") as infile:
    gifts = infile.read()

# question 10
import random as rand

clay_rank = rand.randint(1, 47)


# question 11
class Vegetable:
    pass


class Potato(Vegetable):
    pass


# question 12
class Sorcerer:
    def __init__(self, name, occupation, technique) -> None:
        self._name = name
        self._occupation = occupation
        self._technique = technique

    # question 13
    def __str__(self):
        return f"{self._name}, {self._occupation}, {self._technique}"


# question 14
# from SpecialGrade import Sorcerer

kitkat = Sorcerer("Satoru Gojo", "Teacher", "Unlimited Void")

# question 15
print(kitkat)
