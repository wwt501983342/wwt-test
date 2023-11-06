import zipfile
 
f = zipfile.ZipFile("./train1.zip",'r') # 压缩文件位置
for file in f.namelist():
    f.extract(file,"./train")               # 解压位置
f.close()

f2 = zipfile.ZipFile("./train2.zip",'r') # 压缩文件位置
for file in f2.namelist():
    f2.extract(file,"./train")               # 解压位置
f2.close()