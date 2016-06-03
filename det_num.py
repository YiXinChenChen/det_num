# -*- coding: utf-8 -*-

import numpy as np
import cv2
import square
import segmentation

def  img_process(img):
    shape =  img.shape
    heigth = shape[0]
    width = shape[1]

    sole = 720.0/heigth

    img = cv2.resize(img,(int(round(width*sole)),720))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #图片旋转
    # transport = cv2.transpose(img)
    # img = cv2.flip(transport,0)

    return img

if __name__ == '__main__':
    from glob import glob
    for fn in glob('./test/*.bmp'):
        img = cv2.imread(fn)
        img = img_process(img)


        roi = square.find_squares(img)
        cv2.imshow("squares", roi)

        Num = segmentation.segmentation(roi)
        Num.reverse()

        print Num


        ch = 0xFF & cv2.waitKey()
        if ch == 27:
            break

    cv2.destroyAllWindows()
