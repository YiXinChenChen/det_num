# -*- coding: utf-8 -*-

import cv2
import SVM

# 分割数字
def segmentation(img_path):
    Num =[]
    img = img_path
    # img =cv2.imread(img_path)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval,bin =cv2.threshold(img, 200, 255, cv2.THRESH_BINARY);

    contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    j =0
    for i in contours:
        j+=1
        cnt_len = cv2.arcLength(i, True)
        if cnt_len>100 and cnt_len<200 :
            x,y,w,h = cv2.boundingRect(i)
            roi = img[y:y+h, x:x+w]
            Num.append(SVM.predict(roi))

    return Num



if __name__ =="__main__":
    pass
