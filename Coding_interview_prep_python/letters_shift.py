"""
Given a string, you need to return a new string where every letter is shifted to its right by one place in alphabetical order. The last letters z and Z should be replaced with the first ones: a and A, respectively. If the character isn't a letter, it should stay the same.

It is not allowed to use string built-in methods here.

For example, given the string "abc123XYz!", the function should return "bcd123YZa!".
"""

# def letter_retrieval(letter):
#     alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     next_letter = ""
#     for i, j in enumerate(alphabet):
#         if j == letter:
#             next_letter = alphabet[i+1]
#             break
#         else:
#             continue
#     return next_letter
        
# def letters_shift(s):
#     alphabet = "abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY"
#     complete_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     required_letters = ""
#     for ind, var in enumerate(s):  
#         # print(f"Current variable is {var}") 

#         if var in alphabet:
#             required_letters += letter_retrieval(var)
#             # print(f"Required letter at index {ind} is {required_letters}")
#         # elif var == "z" or var == "Z":
#             # continue 
#         else:
#             if (var == "z" or var == "Z") and var not in alphabet :
#                 continue
#             else:
#                  required_letters += var 

#     if required_letters[-1] in complete_alphabet:
#         return required_letters + s[0]
#     else:
#         return required_letters[:-2] + s[0] + required_letters[-1]
       
# print(letters_shift("abc123XYz!"))


"""______________CORRECT CODE_____________________"""

# TODO: implement find_vowels_positions
def letter_retrieval(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    next_letter = ""
    for i, j in enumerate(alphabet):
        if j == letter:
            next_letter = alphabet[i + 1]
            break
        else:
            continue
    return next_letter
        
        
def solution(s):
    alphabet = "abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY"
    required_letters = ""
    for  var in s:
        if var in alphabet:
            required_letters += letter_retrieval(var)
        else:
            if var == "z" :
                required_letters += "a"
            elif var == "Z":  
                required_letters += "A" 
            else:
                 required_letters += var
    return required_letters 

print(solution("abc123XYz!"))             
