import xml.etree.ElementTree as ET
from random import shuffle
import xml.etree.ElementTree as ET
import os
import random
 


 
def xml_modification():

    files = os.listdir(ann_dir)
    for xml_file in files:
        if os.path.isfile(os.path.join(ann_dir, xml_file)):
            xml_path = os.path.join(ann_dir, xml_file)
            # print(xml_path)
 
            tree = ET.parse(xml_path)
            root = tree.getroot()
 
            for elem in root.iter('folder'):
                elem.text = 'voc2020'
 
            for elem in root.iter('filename'):
                pass
 
            for elem in root.iter('path'):
                path = elem.text
                filename = path.split('\\')[-1]
                new_path = img_dir + filename
                elem.text = new_path
 
            tree.write(xml_path)
 
            print("processed xml : %s" % (xml_path))
 

def generate_train_val_test_txt():

    total_xml = os.listdir(ann_dir)

    ftrain = open(os.path.join(save_Path, 'train.txt'), 'w')
    
    for i in total_xml:
        name = i[:-4] + '\n'
        ftrain.write(name)

    ftrain.close()



def convert_annotation(year, image_id, list_file):
    in_file = open('VOC%s/Annotations/%s.xml'%(year, image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))


if __name__ == '__main__':

    sets=[('2020', 'train')]

    classes = []
    
    file = open("./model_data/voc_classes.txt") 
    for line in file:
        if len(line) != 0 and line != "\n":
            if line.endswith("\n"):
                classes.append(line[:-1])
            else:
                classes.append(line)
    file.close()
     
    print(classes)

    #建立一下以下文件夹
    ann_dir = r"VOC2020\Annotations"
    img_dir = r"VOC2020\JPEGImages"  # 改成自己数据集JPEGImages文件夹绝对路径
    save_Path = r"VOC2020\ImageSets\Main"

    xml_modification()
    generate_train_val_test_txt()

    for year, image_set in sets:
        image_ids = open('VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
        list_file = open('%s.txt'%( image_set), 'w')
        for image_id in image_ids:
            list_file.write('VOC%s/JPEGImages/%s.jpg'%(year, image_id))
            convert_annotation(year, image_id, list_file)
            list_file.write('\n')
        list_file.close()
