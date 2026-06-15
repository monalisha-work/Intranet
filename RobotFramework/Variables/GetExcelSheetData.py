import xlrd
from docx import *
from docx.api import Document

def excel_sheet_data(fileLocation):
	wb = xlrd.open_workbook(fileLocation)
	sheet = wb.sheet_by_index(0)
	columnList = []
	for row in range(1, 15):
		cellValue = sheet.cell_value(row, 1)
		if cellValue=='':
			pass
		else:
			columnList.append(cellValue)
	return columnList
	
def word_file_data(fileLocation):
	document = Document(fileLocation)
	table = document.tables[0]
	fileContentList = []
	for rw in table.rows:
		value = rw.cells[0].text
		if value=='':
			pass
		else:
			fileContentList.append(value)
	print(fileContentList)
	return fileContentList