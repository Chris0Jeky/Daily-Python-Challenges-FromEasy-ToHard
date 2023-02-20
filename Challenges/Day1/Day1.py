"""
Day 1: Division and Square-root
Write a function called divide_or_square that takes one
argument (a number), and returns the square root of the number
if it is divisible by 5, returns its remainder if it is not divisible by
5. For example, if you pass 10 as an argument, then your function
should return 3.16 as the square root.
Extra Challenge: Longest Value
Write a function called longest_value that takes a dictionary
as an argument and returns the first longest value of the
dictionary. For example, the following dictionary should return
– apple as the longest value.
fruits = {'fruit': 'apple', 'color': 'green'}
"""


def divide_or_square(num):
    check1 = num / 5
    check2 = num // 5
    if (check1 - check2) == 0:
        return print(str(pow(num, 0.5)))
    else:
        return print(str(num % 5))

divide_or_square(6)
divide_or_square(10)
divide_or_square(0)
divide_or_square(1)