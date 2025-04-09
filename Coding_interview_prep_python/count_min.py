"""You are given an array of integers. Your task is to write a function in Python that returns the number of times the smallest element appears in the array.

Please note that built-in methods such as min() or count() should not be used in this task. Your goal is to accomplish this task by iterating over the array elements manually. Try to solve the task by doing just a single list traversal."""


"""_______________METHOD 1_____________________"""

# def count_min(numbers):
#     # TODO: Implement this function to count the smallest integer in the list.
#     if numbers == []:
#         return 0

#     count = 0
#     element = numbers[0]

    
#     for i in numbers:
#         if i < element:
#             element = i    

#         else:
#             continue 


#     for _  in numbers:
#         if _ == element:
#             count += 1

#     return (element, count)  # cos, it will always count the first element
# sample_list = [3, 4, 1, 7, 9, 2, 6, 5, 3, 1, 5, 1, 1]  
# print(count_min(sample_list))  


"""_______________METHOD 2_____________________"""

def count_min(numbers):
    # TODO: Implement this function to count the smallest integer in the list.
    if numbers == []:
        return 0 
    
    count = 0
    element = numbers[0]
    for i in numbers:
        if i < element :
            element = i 
            count = 1
            
        elif i == element:
                count += 1
    return (count)      
    # return (element, count)  # cos, it will always count the first element
sample_list = [3, 4, 1, 7, 9, 2, 6, 5, 3, 1, 5, 1, 1]  
print(count_min(sample_list)) 