# Suppose you’re digging through your grandma’s attic and come across a 
# mysterious locked suitcase.
# Grandma tells you that the key for the suitcase is probably in this 
# other box.
# This box contains more boxes, with more boxes inside those boxes. The 
# key is in a box somewhere. What’s your algorithm to search for the key? 
# Think of an algorithm before you read on.

#Ther are two possible approaches:

# 1 - While loop approach

"""
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print “found the key!”
"""

# 2 - Recursion approach

"""
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item) Recursion!
        elif item.is_a_key():
            print “found the key!
"""


# Divide & Conquer

# Sum array elements with recursion:

def sum_array_elements(l):
    sum = 0

    # base case 1
    if len(l) == 0:
        return 0
    # base case 2    
    elif len(l) == 1:
        return l[0]
    else:
        for i in range(len(l)):
            sum = l.pop(l[i])
            return sum_array_elements(l) + sum
    

l1 = [1, 2, 3]
l2 = [5]
l3 = []
print(sum_array_elements(l1), sum_array_elements(l2), sum_array_elements(l3))


def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

l1 = [1, 2, 3, 5]
l2 = [5]
l3 = []
print(sum(l1), sum(l2), sum(l3))


# Write a recursive function to count the number of items in a list.

def count(l):
    if len(l) == 0:
        return 0
    else:
        return 1 + count(l[1:])

# The else statement can be implied:
"""
def count(l):
    if len(l) == 0:
        return 0
    return 1 + count(l[1:])

"""

print(count([1, 2, 4]))


# Find the maximum number in a list

def max(l):
    if len(l) == 0:
        return 0
    else:
        if max(l[1:]) > l[0]:
            return max(l[1:])
        else:
            return l[0]

print(max([1, 4, 3, 7]))


# Double array elements:

def double(arr):
    if len(arr) == 0:
        return []
    else:
        return [2*arr[0]] + double(arr[1:])

double([1, 2, 5])


# Quicksort algorithm

def quicksort(arr):
    #base case:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([5, 4, 2, 10]))





