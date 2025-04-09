"""You are given a list of integers. Your task is to write a Python function to find the second-largest number among these integers. If the list has fewer than two unique numbers, return None.

You are not allowed to use any built-in Python functions or methods such as sorted(), max(), or sort(). Instead, you should implement the task using basic list operations.

  # check_unique = None
    # All_values = []
    # check = True
    # Truth = True
    # while Truth:
    #     for k in nums:
    #         All_values += [k]
    #         if k == check_unique:
    #             check = True
    #         else:
    #             check = False
    #             Truth = False
               
    #     if check == True:
    #         # return None
    #         return (All_values, None) 
"""

# from typing import List, Optional


# def second_max(nums: List[int]) -> Optional[int]:
#     # TODO: Find the second largest number in nums
    
#     ''' This deals with empty list'''
#     if nums == []:
#         return None 
    

#     ''''Handling unique elements in a list'''
#     nums = list(set(nums)) 
     
 
#     ''' This deals with the first Maximum value'''
#     first_max = nums[0]
#     count = 0
#     for i in nums:
#         count += 1
#         if i > first_max:
#             first_max = i
#         else:
#             continue
#     '''This deals with a list with less than two elements'''
#     if count < 2:
#         return None    
    
#     '''This handles the second maximum element'''
#     # nums = set(nums)
#     # nums = list(nums)
#     # print(nums)
    
#     num_iter = []
#     for ind, j in enumerate(nums):
#         # print(j)
#         if j == first_max:
#            continue
#         else:
#             num_iter += [j]
#     # print(num_iter)

#     sec_max = num_iter[0]
#     for l, m in enumerate(num_iter):
#         if m > sec_max:
#                sec_max = m
#         else:
#             continue       
      
#     return sec_max


from typing import List, Optional

# TODO: Find the second largest number in nums


def second_max(nums: List[int]) -> Optional[int]:
    ''' This deals with empty list'''
    if nums == []:
        return None

    ''''Handling unique elements in a list'''
    nums = list(set(nums))
 
    ''' This deals with the first Maximum value'''
    first_max = nums[0]
    count = 0
    for i in nums:
        count += 1
        if i > first_max:
            first_max = i
        else:
            continue
    '''This deals with a list with less than two elements'''
    if count < 2:
        return None
    
    '''This handles the second maximum element'''
    
    num_iter = []
    for j in nums:
        if j == first_max:
           continue
        else:
            num_iter += [j]

    sec_max = num_iter[0]
    for m in num_iter:
        if m > sec_max:
               sec_max = m
        else:
            continue

    return sec_max

    
# print(second_max([1, 2, 3, 2, 1]))
# print(second_max([1, 3,-5, 5, 20])) 
# print(second_max([]))
# print(second_max([10, 10, 10, 10]))
# print(second_max([0, 0, 0, 0, 0, -2, -3]))
