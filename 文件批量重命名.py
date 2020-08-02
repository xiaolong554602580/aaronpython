import json,os,re
import time

#------------------------------------------------------------------------------------------------------
#批量文件重命名
def dirFileRename(FilePath):
	listDir = os.listdir(FilePath)
	for listD in listDir:
		if os.path.splitext(listD)[1] == ".pdf":
			osp = os.path.splitext(listD)[0]
			pat = re.match(r'^CN[0-9]*',osp,re.I)
			oldName = FilePath+"\\"+listD
			newName = FilePath+"\\"+pat.group()+".pdf"

			os.rename(oldName,newName)
			time.sleep(1)
#------------------------------------------------------------------------------------------------------
if __name__ =="__main__":
	dirFileRename(r"d:\aaronmo\Desktop\虎彩")
