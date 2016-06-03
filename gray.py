import numpy as np
import cv2
import cv2.cv as cv
import os

path = ".\image2"

for i in os.listdir(path):
    img_path = os.path.join(os.getcwd(), 'image2', i)
    img = cv.LoadImage(img_path)
    grey = cv.CreateImage(cv.GetSize(img),8,1)
    cv.CvtColor(img, grey, cv2.COLOR_BGR2GRAY)
    cv.SaveImage(img_path, grey)