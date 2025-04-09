"""You are given a number n. Your task is to write a function that will return the n-th prime number.
For example, if n is 1, the function should return 2. If n is 3, the function should return the third prime number, which is 5."""


'''Checks if n is a prime number'''


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return n
 
'''Loops through n_ranges to bring out all primes between n and 2 * n'''
def nth_prime(n):
    all_primes = [2]
    count = 0
    if n <= 1:
        all_primes.append(2)
        # print(f"Because n is 1 all_primes = {all_primes}")


    for i in range(1, n * n, 2):  
        if is_prime(i) >= 2:
            count += 1
            all_primes += [i]
            if count == n:
                break

        else:
            continue 

    print(all_primes)
    return all_primes[n-1]
 # Outputs: False
print(nth_prime(1000))