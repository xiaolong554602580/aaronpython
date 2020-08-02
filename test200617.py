# coding:utf-8
TemStr=input('plase input your trmp')
if TemStr[-1] in ['F','f']:
    c= (eval(TemStr[0:-1])-32)/1.8
    print('转换后的温度是{:.2f}c'.format(c))
elif TemStr[-1] in ['C','c']:
    c= (eval(TemStr[0:-1])-32)/1.8
    print('转换后的温度是{:.2f}F'.format(c))
else:
    print('输入错误')