# Reversed function and reverse method can only be used to reverse objects in 
# Python. But there is a major difference between the two:
# reversed function can reverse and iterable object and returns a reversed object as data type.
# reverse method can only be used with lists as its a list method only.

# Here two examples:

lst=["earth","fire","wind","water"]

lst.reverse()
print(lst)


a=reversed(lst)
print(a)
print(list(a))