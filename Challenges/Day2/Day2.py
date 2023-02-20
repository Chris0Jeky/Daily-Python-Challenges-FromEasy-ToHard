"""Day 2: Strings to Integers
Write a function called convert_add that takes a list of strings
as an argument and converts it to integers and sums the list. For
example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
summed to 9.
Extra Challenge: Duplicate Names
Write a function called check_duplicates that takes a list of
strings as an argument. The function should check if the list has
any duplicates. If there are duplicates, the function should return
the duplicates. If there are no duplicates, the function should
return "No duplicates". For example, the list of fruits below
should return apple as a duplicate and list of names should
return "no duplicates".
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']"""

def convert_add(list_of_strings):
    total = 0
    for string in list_of_strings:
        number = int(string)
        total = total + number

    return total

def check_duplicates(list_of_strings):
    unique_strings = set()
    duplicates = []

    for string in list_of_strings:
        if string in unique_strings:
            duplicates.append(string)
        else:
            unique_strings.add(string)

    if duplicates:
        return duplicates
    else:
        return "no duplicate"

print(convert_add(["1", "2", "2"]))
print(check_duplicates(["apple", "orange", "banana", "apple"]))
print(check_duplicates(["yoda", "moses", "joshua", "mark"]))

