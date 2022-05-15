# To use XlsxWriter with Pandas you has to specify it as the Excel writer engine

# region 1 - Importing/Writing data and access df writer objects
import pandas as pd

df = pd.DataFrame({
    'Index': [1, 4, 3, 2, 7, 13, 1, 4, 3, 2, 7, 13],
    'Data': [10, 20, 30, 40, 50, 35, 72, 10, 50, 5, 3, 18]}
    )

# Create a Pandas Excel writer using XlsxWriter as the engine.
fileName = r'XlsxWriter/pandas_sample.xlsx'
writer = pd.ExcelWriter(fileName, engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, index=False, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file:
# writer.save()

# Get the xlsxwriter objects (workbook and worksheet) from the dataframe writer object.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# endregion

# region 2 - Add Charts

# Once we have the Workbook and Worksheet objects, as shown in the previous 
# section, we we can use them to apply other features such as adding a chart:

# Create a chart object:
chart = workbook.add_chart({'type': 'column'})   # set `type` equal to `line` to have a line plot, etc.

# Get df dimensions:
(max_row, max_col) = df.shape

# Configure the series of the chart from the dataframe data.
chart.add_series({
    'categories': ['Sheet1', 1, 0, max_row, 0], 
    'values': ['Sheet1', 1, 1, max_row, 1]})

# The set_x_axis() method is used to set properties of the X axis:
chart.set_x_axis({
        'name': 'Index',
        'name_font': {'size': 14, 'bold': True},
        'num_font': {'Italic': True}
    })

# The set_y_axis() method is used to set properties of the X axis:
chart.set_y_axis({
        'name': 'Values',
        'name_font': {'size': 14, 'bold': True},
        'num_font': {'Italic': True}
    })

chart.set_title({
        'name': 'Values per Index',
        'name_font': {'size': 14, 'bold': True},
        'num_font': {'Italic': True}
    })

# Insert the chart in the worksheet:
worksheet.insert_chart(1, 3, chart)
# writer.save()
# writer.close()

# endregion


# region 3 - Add Conditional Formatting and Stilying options

# Apply a conditional format to the required cell range.
worksheet.conditional_format(f'B2:B{max_row+1}',# 1, 1, max_col, max_row, 
    {'type': '3_color_scale',
     'criteria': '>',
     'value': df.Data.mean()})

# writer.save()

# see references to see more about this topic

# endregion


# region 4 - Add Pivot Tables

# add a worksheet and the data you need to inserti in:

# pivot data:
min_by_index = df.groupby('Index', as_index=False).min()

# start writing in excel worksheet and set cells properties:
table_titles_props = {
    'bold': True,
    'font_color': 'white',
    'bg_color': 'darkblue'
}

tableTitleFormat = workbook.add_format(table_titles_props)
tableTitleRow = 1
tableTitleColumn = 1
tableTitle = 'Min Value by Index'

pivot_test_sheetName = 'pivot_test'
worksheet_pivot = workbook.add_worksheet(pivot_test_sheetName)
writer.sheets[pivot_test_sheetName] = worksheet_pivot
worksheet_pivot

worksheet_pivot.write_string(tableTitleRow, tableTitleColumn, tableTitle, tableTitleFormat)
min_by_index.to_excel(writer, index=False, sheet_name=pivot_test_sheetName,
        startrow=tableTitleRow+2, startcol=tableTitleColumn)

writer.save()

# endregion

# References:
# - https://xlsxwriter.readthedocs.io/
# - https://katalinnagy.nl/automatic-excel-report-with-pandas-and-xlsxwriter/ to see an example of excel reporting output
# - https://sparkbyexamples.com/pandas/pandas-excelwriter-explained-with-examples/  excelWriter expained with examples