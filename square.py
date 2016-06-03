# -*- coding: utf-8 -*-

import numpy as np
import cv2


def angle_cos(p0, p1, p2): #计算矩阵夹角
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def horizontal(p0,p1): #矩阵是否水平
    d1, d2 = abs(p0[0]-p1[0]), abs(p0[1]-p1[1])
    return min(d1,d2)

def isDigit(p0, p2): #判断是否是数字所在的矩形
    d1, d2 = abs(p0[0]-p2[0]), abs(p0[1]-p2[1])
    if d1/d2 >=2 and d1/d2 <2.5:
        return True
    else:
        return False


def rectu(p0, p2): #返回一个矩形
    w, h = abs(p2[0]-p0[0]), abs(p2[1]-p0[1])
    x = p0[0]+3
    y = p0[1]+3
    rect = (x, y, int(w-w*0.02), int(h-h*0.02))
    return rect

def find_squares(img):
    img = cv2.GaussianBlur(img, (5, 5), 0)
    lists = []
    for thrs in xrange(0, 255, 26):
        if thrs == 0:
            bin = cv2.Canny(img, 0, 50, apertureSize=5)  #边缘化
            bin = cv2.dilate(bin, None) #膨胀
        else:
            retval, bin = cv2.threshold(img, thrs, 255, cv2.THRESH_BINARY)

        contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #得到轮廓

        for cnt in contours:

            cnt_len = cv2.arcLength(cnt, True) #计算轮廓长度
            cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
            if len(cnt) == 4 and cv2.contourArea(cnt) > 500 and cv2.isContourConvex(cnt):
                cnt = cnt.reshape(-1, 2)

                max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)]) #计算矩阵夹角是否90°

                if max_cos < 0.1 and horizontal(cnt[0],cnt[1]) <5 and isDigit(cnt[0],cnt[2]) :
                    a = cnt.tolist()
                    if a not in lists:
                        lists.append(cnt.tolist())
                        rect = rectu(cnt[0],cnt[2])
                        roi = img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]

                    if len(lists) > 0:
                        break
        if len(lists) > 0:
            break


    return roi

if __name__ == "__main__":
    pass