
from urllib.request import urlretrieve
import zipfile,os

url = "http://www.baidu.com"
urlretrieve(url, filename="./baidu.html", reporthook=None, data=None)

zippath = r'./test.zip'
destpath = r'./test1dir'

# 创建zipfile对象
with zipfile.ZipFile(zippath, 'r') as fzip:
    # 文件全部加压缩到destpath目录
    fzip.extractall(destpath)

result = os.system("./test.exe")