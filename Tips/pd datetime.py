import pandas as pd

data = pd.DataFrame({'Date': ['01/01/2021', '01/02/2021', '01/03/2021']})

data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
data.dtypes

# Remember that it's better to work with date as index. For this see 
# the time series tutorial in "Fun Project" folder.


# Get year, month and day number
data['year'] =  data['Date'].dt.year
data['month_num'] =  data['Date'].dt.month
data['day_num'] = data['Date'].dt.day

# Get month and day name
data['month_name'] = data['Date'].apply(lambda x: x.strftime('%B'))
data['day_name'] = data['Date'].apply(lambda x: x.day_name())
data.head()

