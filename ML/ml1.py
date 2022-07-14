# 导入matplotlib和sklearn库，这两个库在后面的课程中会经常用到
import matplotlib.pyplot as plt
from sklearn import datasets

# 取出sklearn里面的手写识别图片
digits = datasets.load_digits()

# 将这些手写识别图片部分画出
row_num, col_num = 4, 6 # 总共4行，每行6张图片
_, axes = plt.subplots(row_num, col_num, subplot_kw=dict(xticks=[], yticks=[]))
images_and_labels = list(zip(digits.images, digits.target))
for i in range(row_num):
	for j in range(col_num):
		(image, label) = images_and_labels[i*col_num+j]
		axes[i, j].imshow(image.reshape((8, 8)), cmap=plt.cm.binary) # 图片为8*8的灰度图
		axes[i, j].set_title('label = %i' % label)

plt.show() # 显示上面的绘制结果```