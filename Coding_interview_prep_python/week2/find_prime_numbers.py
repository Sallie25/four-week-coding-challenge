"""identifying if a number is prime or not. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

Now that we've grasped the idea of handling math problems in Python let's proceed to practice exercises! This basic understanding of standard math algorithms can be a game-changer in solving multifaceted coding challenges. It's not just about applying a function to solve a problem but more about understanding the logic behind it that paves your way toward becoming a skilled programmer.
"""
# """___Simpler way to do this___"""

# def is_prime(n):
#     """
#     This function checks if a number is prime.
#     - Returns False if the number is less than or equal to 1.
#     - Then checks if any number from 2 up to the square root of n divides it evenly.
#     -If any such number is found, n is not prime (return False).
#     - If no such number divides n, then n is prime (return True).
#     """
#     if n <= 1:
#         return False
    
#     for i in range(2, int(n**0.5) + 1): # range from 2 to the square root of n + 1 cos range will not include the last number.
#         # So, if any value in the range from 2 to the square root of n divides n evenly, then n is not a prime number, so the function returns False.However, if none of the values in that range divide n, then n is a prime number, so the function returns True.
        
#         if n % i == 0:
#             return (False,None)
#     return (True,n)

# # Example usage
# print(is_prime(10)) # Outputs: False
# print(is_prime(2)) # Outputs: True


def is_prime(value):
    if value <= 1:
        return False

    count = 0
    divisors = []
    prime = False
    for i in range(1, value + 1):
        if value % i == 0:
            divisors += [i]
        else:
            continue    

    for _ in divisors:
        count += 1
    if count == 2:
        prime = True
        return prime
    else: 
        return prime

print(is_prime(2)) # Outputs: True
print(is_prime(6)) # Outputs: False       


