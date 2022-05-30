# Given an array of integers, return a new array where each elemnt in the new
# array is the number of the smaller elements to the right of that element in
# the original input array

def smallerCount(arr: list):

    smaller_count_array = [] 

    for i, el in enumerate(arr):
        count = sum(val < el for val in arr[i+1:])
        smaller_count_array.append(count)
    
    return smaller_count_array
        
smallerCount([1, 2, 1])