# Use * and _ to improve your unpacking.

# Unpacking example:
x, y, z = (1, 2, 3)
print(x, y, z, sep=',')

# You can use * to unpack "the rest" of the items in an iterable.
# It is common to use when you have some items of interest,
# and other items that are less important.
x, *y, z = [1, 2, 3, 4, 5, 6, 7]
print(x, y, z, sep='\n')

# You can use the underscore _ unpacking operator to unpack and not save a value.
x, _ = (1, 2)
print(x)

# You can also combine both methods to unpack and not store "the rest" of values.
x, *_ = (1, 2, 3, 4, 5, 6)
print(x)