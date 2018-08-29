# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 08:51:45 2018

@author: 王永威
"""
'''
采用imageai进行目标检测
模型采用RetinaNET
权重是resnet50_coco_best
批量测试图片，将测试图片输出
如果是人，为TRUE，其他为FALSE
图片序列有规律

'''

from imageai.Detection import ObjectDetection
import os
import time
start_time = time.time()


execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
#custom_objects = detector.CustomObjects(person=True, car=False)
#detections = detector.detectCustomObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"),\
#                                                   output_image_path=os.path.join(execution_path , "image3_new.jpg"), \
#                                                   custom_objects=custom_objects, minimum_percentage_probability=50)

for i in range(470):
    in_path = r'E:\Python\ceshishipin\xulie-01%03d.jpg'%(i)
    out_path = r'E:\Python\ceshishipin3\xulie-01%03d.jpg'%(i)
    #print(inpath)
    
    detections = detector.detectCustomObjectsFromImage(input_image=os.path.join(execution_path , in_path),\
                                                   output_image_path=os.path.join(execution_path , out_path), \
                                                   minimum_percentage_probability=40)
    

end_time = time.time()

print('Totally cost time',end_time - start_time)