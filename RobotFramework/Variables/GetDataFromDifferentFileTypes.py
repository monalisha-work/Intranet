import xlrd
from docx import *
from docx.api import Document
import PyPDF2
from pptx import Presentation
import win32com.client

def Get_Excel_Sheet_Data(fileLocation):
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
	
def Get_Word_File_Data_From_Table(fileLocation):
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
	
def Get_PDFfile_Data(fileName):
	pdfFileObj = open(fileName, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	print(pdfReader.numPages)
	fileData = []
	for num in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(int(num))
		print("hey...") 
		print(pageObj.extractText())
		data = pageObj.extractText()
		fileData.append(data)
	return fileData	
