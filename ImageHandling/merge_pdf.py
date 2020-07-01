import PyPDF2

with open('out_pdf.pdf','rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	with open('original.pdf','rb') as waterm:
		reader2 = PyPDF2.PdfFileReader(waterm)
		writer = PyPDF2.PdfFileWriter()
		for i in range(reader.getNumPages()):
			page = reader.getPage(i)
			page.mergePage(reader2.getPage(0))
			writer.addPage(page)
		with open('merged_pdf.pdf','wb') as outFile:
			writer.write(outFile)
