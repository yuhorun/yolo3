import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image

def detect_img(yolo):
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    
    if len(sys.argv) !=2 :
        print("请输入正确的参数, eg:  python detect_video.py 'd:/video/test.mp4'")
        exit(0)
    input_path = sys.argv[1]
    out_path = "./out/" + os.path.basename(input_path)
    detect_video(YOLO(), input_path, out_path)
