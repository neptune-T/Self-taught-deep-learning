# opencv使用笔记

### opencv的图像处理

怎么在`ide`中打开一个照片？

```
# 读取图像,img是变量名
img = cv2.imread('logo.jpg')
# 打印图像的维度，这里的3是指的是图像的通道数，这里是灰度图像，所以是3
print(img.shape)
# 显示图像
cv2.imshow('img', img)
# 等待按键
cv2.waitKey(0)
```

最后一行添加的原因是因为不添加确实打开了，但是一闪而过了，不会在显示屏上显示东西，添加之后按任意键关闭。

#### 显示原理

计算机对于图像色彩的描述普遍使用了`RGB`3色原理。对于`opencv`来说，存贮一张彩色照片等于存储3张灰度图像。被存贮在opencv的第三个维度上，灰度范围是0～255。

`opencv`对颜色的存贮顺序是`BGR`与平时常见的顺序相反。当显示器显示这张图片的时候，计算机会依次取出这张图片的3张灰度图像，分别投影到显示器的蓝色，绿色和红色的LED芯片之上，从而渲染彩色画面。

![image-20231201211340186](/home/plote/.config/Typora/typora-user-images/image-20231201211340186.png)

这里我们需要取出照片的`RGB`3色，只需要将第三维数值打出来就好了。

```
# 图像的灰度化处理
img_gray= cv2.imread('logo.jpg')
cv2.imshow('blue', img_gray[:,:,0])
cv2.imshow('green', img_gray[:,:,1])
cv2.imshow('red', img_gray[:,:,2])
```

opencv提供算法：可以把3个彩色通道的图像作平方和加权平均。得到的图像实际上也描述了图像的明暗分布。

在计算机视觉上，我们把这个图片也叫做灰度图。

```
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
```

![image-20231202194529980](/home/plote/.config/Typora/typora-user-images/image-20231202194529980.png)

#### 图像的剪切

没什么好说的，在这里用到了`crop`函数对图像进行剪切。

```
image = cv2.imread('logo.jpg')
crop = image[100:200, 40：233]
cv2.imshow('crop', crop)
cv2.waitKey(0)
```

而剪切对应的规则是先横行后纵列，这里的`100：200`对应的是图像第100横行到第200横行；这里的`40：233`对应的是第40列到第233列。



