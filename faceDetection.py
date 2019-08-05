# -*- coding: utf-8 -*-

import cv2
import sys

# Get user supplied values 1.获取待识别图像地址，以及处理方式
imagePath = '4.jpg'#待识别的图像
cascPath = "haarcascade_frontalface_default.xml"

# Read the image 2.读取图片并灰度化以便于计算
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create the haar cascade  3.创建OpenCV人脸检测实例，加载相应的分类器xml
faceCascade = cv2.CascadeClassifier(cascPath)

# Detect faces in the image 4.检测图像，设置参数
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces 5.对识别的人脸进行标识
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 6.显示检测结果（展示图片）
cv2.imshow("Faces found", image)
cv2.waitKey(0)

# 其中cascPath =
#  "haarcascade_frontalface_default.xml"