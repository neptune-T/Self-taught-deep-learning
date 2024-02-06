import cv2

# 读取照片
image = cv2.imread('photo.jpg')

# 应用高斯滤波
# 第二个参数是高斯核的大小，必须是正的奇数
# 第三个参数是标准差，如果为0，则根据核大小自动计算
gaussian_blur = cv2.GaussianBlur(image, (9, 7), 0)

# 显示原图和滤波后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Gaussian Blurred Image', gaussian_blur)

# 等待按键后退出
cv2.waitKey(0)
cv2.destroyAllWindows()
