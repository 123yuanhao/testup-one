import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\fruit_price.xlsx'

wb1 = opx.load_workbook(p + f1)
ws1 = wb1['Sheet1']

# 从第2行开始按行读取数据，有几行读取几行
r = []
for n in ws1.iter_rows():
    t = []
    for c in n:
        t.append(c.value)
    r.append(t)

print(r)
wb1.close()
