import pandas as pd

#Example df:
df = pd.DataFrame({
    'item': ['phone', 'mouse', 'keyboard'],
    'January 2021': [1000, 200, 300],
    'February 2021': [3500, 100, 250],
    'March 2021': [2000, 400, 500],
    'April 2021': [5000, 50, 150]})

df = df.append([df[df['item'] == 'phone']]*3, ignore_index=True)
df

# Count item frequency and selecting the most frequent one:
count = df.item.value_counts()
count.nlargest(1).index

phones = df[df['item'].isin(count.nlargest(1).index)]
phones.head()

# Obviously you can do it with multiple categories


# With the ~ operator you can do the opposite operation: exclusion
not_phones = df[~df['item'].isin(count.nlargest(1).index)]
not_phones.head()