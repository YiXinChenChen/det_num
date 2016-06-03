# -*- coding: utf-8 -*-
import string
import numpy as np
import cv2


def train():
    svm_params = dict(kernel_type=cv2.SVM_LINEAR,
                      svm_type=cv2.SVM_C_SVC,
                      C=2.67, gamma=5.383)

    nLine = 0
    img_catg = list()  # lables1 or 0
    img_path = list()
    svm_data = open('.\source_data.txt')  # 训练样本路径和监督参数
    for line in svm_data.readlines():
        line = line.strip()
        nLine += 1
        if nLine % 2 == 0:
            img_catg.append(string.atoi(line))
        else:
            img_path.append(line)
    svm_data.close()

    nImgNum = nLine / 2
    print nImgNum
    data_mat = list()

    n = 0
    hog = cv2.HOGDescriptor((64,64), (16,16), (8,8), (8,8), 9)
    for path in img_path:
        img = cv2.imread(path)
        img = cv2.resize(img,(64,64))
        # print img.shape
        if not img.any():
            print " can not load the image: " + path + "\n"
            continue
        # print " processing " + path

        r = ((1, 2),)
        desc = hog.compute(img, hog.blockStride, hog.cellSize, r)
        data_mat.append(desc)

    trainData = np.array(np.float32(data_mat))
    responses = np.float32(np.array(img_catg))
    svm = cv2.SVM()
    svm.train(trainData, responses, params=svm_params)
    svm.save('svm_data.xml') #得到识别文件

def predict(img_path):
    svm = cv2.SVM()
    svm.load('.\svm_data.xml') #加载训练文件
    img = img_path

    img = cv2.resize(img, (64,64))

    # cv2.imshow("2", img)
    # ch = 0xFF & cv2.waitKey()

    hog = cv2.HOGDescriptor((64,64), (16,16), (8,8), (8,8), 9)
    r = ((1, 2),)
    h = hog.compute(img, hog.blockStride, hog.cellSize, r)
    p = svm.predict(h)
    return int(p)


if __name__ == "__main__":
     pass
     # train()
     # predict()
