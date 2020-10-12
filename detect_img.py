import sys
import os
import argparse
from yolo import YOLO, detect_video
from PIL import Image

def detect_img(yolo,img):

    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        exit(0)
    else:
        r_image = yolo.detect_image(image)
        img_name = os.path.basename(img)
        r_image.save("./out/"+img_name)
        r_image.show()
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':

    print(sys.argv)

    if len(sys.argv)!=2:
        print("请输入图片所在路径，eg：python detect_img.py 'D:/images/test.jpg'\n")
        exit(0)
    
    detect_img(YOLO(),sys.argv[1])
