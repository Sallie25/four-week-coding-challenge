"""You are given a string s. Your task is to write a function that returns a string in which every pair of adjacent characters in the original string is swapped. If the string has an odd length, leave the last character as it is.

It is not allowed to use Python built-in functions like reverse() or join() in this task, you should implement the solution without using them.

For example, if you are given the string "abcdef", your function should return "badcfe". If the string is "hello", your function should return "ehllo".
"""
def solution(s):
    # TODO: implement the solution here
    swapped_odd = ""
    swapped_even = ""
    swapped = ""
    for i, j in enumerate(s):
        if i % 2 == 0:
            swapped_even += j
            
        else:
            swapped_odd += j          
    print(swapped_even,swapped_odd)
    for k, l in enumerate(swapped_odd):
        swapped = swapped + l + swapped_even[k]

    if len(swapped_even) == len(swapped_odd):
        return swapped 
    elif len(swapped_even) > len(swapped_odd):
        return swapped + swapped_even[-1]
    else: 
        return swapped + swapped_odd[-1]

print(solution("abcdef")) 
print(solution("hello")) 
print(solution("123456"))  