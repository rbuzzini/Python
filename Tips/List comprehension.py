l = [1, 2, 3, 4, 5, 6]

# return l squared with a for loop:
lSquared = []
for i in l:
    lSquared.append(i**2)

print(lSquared)

# return l squared with a for loop:
lSquared2 = []
[lSquared2.append(i**2) for i in l]
print(lSquared2)
print('The two lists are identical? {}'.format(lSquared == lSquared2))

# We can use conditions inside list comprehension:
lEvenSquared = []
[lEvenSquared.append(i**2) for i in l if i%2==0]
print(lEvenSquared)

