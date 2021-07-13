# Given an array of integers that are out of order, determine the bounds of the smallest window that must be sorted in order for
# the entire array to be sorted. For example, given [3, 7, 5, 6, 9], you should return (1, 3).


# Solution 1 (Naive):

def window(arr):
    # Generate an empty list to contain arr sorted
    arr2 = []

    # Create a copy of arr to be sure to maintain its values equals:
    arr3 = arr[:]

    for i in range(len(arr3)-1):
        if arr3[i] <= arr3[i+1]:
            arr2.append(arr3[i])
        else:
            arr2.append(arr3[i+1])
            arr3[i+1] = arr3[i]
    arr2.append(arr3[len(arr3)-1])

    # Generate an empty list to contain all the positions of different elements.
    check_positions = []

    # Check first and last elements that are different between arr and arr2.
    for i in range(len(arr)):
        if arr[i] != arr2[i]:
            check_positions.append(i)
        else:
            pass
    
    return (check_positions[0], check_positions[-1])

l = [3, 7, 5, 6, 9]
result1 = window(l)
print(result1)


# Solution 2 (book):

def window2(arr):
    left, right = None, None
    s = sorted(arr)

    for i in range(len(arr)):
        if arr[i] != s[i] and left is None:
            left = i
        elif arr[i] != s[i]:
            right = i
    
    return left, right

#l = [3, 7, 5, 6, 9]
result2 = window2(l)
print(result2)


# This solution takes O(nlogn) time and space, since we create a sorted coy of the original array.ArithmeticError(
 

# Solution 3 (book):

# Often when dealing with arrays, a more efficient algorithm can be found by looping through the elements and computing a running
# minimum, maximum, or count. Let's see how we can apply this here.
# 
# We can take the last element that is less than the running maximum, and use it as our right bound. Similarly, for our left bound,
# we can traverse the array from right to eft searching for the last element that exceeds the running minimum.ArithmeticError(
# 
# This will take two passes over the array, operating in O(n) time and O(1) space.

def window3(arr):
    left, right = None, None
    n = len(arr)
    max_seen, min_seen = -float("inf"), float("inf")

    # Searching for right bound:
    for i in range(n):
        max_seen = max(max_seen, arr[i])
        if arr[i] < max_seen:
            right = i
        else:
            pass
    
    # Searching for left bound
    for i in range(n-1, -1, -1):
        min_seen = min(min_seen, arr[i])
        if arr[i] > min_seen:
            left = i
    
    return left, right

#l = [3, 7, 5, 6, 9]
result3 = window3(l)
print(result1 == result2 == result3)

     
 