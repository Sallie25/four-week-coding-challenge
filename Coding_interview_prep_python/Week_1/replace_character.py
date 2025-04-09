"""
Given a string input_string, return a new string in which all occurrences of character c1 in the original string replaced by c2. You cannot use any built-in string methods or functions in Python, such as replace().

Here's an example:

print(replace_character("hello, world", "o", "a"))  
# Output: "hella, warld"

"""
def replace_character(input_string, c1, c2):
    # TODO: Replace all occurrences of character `c1` in `input_string` with `c2'
    formatted_string  = ""
    for i, j in enumerate(input_string):
        if j == c1:
            formatted_string += c2
        else:
            formatted_string += j    
    return formatted_string
print(replace_character("we are practicing string manipulations", "i", "o"))