# Iterable
lst = [1, 2, 3, 4]
for el in lst:
    print(el)


# Iterator
iterator = iter(lst)
print(type(iterator))
for i in iterator:
    print(i)

try:
    print(next(iterator))
except StopIteration:
    print("The iterator is empty")


# Generator

def square(n):
    for i in range(n):
        yield i**2

# note: try to understand why I used "yield" instead of "return"

print(square(3))

for i in square(3):
    print(i)

g = square(3)
print(next(g))

# We can create an iterator with a generator, but what are the differences 
# between the two?

# difference 1:
# to create an iterator we use iter() and to create a generator we use a
# function along with yield keyword, which saves the local variables

# difference 2:
# generators in python helps us write fast and compact code

# difference 3:
# Python iterators are mmuch more memory efficient