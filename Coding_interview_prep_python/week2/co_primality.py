"""You are provided with two integers, a and b. Your task is to write a Python function that checks whether both a and b are co-prime or not. Two numbers are said to be co-prime or mutually prime if the only positive integer that divides both of them is 1 - Two numbers are coprime (also called relatively prime) when they have no common factors except the number 1.

For Example:-
print(are_coprime(15, 28))   # Output: True
print(are_coprime(12, 18))   # Output: False

Explanations: In the first example, the only positive integer that divides both 15 and 28 is 1; hence, they are co-prime. However, in the second example, 12 and 18 are divisible by 2 and 3; thus, they are not co-prime.
"""

"""LONGER SOLUTION"""
# def are_coprime(a, b):
#     # TODO: implement
#     factors_a = []
#     factors_b = []
#     for i in range(1, a + 1):
#         if a % i == 0:
#             factors_a += [i]
#         else:
#             continue

#     for i in range(1, b + 1):
#         if b % i == 0:
#             factors_b += [i]
#         else:
#             continue 

#     common_factors = [] 
#     for j in factors_a:
#         if j in factors_b:
#             common_factors.append(j)
#         else:
#             continue    
#     print(f"common_factors of {a,b} is {common_factors}")    
#     if 1 in common_factors and len(common_factors) == 1:
#         return True
#     else:
#         return False


# print(are_coprime(1, 1))   # Output: True
# print(are_coprime(17, 51))   # Output: False


"""Way shorter version"""
from math import gcd

def are_coprime(a, b):
    # TODO: implement    
    if gcd(a,b) == 1:
        return True
    else:
        return False


print(are_coprime(1, 1))   # Output: True
print(are_coprime(17, 51))   # Output: False