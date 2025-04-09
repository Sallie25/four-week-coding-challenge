"""You are given a list of integers. Your task is to write a function find_min(nums), that returns the minimum number from the list without using Python's built-in min() function.

If the list is empty, your function should return None."""

def find_min(nums):
    if nums == []:
        return None
    
    value = nums[0]
    for var in nums:
        if var < value:
            value = var
        else:
            continue
    return value

sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]    
# sample_list = []        
print(find_min(sample_list)) 