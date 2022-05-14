import openpyxl

wb = openpyxl.load_workbook(r'C:\Users\rbuzzini\Documents\Personale\Git\Python\transaction.xlsx')
ws = wb['Sheet1']


# iter_rows:
rows = ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=1, max_col=ws.max_column)

txn_id = []	
member_id = []
ticker = []
txn_date = []
txn_time = []
txn_type = []
quantity = []
percentage_fee = []

for a, b, c, d, e, f, g, h in rows:
    txn_id.append(a.value)	
    member_id.append(b.value)
    ticker.append(c.value)
    txn_date.append(d.value)
    txn_time.append(e.value)
    txn_type.append(f.value)
    quantity.append(g.value)
    percentage_fee.append(h.value)

len(percentage_fee)


# iter_cols:
cols = ws.iter_cols(min_row=1, max_row=ws.max_row, min_col=1, max_col=ws.max_column)

for col in cols:
    print(col)

txn_id = []	
member_id = []
ticker = []
txn_date = []
txn_time = []
txn_type = []
quantity = []
percentage_fee = []

for a, b, c, d, e, f, g, h in rows:
    txn_id.append(a.value)	
    member_id.append(b.value)
    ticker.append(c.value)
    txn_date.append(d.value)
    txn_time.append(e.value)
    txn_type.append(f.value)
    quantity.append(g.value)
    percentage_fee.append(h.value)

len(percentage_fee)