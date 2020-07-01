import PyPDF2
i=0
with open('./PDF/Aadhar.pdf', 'rb') as aadhar:
	reader = PyPDF2.PdfFileReader(aadhar)
	with open('./PDF/License.pdf', 'rb') as license:
		reader2 = PyPDF2.PdfFileReader(license)
		writer = PyPDF2.PdfFileWriter()
		with open('out_pdf.pdf','wb') as out_pdf:
			while i<reader.getNumPages():
				page = reader.getPage(i)
				writer.addPage(page)
				i+=1
			i=0	
			while i<reader2.getNumPages():
				page = reader2.getPage(i)
				writer.addPage(page)
				i+=1
			writer.write(out_pdf)