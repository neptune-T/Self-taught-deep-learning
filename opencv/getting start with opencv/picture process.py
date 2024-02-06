# @Time : 2023/12/1 20:40
import cv2
# 验证安装的opencv版本
print('OpenCV Version:', cv2.__version__)

# 读取图像,img是变量名
img = cv2.imread('photo/logo.jpg')
# 打印图像的维度，这里的3是指的是图像的通道数，这里是灰度图像，所以是3
print(img.shape)
# 显示图像
cv2.imshow('img', img)

# 图像的灰度化处理
img_gray= cv2.imread('logo.jpg')
cv2.imshow('blue', img_gray[:,:,0])
cv2.imshow('green', img_gray[:,:,1])
cv2.imshow('red', img_gray[:,:,2])


# 彩色图像的灰度变换算法
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# 等待按键
cv2.waitKey(0)

# 图像的剪切
image = cv2.imread('logo.jpg')
crop = image[100:200, 40:233]
cv2.imshow('crop', crop)
cv2.waitKey(0)