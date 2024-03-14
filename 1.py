# 2.1To write a Python Program to find the maximum from a list of numbers.
# Program:

input_numbers = input("Enter a list of numbers : ")

"split fuction is separat value"
numbers = [int(i) for i in input_numbers.split()]

if not numbers:
    print("The list is empty.")
else:
    maximum = max(numbers)
    print(f"The maximum value in the list is: {maximum}")