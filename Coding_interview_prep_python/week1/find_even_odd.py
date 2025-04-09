"""You are given an array of integers. Your job is to return the count of even and odd integers in the given array without using any built-in Python methods.

Your function should return a tuple in the format (even_count, odd_count), where even_count represents the number of even integers and odd_count represents the number of odd integers in the provided array.

"""
def solution(nums):
    # TODO: implement the function to return a tuple (even_count, odd_count)
    even_nums = []
    odd_nums = []
    # print(nums)
    for i in nums:
        # print(i)
        if i % 2 == 0:
            even_nums += [i]
        else:
            odd_nums += [i]
    # print(f"The even numbers are: {even_nums}")    
    # print(f"The odd numbers are: {odd_nums}")    

    even_count = 0
    for _ in even_nums:
        even_count += 1

    odd_count = 0
    for _ in odd_nums:
        odd_count += 1  
                
    return(even_count, odd_count)  
          
sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]  
print(solution(sample_list))