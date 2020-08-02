# coding:utf-8
'''
一個獲取佰騰專利網的JSON文件，並寫入sqlite數據庫保存的腳本。
'''

import sqlite3
import json,os,time


class PatentsWrite(object):
	"""docstring for PatentsWrite"""
	def __init__(self,filesPath,databasePath,dataTable):
		super(PatentsWrite, self).__init__()
		self.filesPath = filesPath
		self.databasePath = databasePath
		self.dataTable = dataTable
		self.Patcount = 0
		self.main()

#-------------------------------------------------------------

	def main(self):
		#得到JSON文件目錄
		#打開單個文件讀取
		#獲取JSON文件的專利
		#整理出每條專利
		#寫入數據庫
		jsonFileDir = self.JsonFileDir(self.filesPath)
		filecount = len(jsonFileDir)
		for fileName in jsonFileDir:
			self.openJsonFile(fileName)
			filecount-=1
			print('還有{}個文件。'.format(filecount))
		print('完成了{}條專利'.format(self.Patcount))


#-------------------------------------------------------------
	#得到JSON文件目錄
	def JsonFileDir(self,filesPath):
		JsonFiles = []
		Files = os.listdir(filesPath)
		for JsonFile in Files:
			if os.path.splitext(JsonFile)[1] == ".json":
				JsonFiles.append(filesPath + "/" + JsonFile)
				print("獲取了{}文件；".format(JsonFile))
		print("總共得到了{}個文件。".format(len(JsonFiles)))
		time.sleep(3)
		return JsonFiles
#------------------------------------------------------------------
	#打開單個文件讀取
	def openJsonFile(self,fileName):
		panTypes = ['id','pn','ti','an','pd','ad','pa','in','ls1','ab','apn','apd','ic2','ic1','pr','aa','agc','agt','cty',\
				'ls1_2','ls2_1','cpa','type','lsnt','lsn2','lsn1','lset','lse','ain','co','ac']
		try:
			f = open(fileName,"r",encoding="utf-8-sig")
			jsonData = json.load(f)
		except:
			print("文件格式錯誤")
			pass
		else:
			jsonDatas = jsonData['cubePatentSearchResponse']['documents']
			print(len(jsonDatas))
			i = 0
			while i < len(jsonDatas):
				jsonData = jsonDatas[i]['field_values']
				for j in range(0,len(panTypes)):
					jsonData.setdefault(panTypes[j])
				#print(jsonData)
				self.DBconnect(jsonData)
				i+=1
			f.close()

#---------------------------------------------------------------------------
	#專利寫入數據庫
	def DBconnect(self,*jsonDatas):
		conn = sqlite3.connect(databasePath)
		c = conn.cursor()
		for jsonData in jsonDatas:
			id = jsonData['id']
			pn = jsonData['pn']
			ti = jsonData['ti']
			an = jsonData['an']
			pd = jsonData['pd']
			ad = jsonData['ad']
			pa = jsonData['pa']
			in1 = jsonData['in']
			ls1 = jsonData['ls1']
			ab = jsonData['ab']
			apn = jsonData['apn']
			apd = jsonData['apd']
			ic2 = jsonData['ic2']
			ic1 = jsonData['ic1']
			pr = jsonData['pr']
			aa = jsonData['aa']
			agc = jsonData['agc']
			agt = jsonData['agt']
			cty = jsonData['cty']
			ls1_2 = jsonData['ls1_2']
			ls2_1 = jsonData['ls2_1']
			cpa = jsonData['cpa']
			type = jsonData['type']
			lsnt = jsonData['lsnt']
			lsn2 = jsonData['lsn2']
			lsn1 = jsonData['lsn1']
			lset = jsonData['lset']
			lse = jsonData['lse']
			ain = jsonData['ain']
			co = jsonData['co']
			ac = jsonData['ac']
			updatetime = time.strftime("%Y%m%d",time.localtime())
			#id,pn,ti,an,pd,ad,pa,in,ls1,ab,apn,apd,ic2,ic1,pr,aa,agc,agt,cty,ls1_2,ls2_1,cpa,type,lsnt,lsn2,lsn1,lset,lse,ain,co,ac,
			sqlText = (str(id),str(pn),str(ti),str(an),str(pd),str(ad),str(pa),str(in1),str(ls1),str(ab),str(apn),str(apd),str(ic2),str(ic1),\
				str(pr),str(aa),str(agc),str(agt),str(cty),str(ls1_2),str(ls2_1),str(cpa),str(type),str(lsnt),str(lsn2),str(lsn1),str(lset),\
				str(lse),str(ain),str(co),str(ac),updatetime)
			#INSERT OR IGNORE/REPLACE
			c.execute("INSERT OR IGNORE INTO patents VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",sqlText)
			print("專利申請號：{}，寫入成功；".format(id))
			self.Patcount += 1
			conn.commit()
		conn.close()

if __name__ == '__main__':
	filesPath = "C:/Users/55460/Desktop/20200425json"
	databasePath = "C:/Users/55460/Desktop/script/data.sqlite"
	dataTable = "patents"
	PatentsWrite(filesPath,databasePath,dataTable)
