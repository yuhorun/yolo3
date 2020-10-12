import os

annotations_dir = './VOC2020/Annotations'
JPEGImages_dir = './VOC2020/JPEGImages'

annotations_filelist = os.listdir('./VOC2020/Annotations') 
JPEGImages_filelist = os.listdir('.//VOC2020/JPEGImages')

# try:
#     os.rename(srcFile,dstFile)
# except Exception as e:
#     print(e)
#     print('rename file fail\r\n')
# else:
#     print('rename file success\r\n')

for i in annotations_filelist:
    new_name = i.replace(' ', '_')
    try:
        os.rename(os.path.join(annotations_dir,i),os.path.join(annotations_dir,new_name))
    except Exception as e:
        print(e)

for i in JPEGImages_filelist:
    new_name = i.replace(' ', '_')
    try:
        os.rename(os.path.join(JPEGImages_dir,i),os.path.join(JPEGImages_dir,new_name))
    except Exception as e:
        print(e)