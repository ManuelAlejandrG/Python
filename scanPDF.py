import PyPDF2
read_pdf = PyPDF2.PdfFileReader('1.pdf')
number_of_pages = read_pdf.getNumPages()
#print(number_of_pages)
page = read_pdf.getPage(0)
page_content = page.extractText()

print (page_content)
