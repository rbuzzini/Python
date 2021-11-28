# how many digits are in large numbers like these?
num1 = 10000000000
num2 = 10000000

total = num1 + num2

print(total)


# "_" in python doesn't affect number value:
num3 = 10_000_000_000
num4 = 10_000_000

print(num1 == num3, num2 == num4, sep='\n')

# How about total?
print(f'{num1+num2:,}')