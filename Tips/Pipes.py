# Write clean code using pipes

# map and filter are two efficient Python methods to work with iterables. 
# However, the code can look messy if you use both map and filter at the same time.

arr = [1, 2, 3, 4, 5]
list(map(lambda x: x*2, filter(lambda x: x%2 == 0, arr)))

# Same operation with pipes:
from pipe import select, where
list(arr
     | where(lambda x: x%2 == 0)
     | select(lambda x: x*2))


# Where: filter elements in an iterable:
list(arr | where(lambda x: x%2 == 0))

# Select: apply a function to an iterable
list(arr | select(lambda x: x*2))



# Unfold Iterables:

# - chain:  chain a sequence of iterables
from pipe import chain
nested = [[1, 2, 3], [4, 5]]
list(nested | chain)

# - traverse: recursively unfold iterables
from pipe import traverse
nested2 = [[1, [2], 3], [4, [5, 6]]]
list(nested2 | traverse)


# Let’s integrate this method with the select method to get 
# the values of a dictionary and flatten the list.

fruit = [
    {'name': 'apple', 'price': [2, 5]},
    {'name': 'orange', 'price': 4},
    {'name': 'grape', 'price': 5}
]


list(fruit
    | select(lambda fruit: fruit['price'])
    | traverse)


# Group elements in a list
from pipe import groupby, select, where

list((1, 2, 3, 4, 5, 6, 7, 8, 9)
    | groupby(lambda x: 'Even' if x%2 == 0 else 'Odd'))

list((1, 2, 3, 4, 5, 6, 7, 8, 9)
    | groupby(lambda x: 'Even' if x%2 == 0 else 'Odd')
    | select(lambda x: {x[0]: list(x[1])}))

# to select only elements greater than 2:
list((1, 2, 3, 4, 5, 6, 7, 8, 9)
    | groupby(lambda x: 'Even' if x%2 == 0 else 'Odd')
    | select(lambda x: {x[0]: list(x[1] | where(lambda x : x > 2))}))



# References:
# https://towardsdatascience.com/write-clean-python-code-using-pipes-1239a0f3abf5