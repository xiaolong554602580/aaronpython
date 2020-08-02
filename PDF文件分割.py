#文本形式打開文件

from PyPDF2 import PdfFileReader,PdfFileWriter





def pdf_split(path):
	fname = 123
	pdf = PdfFileReader(path)#打開PDF文件。
	for page in range(pdf.getNumPages()):#遍歷PDF頁面
		pdf_writer = PdfFileWriter()
		pdf_writer.addPage(pdf.getPage(page))#重新寫入頁面碼
		output_filename = '{}_page_{}.pdf'.format(fname,page+1)#輸出文件名
		with open(output_filename,'wb') as out:
			pdf_writer.write(out)#重新寫入文件
			print('Created:{}'.format(output_filename))


path = ""
pdf_split(path)