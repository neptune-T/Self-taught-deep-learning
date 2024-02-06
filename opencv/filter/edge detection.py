import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
image = cv2.imread('9.jpg')

# 转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 应用高斯滤波以减少噪声
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# 使用Canny算法进行边缘检测
# 这里的两个阈值可以根据需要进行调整
canny_edges = cv2.Canny(blurred_image, 100, 200)

# 显示原图和边缘检测后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', canny_edges)

# 等待按键后退出
cv2.waitKey(0)
cv2.destroyAllWindows()
