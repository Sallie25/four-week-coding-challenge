"""You are given an integer number n. The task is to determine if this number is a perfect square or not. A perfect square is a number that can be expressed as the product of an integer with itself. For example, 1 = 1 * 1, 4 = 2 * 2, 9 = 3 * 3, and 16 = 4 * 4 are perfect squares, but 2, 3, 5, and 6 are not.

Implement a function is_perfect_square(n) that returns True if the given number n is a perfect square and False otherwise.
"""


def is_perfect_square(n):
    if n <= 2 or (n % n**0.5) != 0:
        return False
    elif (n % n**0.5) == 0:
        return True
    
    
print(f"is_perfect_square(2): {is_perfect_square(2)}\n")
print(f"is_perfect_square(144): {is_perfect_square(144)}\n")
print(f"is_perfect_square(1521): {is_perfect_square(1521)}\n")
print(f"is_perfect_square(1458): {is_perfect_square(1458)}\n")
print(f"is_perfect_square(1000000000000): {is_perfect_square(1000000000000)}\n")
print(f"is_perfect_square(99999998320036): {is_perfect_square(99999998320036)}\n")    