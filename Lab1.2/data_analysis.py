from matplotlib import pyplot
from openpyxl import load_workbook

book = load_workbook('data_analysis_lab.xlsx')
sheet = book['Data']

def getvalue(x): return x.value

pyplot.plot(list(map(getvalue,sheet['A'][1:])), list(map(getvalue,sheet['C'][1:])), label="Temp")
pyplot.plot(list(map(getvalue,sheet['A'][1:])), list(map(getvalue,sheet['D'][1:])), label="Activity")
pyplot.show()
