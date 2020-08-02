# coding:utf-8


import openpyxl
import sqlite3


#File_Path=r'C:\Users\55460\Desktop\patents.xlsx'

#wb=openpyxl.load_workbook(File_Name)
#ws = wb.active


def Write_Data(Sql_Path,*Test_list):
    conn = sqlite3.connect(Sql_Path)
    print('Opened database successfully')
    c=conn.cursor()
    #创建列表
    '''c.execute(CREATE TABLE COMPANY(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL,ADDRESS CHAR(50),SALARY REAL);)
    print('Table created successfully')'''
    #写入数据
    c.execute("INSERT OR IGNORE INTO COMPANY VALUES(?,?,?,?,?)",Test_list)
    print("Records created successfully")
    #更新任何记录
    #c.execute("UPDATE COMPANY SET SALARY=25000.787 WHERE ID=1")
    #删除记录
    #c.execute("DELETE from COMPANY where ID=2;")
    conn.commit()
    #查寻数据
    cursor = c.execute("SELECT ID,NAME,ADDRESS,SALARY FROM COMPANY")
    for row in cursor:
        print("id=",row[0])
        print("name=",row[1])
        print("address=",row[2])
        print("salary=",row[3])
    #conn.commit()
    conn.close()

Write_Data("thistest.db",[1,'333','111','你好吗',30304.98])
