import xlrd
data = xlrd.open_workbook("E:\kkkk.xlsx")  # 括号内填xls文件路径
table = data.sheets()[1]
nrows = table.nrows
for i in range(nrows):
    if i == 0:
        continue
    print(table.row_values(i)[:7])