
## 配置
+ 修改cfg文件  classes为类别数量和它上面的filters为（class+5）*3
+ covert.py生成预训练模型
+ 修改train.py的anchors选择是tiny还是正常的  
+ 修改yolo.py的anchors 和train.py对应
+ 修改class.txt


## 训练
+ 创建2020文件夹结构

+ 运行voc_annatation.py

+ python train.py

## 识别
视频：
`python yolo_val.py --input D:\data\test.mp4`

图片:
`python yolo_val.py` 


## 查看日志

`tensorboard --logdir '/home/wsco/Downloads/yolo3/logs' &`


## requirement
`tensorflow-gpu==1.6.0`

`keras==2.1.5`

## 备注
github最大上传100m，yolov3.weights可以从网上找到下载