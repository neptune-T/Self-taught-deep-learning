import cv2
import os

# 读取图像
image = cv2.imread('photo.jpg')
# 应用均值滤波
# 可以调整kernel_size来改变滤波效果
kernel_size = (5, 5)
blurred_image = cv2.blur(image, kernel_size)
# 显示原图和滤波后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
# 等待按键后退出
cv2.waitKey(0)
cv2.destroyAllWindows()
