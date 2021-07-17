def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print ("getting ready to say bye...")
    bye()

#This function greets you and then calls two other functions. Here are 
#those two functions:

def greet2(name):
    print("how are you, " + name + "?")
def bye():
 print("ok bye!")

greet("Robi")


# Call stack with recursion

# Recursive functions use the call stack too! Let’s look at this in action 
# with the factorial function.

# My try forfactorial function
def factorial(n):
    i = 1
    prod = i

    while i <= n:
        prod *= i
        i += 1
    
    return prod

print(factorial(4))

# Now I try with recursion

def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial2(4))




