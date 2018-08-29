# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 16:29:54 2018

@author: 王永威
"""
'''
cv2的使用方法练习
'''


import cv2

#视频打开
video = cv2.VideoCapture(r'E:\Python\test2.mp4')

#视频读取
success,frame = video.read()
#视频编码
video_FourCC = int(video.get(cv2.CAP_PROP_FOURCC))
#获取视频帧数
video_fps = video.get(cv2.CAP_PROP_FPS)
#获取视频的宽高
video_size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#写入视频，电脑缺少编码器
#videoWriter = cv2.VideoWriter(r'E:\Python\test37.avi',video_FourCC,video_fps,video_size)
#-1是需要指定编码格式
videoWriter = cv2.VideoWriter(r'E:\Python\test36.avi',-1,video_fps,video_size)
while success:
    cv2.imshow('test22',frame)#显示视频
    cv2.waitKey(int(video_fps))#暂定
    
    videoWriter.write(frame)
    success,frame=video.read()#继续读取帧
  
#释放视频
cv2.destroyAllWindows()
video.release()
videoWriter.release()