import openpyxl


# Load excel workbook:
wb = openpyxl.load_workbook(r'C:\Users\rbuzzini\Documents\Personale\Git\Python\transaction.xlsx')

# Access a single worksheet in the workbook:
ws = wb['Sheet1']
 

# Create a new worksheet:
wb.create_sheet('NewSheet')
# with the index parameter you can specify the position
# where you want to create the worksheet (wb.create_sheet('NewSheet', 1))

# the changes won't be added to the file until you save them
wb.save(r'C:\Users\rbuzzini\Documents\Personale\Git\Python\transaction.xlsx')