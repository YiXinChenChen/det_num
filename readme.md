使用说明：


文件夹：
	image*：存放训练的数字样本
	test： 测试图片

文件：
	source_data.txt：监督学习对应的路径和标签
	svm_data.xml： 训练得到的SVM文件
	read.py：生成source_data.txt文件
	gray.py：把图片变成灰度图片

	det_num.py：主函数，导入处理测试图片
	square.py：找到数字对应的矩阵
	segmentation.py：切割数字
	SVM.py：识别数字


