# coding:utf-8


from os import listdir
from PIL import Image


class MergeLongImage:
    def __init__(self, images_path):
        self.images_path = images_path
    

    def getImages(self):
        '''
        获取当前文件夹下所以图片
        '''
        ims = [Image.open(self.images_path + "\\" + fn) for fn in listdir(self.images_path) if fn.endswith('.jpg') or fn.endswith('.png')]
        print(listdir(self.images_path))
        ims_size = [list(im.size) for im in ims]
        middle_width = sorted(ims_size, key=lambda im: im[0])[int(len(ims_size)/2)][0] # 中位数宽度
        ims = [im for im in ims if im.size[0] > middle_width/2] # 过滤宽度过小的无效图片
        # 过滤后重新计算
        ims_size = [list(im.size) for im in ims]
        middle_width = sorted(ims_size, key=lambda im: im[0])[int(len(ims_size)/2)][0] # 中位数宽度
        ims = [im for im in ims if im.size[0] > middle_width/2] # 过滤宽度过小的无效图片
        # 计算相对长图目标宽度尺寸
        for i in range(len(ims_size)):
            rate = middle_width/ims_size[i][0]
            ims_size[i][0] = middle_width
            ims_size[i][1] = int(rate*ims_size[i][1])
        sum_height = sum([im[1] for im in ims_size])
        # 创建空白长图
        result = Image.new(ims[0].mode, (middle_width, sum_height))
        # 拼接
        top = 0
        for i, im in enumerate(ims):
            mew_im = im.resize(ims_size[i], Image.ANTIALIAS) # 等比缩放
            result.paste(mew_im, box=(0, top))
            top += ims_size[i][1]
        # 保存
        result.save(self.images_path + '\\result.png')
        print('done')

if __name__ == "__main__":
    mainn = MergeLongImage(r'C:\Users\55460\Desktop\learnpython\images')
    mainn.getImages()