""" finding the maximum element in a list. Without using Python's built-in max() function"""
def find_max_element(lst):
    value = lst[0]
    for var in lst:
        if var > value:
            value = var
        else:
            continue
    return value
sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]            
print(find_max_element(sample_list))        