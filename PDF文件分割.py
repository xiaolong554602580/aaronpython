#PDF文件小工具（分割、合并）

from PyPDF2 import PdfFileReader,PdfFileWriter
import os


class PDFSplitTool():
	'''
	这是PDF文件分割的代码
	'''
	def __init__(self,PDFPath):
		self.PDFPath = PDFPath
		self.judgmentPath()

		

	def judgmentPath(self):
		'''
		判断路径是目录还是单个，如果路径是目录，就遍历分割全部PDF文件，如果是路径是文件，则分割单个文件 		
		'''
		if os.path.isdir(self.PDFPath):
			print('This is dir')
			self.judgDir()
		elif os.path.isfile(self.PDFPath):
			print('This is file')
			self.splitPDF(self.PDFPath)
		else:
			print('Nothing')
			
	def splitPDF(self,PDFPath):

		'''
		分割文件的主代码
		'''
		filePath,tempfilename = os.path.split(PDFPath)
		PDFReader = PdfFileReader(PDFPath)
		i = 0
		for page in range(i,PDFReader.getNumPages()):
			PDFWriter = PdfFileWriter()#循环创建空白的pdf
			#print(page)
			PDFWriter.addPage(PDFReader.getPage(page))#空白页增加PDF
			outdir = os.path.join(filePath,"分割文件")
			#print(outdir)
			if not os.path.exists(outdir):
				os.mkdir(outdir)
			PDFWriter.write(open(os.path.join(outdir,tempfilename[:-3]+'P{}.pdf').format(page+1),'wb'))

	def judgDir(self):
		'''
		判断路径类型后，遍历并分割全部PDF文件
		'''
		listfilename = os.listdir(self.PDFPath)
		#print(listfilename)
		for name in listfilename:	
			if name[-4:] == '.pdf':
				getFile = os.path.join(self.PDFPath,name)
				#print(getFile)
				self.splitPDF(getFile)
				print('{}已经完成分割'.format(name))


class PDFMergerTool():
	def __init__(self,PDFPath):
		self.PDFPath = PDFPath




if __name__ == "__main__":
	PDFSplitTool(r'C:\Users\55460\Desktop\files')
	

