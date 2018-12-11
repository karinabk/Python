import PyPDF2


if __name__=='__main__':
	pdfFileObj = open('pdf-sample.pdf','rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
	  
	# printing number of pages in pdf file 
	print(pdfReader.numPages) 
	  
	# creating a page object 
	pageObj = pdfReader.getPage(0) 
	  
	# extracting text from page 
	print(pageObj.extractText()) 
	  
	# closing the pdf file object 
	pdfFileObj.close() 
	
	
