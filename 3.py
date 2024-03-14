# 2.2.2Write a Python program which takes a list and returns a list with the elements "shifted left by one position" so [1, 2, 3] yields [2, 3, 1]. Example: [1, 2, 3] → [2, 3, 1] [11, 12, 13] → [12, 13, 11].
# Program:
def skip_newlist(num):
    if len(num)<2:
        return num
    else:
        shift_list = num[1:]
        shift_list.append(num[0])
        return shift_list

input_list = input("Enter The List Data :")
number = [int (i) for i in input_list.split()]
print(f"Your List Is : {number}")
result = skip_newlist(number)
print(result)