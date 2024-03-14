# 2.3Write a program to convert a list of characters into a string.
# Program:


def character_inString(input_string):
    return ''.join(input_string)

input_string = input("Enter The Characters (without spaces) :")
input_string=list(input_string)
print("Your Input Characters List Is :\n",input_string)
result = character_inString(input_string)
print("\n String Representation :",result+"\n")