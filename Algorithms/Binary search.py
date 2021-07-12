# Let’s see how to write binary search in Python. The code sample here 
# uses arrays.
# The binary_search function takes a sorted array and an item. If the 
# item is in the array, the function returns its position. You’ll keep track 
# of what part of the array you have to search through. At the beginning, 
# this is the entire array:
# low = 0
# high = len(list) -1

# Each time, you check the middle element:
# mid = (low + high) / 2
# guess = list[mid]

# If the guess is too low, you update low accordingly:
# if guess < item:
#     low = mid +1 

# And if the guess is too high, you update high. Here’s the full code:

def binary_search(list, item):
    list = sorted(list)
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid -1
       
    return None

# Test:
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))    # -> 1
print(binary_search(my_list, -2))   # -> None   



# Exercises:


# 1 -  Suppose you have a sorted list of 128 names, and you’re searching 
# through it using binary search. What’s the maximum number of 
# steps it would take?

# Answer: binary search algorithm takes maximum log2(n) steps to find the 
# solution. Then, in this case, the maximum number of steps it would take is
# log2(128) = 7 steps


# 2 - Suppose you double the size of the list. What’s the maximum 
#number of steps now?

# Answer: It would take 1 step more: 8



