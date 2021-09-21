# Python provides the assert statement to check if a given logica expression
# is true or false.
#Program execution proceeds only if the expression is true and raises an 
# AssertionError when it is false.


num = 10
assert num>=10 
assert num > 10 # AssertionError raises

# assert statement is like an exception handling applied to a logical expression.

try:
    num = int(input('Enter a number:'))
    assert num%2==0
    print('The number is even')
except AssertionError:
    print('Please enter even number')
