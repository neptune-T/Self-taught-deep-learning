import cv2
import numpy as np

# 读取图像
image = cv2.imread('j.jpg', cv2.IMREAD_GRAYSCALE)

# 定义腐蚀核大小
kernel_size = 5

# 创建腐蚀核
kernel = np.ones((kernel_size, kernel_size), np.uint8)

# 进行腐蚀操作
erosion_result = cv2.erode(image, kernel, iterations=1)

# 保存腐蚀后的图像
cv2.imwrite('erosion_result.jpg', erosion_result)

# 定义膨胀核大小
kernel_size = 5

# 创建膨胀核
kernel = np.ones((kernel_size, kernel_size), np.uint8)

# 进行膨胀操作
dilation_result = cv2.dilate(image, kernel, iterations=1)

# 保存膨胀后的图像
cv2.imwrite('dilation_result.jpg', dilation_result)

# 开运算
def opening(image, kernel_size):
    # 创建腐蚀核
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # 进行腐蚀操作
    erosion_result = cv2.erode(image, kernel, iterations=1)

    # 进行膨胀操作
    dilation_result = cv2.dilate(erosion_result, kernel, iterations=1)

    # 保存开运算结果
    cv2.imwrite('opening.jpg', dilation_result)

# 闭运算
def closing(image, kernel_size):
    # 创建膨胀核
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # 进行膨胀操作
    dilation_result = cv2.dilate(image, kernel, iterations=1)

    # 进行腐蚀操作
    erosion_result = cv2.erode(dilation_result, kernel, iterations=1)

    # 保存闭运算结果
    cv2.imwrite('closing.jpg', erosion_result)

# 显示图片
cv2.imshow('image', image)
cv2.imshow('erosion_result', erosion_result)
cv2.imshow('dilation_result', dilation_result)

# 执行开运算和闭运算
opening(image, kernel_size)
closing(image, kernel_size)

# 显示开运算和闭运算的结果
opening_result = cv2.imread('opening.jpg')
closing_result = cv2.imread('closing.jpg')
cv2.imshow('opening_result', opening_result)
cv2.imshow('closing_result', closing_result)

# 等待按键后退出
cv2.waitKey(0)
cv2.destroyAllWindows()

