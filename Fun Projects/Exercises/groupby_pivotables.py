import pandas as pd

class_list = ['A', 'A', 'B', 'B', 'C', 'C']
code_list = ['ch16', 'dh16', 'ke48', 'cz12', 'n012', 'm44']
value_list = [100, 200, 150, 300, 50, 100]
df1 = pd.DataFrame({'class': class_list,
    'code': code_list,
    'value': value_list})
df2 = pd.DataFrame({'class': class_list,
    'code': code_list,
    'value': value_list})

df = df1.append(df2, ignore_index=True)
df

# Now I want to see only codes with max values per class.

# Firstly I have to group by class and code:
df_grouped = df.groupby(['class', 'code'], as_index=False).agg({'value': 'sum'}).sort_values(by=['class','value'], ascending=[True,False])
df_grouped

df_grouped.groupby(['class'])['value'].max()

# I saw on the web to do this kind of groupby and then to use an inner join
# with the starting df (in this cas df_grouped), but what if I have duplicates in
# values? How can I add codes in the groupby df?



# Solution 1: Iterate over df_grouped (sorted descending by values) 
# and then take the first line for each class:

df_grouped_maxValue = pd.DataFrame()
for group in df_grouped['class'].unique():
    #f"df_{group}" = df_grouped[df_grouped['class'] == group]     # I don't know why it gives an indentation error
    df_temp = df_grouped[df_grouped['class'] == group]

    for i in df_temp.index:
        df_grouped_maxValue = df_grouped_maxValue.append(df_temp.loc[i])
        break

df_grouped_maxValue



# Solution 2:
# give a rank to eache class codes with a window function.


    
    

