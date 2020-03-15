# -*- coding: UTF-8 -*-
import os
import cv2
import time
import part1
import part2
import part3
import part4
# 图片合成视频

path ='/home/mally/图片/text'  #文件路径
size = (640,480)            #图片的分辨率片
fps = 3
file_path = "try"+ ".avi"  # 导出路径
fourcc = cv2.VideoWriter_fourcc('I', '4', '2', '0')  # 不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）
video = cv2.VideoWriter(file_path, fourcc, fps, size)

speed_bei=fps      #因为之前的fps为1,速度正好，现在新加了东西，故而要调速度
def read(name,num=1):
    img=cv2.imread(name)
    if num!=-1: num=num*speed_bei       #如果num-=-1,说明是要自己调节的加速版本
    else:num=1
    for i in range(num):video.write(img)

def picvideo():
# 存part1的图片

    read("picture/1.jpg",4)
    read("picture/2.jpg", 4)

    #1.基本信号
    read("picture/3.jpg", 4)
    part1.make_dirac()
    part1.dirac_step()
    part1.make_step_func()
    part1.step_rope()
    part1.make_rope_func()

    #2.时变和时不变

    read("picture/0.jpg", 4)
    read("picture/4.jpg", 4)
    read("picture/5.jpg", 5)
    read("picture/6.jpg", 6)
    read("picture/7.jpg", 4)
    read("picture/8.jpg", 10)

    part2.sig_f1()      #说明点动
    part2.sig_f2()      #说明平移
    part3.combin1()  # 对比y=f(t)
    read("picture/15.jpg", 5)
    read("picture/16.jpg", 4)
    part3.combin2()  # 对比y=f(-t)

#3.卷积
    read("picture/9.jpg", 4)
    read("picture/10.jpg", 4)
    read("picture/11.jpg", 5)
    read("picture/12.jpg", 4)
    read("picture/13.jpg", 5)
    read("picture/14.jpg", 4)
    part4.func1()
    read("picture/17.jpg", 4)


    video.release()  # 释放
        # cap=cv2.VideoCapture



