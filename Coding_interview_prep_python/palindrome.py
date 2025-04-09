"""You are given a string, and your task is to check whether the provided string is a palindrome, without using any built-in string methods. A string is a palindrome if it reads the same forward and backward, ignoring the casing of letters ('A' and 'a' are considered the same) and ignoring non-letter characters.

Return a boolean value: True if the string is a palindrome and False if it is not.

It is not allowed to use Python built-in functions like reverse(), reversed(), or similar in this task.
"""
def letter_retrieval_lower(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_caps = ""
    for i, j in enumerate(upper_alphabet):
        if j == letter:
            lower_caps = alphabet[i]
            break
        else:
            continue
    return lower_caps

def solution(input_string):
    # TODO: Implement the function to check whether the provided string is a
    # palindrome or not.

    transformed = ""
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reversed = ""

    for i,j in enumerate(input_string):
        if j in lower_alphabet:
            transformed += j
        elif j in upper_alphabet:
            transformed += letter_retrieval_lower(j)
        else:
            continue
            # transformed += j

    for i in range(1, len(transformed) + 1):
        reversed += transformed[-i]
    print(reversed, transformed)
    return reversed == transformed  

print(solution("A man, a plan, a canal: Panama"))
