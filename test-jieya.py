import zipfile
 
f = zipfile.ZipFile("/home/u202120081002013/ACM-Net/data/ActivityNet13/test.zip",'r') # 压缩文件位置
for file in f.namelist():
    f.extract(file,"/home/u202120081002013/ACM-Net/data/ActivityNet13")               # 解压位置
f.close()