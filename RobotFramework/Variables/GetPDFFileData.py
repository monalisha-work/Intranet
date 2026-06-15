import PyPDF2

def get_PDFfile_data(fileName):
	pdfFileObj = open(fileName, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	print(pdfReader.numPages)
	pageObj = pdfReader.getPage(4)
	print(pageObj.extractText())
	fileContent	= pageObj.extractText()
	return fileContent	
	
def create_new_file(file_name, content):
	file = open(file_name, "w+")
	file.write(content)
	
def get_data_from_new_file(file_name):	
	file = open(file_name, "r")
	file_Content = file.read()
	return file_Content	