"""Your task is to create a Python function called get_prime_factors(n) that will return all unique prime factors of an integer n in a list. A prime factor of n is a prime number that divides n without leaving a remainder.
Note that returned prime factors should be unique and sorted in ascending order in the resulting list.

def get_prime_factors(n):
    # TODO: Implement the function that returns all prime factors of n
"""

'''Find all the factors on n'''


def factors(n):
    n_factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            n_factors += [i]
        else:
            continue 
    # print(f"All the factors of {n} is {n_factors}")       
    return n_factors


'''Checks if n is a prime number'''


def is_prime(n):
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return 0
    return n


'''Loops through n_ranges to bring out all primes between n and 2 * n'''


def get_prime_factors(n):
    # TODO: Implement the function that returns all prime factors of n


    all_primes = []
    for i in factors(n):
        # print(f"Current iteration of i is {i}") 
        if is_prime(i) >= 2: # is_prime checks if any of the factors of n
            # is a prime and appends the factor to all primes if it is true. 
            # if is_prime returns 0 it means that factor is not a prime number.
            all_primes += [i]
        else:
            continue 
    return all_primes

print(get_prime_factors(18))