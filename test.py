# -*- coding: utf-8 -*-

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '*********'
API_KEY = '************'
SECRET_KEY = '***********'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(r'C:\Users\55460\Desktop\Snipaste_2020-07-16_17-53-40.png')

""" 调用通用文字识别, 图片参数为本地图片 """


print(client.basicGeneral(image))