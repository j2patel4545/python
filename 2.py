# 2.2.1Write a Python program which will return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and number that come immediately after 13 also do not count. Example : [1, 2, 3, 4] = 10 [1, 2, 3, 4, 13] = 10 [13, 1, 2, 3, 13] = 5 
# Program:
def sum_with_unlucky_13(arr):
    total = 0
    for num in arr:
        if num == 13:
            continue
        total += num
    return total

# Example usage:
input_array = input("Enter List Of Number :")
number=[int (i) for i in input_array.split()]
result = sum_with_unlucky_13(number)
print(f"The sum of numbers in the array is: {result}")