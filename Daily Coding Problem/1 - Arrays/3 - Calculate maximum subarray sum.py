# Given an array of numbers, find the maximum sum of any contiguous subarray
# of the array. For example, given the array [34, -50, 42, 14, -5, 86], the 
# maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
# Given array [-5, -1, -8, -9], the maximum sum would be 0, since we would
# choose not to take any elements.

# Solution 1:

def max_sum(arr):
    sum_max = 0

    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            sum_max = max(sum_max, sum(arr[i:(j+1)]))
    
    return sum_max

print(max_sum([34, -50, 42, 14, -5, 86]), max_sum([-5, -1, -8, -9]))

# This would run in O(n^3) time.

# Solution 2 (book):

def max_sum2(arr):
    max_ending_here = max_so_far = 0

    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print(max_sum2([34, -50, 42, 14, -5, 86]), max_sum2([-5, -1, -8, -9]))

# This algorithm is known as Kadane's algorithm, and it runs in O(n) time and
# O(1) space.


# Solution 3 (book):

# We can first find the minimum subarray sum using exactly the method above,
# and subtract this from the array's total.

def maximum_circular_subarray(arr):
    max_subarray_sum_wraparound = sum(arr) - min_subarray_sum(arr)

    return max(max_subarray_sum(arr), max_subarray_sum_wraparound)

def max_subarray_sum(arr):
    max_ending_here = max_so_far = 0

    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

def min_subarray_sum(arr):
    min_ending_here = min_so_far = 0

    for x in arr:
        min_ending_here = min(x, min_ending_here + x)
        min_so_far = min(min_so_far, min_ending_here)

    return min_so_far

# This takes O(n) time and O(1) space.

print(min_subarray_sum([34, -50, 42, 14, -5, 86]), min_subarray_sum([-5, -1, -8, -9]))








