import time

from PIL import Image,ImageDraw,ImageFont
#加载底图
print(time.time())
base_img = Image.open('9.png')#加载底图
# 可以查看图片的size和mode，常见mode有RGB和RGBA，RGBA比RGB多了Alpha透明度
#  print base_img.size, base_img.mode
box = (60, 44, 130, 120)  # 底图上需要P掉的区域
#加载需要P上去的图片
tmp_img = Image.open('12.png')#要粘贴的图可选择大小或整张
#这里可以选择一块区域或者整张图片
# region = tmp_img    #使用整张
#注意，region的大小必须和box的大小完全匹配。但是两张图片的mode可以不同，合并的时候回自动转化。如果#需要保留透明度，则使用RGMA mode
#提前将图片进行缩放，以适应box区域大小
tmp_img = tmp_img.rotate(180) #对图片进行旋转
tmp_img = tmp_img.resize((box[2] - box[0], box[3] - box[1]))
base_img.paste(tmp_img, box)
drawobj=ImageDraw.Draw(base_img)
text='hello world'
#位置 文本 颜色
drawobj.text([10,50],text,'red')
text='hello world'
#位置 文本 颜色
drawobj.text([30,70],text,'red')
text='hello world'
#位置 文本 颜色
drawobj.text([50,90],text,'red')
# base_img.show() # 查看合成的图片
print(time.time())
# base_img.save('./out.png') #保存图片
# print(time.time())
