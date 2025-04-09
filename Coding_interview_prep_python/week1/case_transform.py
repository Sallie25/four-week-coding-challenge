"""
Given a string input_string, your task is to write a function that transforms all the lowercase letters to uppercase and all the uppercase letters to lowercase. If the character is not a letter, do not transform it.

The transformation should be done without using any built-in Python methods, it is not allowed to use built-in Python functions like lower(), upper(), or similar in your code.

For example, for the input string "HelLo WoRld 123", the output should be "hELlO wOrLD 123".
"""

"""________BETTER SOLUTION_________"""
# def solution(input_string):
#     transformed_string = ""
#     for char in input_string:
#         ascii_val = ord(char)
#         if 65 <= ascii_val <= 90:  # Uppercase A-Z
#             transformed_string += chr(ascii_val + 32)
#         elif 97 <= ascii_val <= 122:  # Lowercase a-z
#             transformed_string += chr(ascii_val - 32)
#         else:
#             transformed_string += char
#     return transformed_string


def letter_retrieval_caps(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    next_letter = ""
    for i, j in enumerate(alphabet):
        if j == letter:
            next_letter = upper_alphabet[i]
            break
        else:
            continue
    return next_letter

def letter_retrieval_lower(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    next_letter = ""
    for i, j in enumerate(upper_alphabet):
        if j == letter:
            next_letter = alphabet[i]
            break
        else:
            continue
    return next_letter

def solution(input_string):
    # TODO: implement the function
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    transformed_string = ""
    for ind, var in enumerate(input_string):
        if var in lower_case:
            transformed_string += letter_retrieval_caps(var)
        elif var in upper_case:
            transformed_string += letter_retrieval_lower(var)   
        else:
            transformed_string += var             
    return transformed_string        

print(solution("CaSeChAnGe"))


