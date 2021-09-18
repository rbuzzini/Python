l = [1, 5, 'hello', (1, 'bike'), 5, 5, 2, 7]
print(max(set(l), key=l.count))
