d1 = {'A': 10, 'B': 15, 'C': 30}
d2 = {'D': 100, 'E': 150, 'F': 300}

d3 = {**d1, **d2}
print(d3)

# Or we can use the update() method, but the changes will be saved in the
# dictionary where the update() is applied.
d4 = d1.update(d2)
print(d4, d1, sep='\n')