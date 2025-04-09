"""You are given an integer number, 1≤n≤10**6

Your task is to write a function next_prime(n), that takes an integer n as input and returns the smallest prime number larger than n.

Here are some examples:

next_prime(7) should return 11, because 11 is the next prime number after 7.
next_prime(13) should return 17, because 17 is the next prime number after 13.
next_prime(50) should return 53, because 53 is the next prime number after 50."""


# """Code signal's Solution"""

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def next_prime(n):
#     n += 1
#     while not is_prime(n):
#         n += 1
#     return n

"""_______My Solution_________"""

'''Define the ranges for the loop'''
# def n_ranges(n):
#     ranges = range(n, 2 * n ) #Bertrand’s Postulate
#     return ranges

'''Checks if n is a prime number'''
def is_prime(n):
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return 0
    return n

# print(is_prime(10)) # Outputs: False
# print(is_prime(2)) # Outputs: True
 
'''Loops through n_ranges to bring out all primes between n and 2 * n'''
def next_prime(n):
    all_primes = []
    for i in range(n, 2 * n):
        if n <= 1:
           return 2
        
        elif is_prime(i) >= 2:
            all_primes += [i]
        else:
            continue 

    if all_primes[0] == n:
        return all_primes[1]   
    else:
        return all_primes[0]
 # Outputs: False
print(next_prime(11)) 


