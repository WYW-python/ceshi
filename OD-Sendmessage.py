# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 13:44:51 2018

@author: 王永威
"""
'''
文件位置为E:\Python
人数超标，短信发送
采用requests
'''

from imageai.Detection import ObjectDetection
import os
import time
import requests
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

in_path = r'E:\Python\test.jpg'
out_path = r'E:\Python\test0830.jpg'
    
detections = detector.detectCustomObjectsFromImage(input_image=os.path.join(execution_path , in_path),\
                                                   output_image_path=os.path.join(execution_path , out_path), \
                                                   minimum_percentage_probability=40)
    
count = 0
for eachobject in detections:
    if eachobject['name'] == 'person':
        count = count + 1     

if count >3:
    url = "http://apis.renxinl.com:8080/smsgate/varsend.do?user=15629016275&pwd=100200&params=15107181370,%d,&mid=19680&extno=123&sendtime=" %(count)
    req = requests.get(url)
    #print(req.text)


'''
for eachObject in detections:
   print(eachObject["name"] + " : " + eachObject["percentage_probability"] )
   print("--------------------------------")
   
from IPython.display import Image
Image("test_new2.jpg")
'''

end_time = time.time()

print('Totally cost time',end_time - start_time)