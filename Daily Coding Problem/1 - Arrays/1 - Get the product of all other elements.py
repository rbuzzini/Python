# Get the product of all other elements

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the
# numbers in the original array excep the one at i.IOError
# For example, if our input was [1, 2, 3, 4, 5] the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
# the expected output would be [2, 3, 6]

# Follow-up: What if you can't use division?


# Solution 1 (with division):

def prod1(arr):
    arr2 = []

    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            product = (product * arr[j])
        arr2.append(int(product / arr[i]))
    
    return arr2

#Some examples:
p1 = prod1([1, 2, 3])
p2 = prod1([1, 2, 3, 4, 5])
print(p1, p2)


# Solution 2 (without division): 

def prod2(arr):
    arr2 = []

    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i != j:
                product *= arr[j]
        arr2.append(product)

    return arr2


# Some examples:
p3 = prod2([1, 2, 3])
p4 = prod2([1, 2, 3, 4, 5])
print(p3, p4)


# Book solution: create a list of prefix products and a list of suffix products and finally multiply the appropriate prefix and
# suffix values to obtain out solution.

def products(arr):
    # Generate prefix products.
    prefix_prod = []

    for el in arr:
        if prefix_prod:
            prefix_prod.append(prefix_prod[-1] * el)
        else:
            prefix_prod.append(el)
    
    # Generate suffix products.
    suffix_prod = []
    for el in reversed(arr):
        if suffix_prod:
            suffix_prod.append(suffix_prod[-1] * el)
        else:
            suffix_prod.append(el)
    suffix_prod = list(reversed(suffix_prod))
    

    # Generate result list from prefix_prod and suffix_prod
    result = []
    for i in range(len(arr)):
        if i == 0:
            result.append(suffix_prod[i+1])
        elif i == len(arr)-1:
            result.append(prefix_prod[i - 1])
        else:
            result.append(prefix_prod[i-1] * suffix_prod[i+1])
    return result

p5 = products([1, 2, 3])
p6 = products([1, 2, 3, 4, 5])
print(p5, p6)


# Check if all the results are equal:
print(p1 == p3 == p5, p2 == p4 == p6)