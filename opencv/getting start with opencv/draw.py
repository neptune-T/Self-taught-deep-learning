import cv2
import numpy as np
# 添加画布
image = np.zeros((512, 512, 3), dtype=np.uint8)
# 画图
# 画圆，坐标，半径，颜色，线宽
cv2.circle(image, (256, 256), 100, (255, 0, 0), -1)
# 画线，坐标，颜色，线宽
cv2.line(image,(100,200),(250,250),(0,0,255),3)
# 写字，坐标，字体，字体大小，颜色，线宽
cv2.putText(image, 'Hello World', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
# 画矩形，坐标，宽，高，颜色，线宽
cv2.rectangle(image, (100, 100), (200, 200), (0, 255, 0), 2)
# 画椭圆，坐标，长宽，角度，颜色，线宽
cv2.ellipse(image, (256, 256), (100, 50), 0, 0, 360, (0, 255, 0), 2)

cv2.imshow('image', image)
cv2.waitKey()