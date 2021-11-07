# Else clause is executed after for loop completes. It can be difficult to know
# if the loop successfully completed especially if there is a break statement
# in the loop. Else statement here assures us that loop ran successfully throughout.
# This means that the loop did not encounter a break statement.

for i in range(5):
    print(i)
else:
    print('yes')


# It seems redundant hence the confusion but see it this way.
# What if there was a break statement in the loop:

for i in range(5):
    print(i)
    if i == 2:
        break
else:
    print("yes")

# Else clause in For Else structures are completion clauses. They are confused 
# heavily because they resemble if / else structures where else triggers a
# conditional behavior rather than a completion behavior. 