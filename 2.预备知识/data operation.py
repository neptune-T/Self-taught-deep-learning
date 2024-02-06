# @Time    : 2023/11/15 21:32
import torch
# 创建一个包含从0到11的12个整数的一维张量
x = torch.arange(12)
# 查询张量的形状，这将返回一个元组，表示张量的维度
x.shape
# 将一维张量重塑为3行4列的二维张量，不改变数据的总数
x.view(3,4)
# 将张量重塑，这里的-1表示可以根据其他维度推断出维度，3表示行数
# 在此处，根据3的值推断，是3行4列，所以输出为3行4列的二维张量
x.view(-1,3)
print(x.view(-1,3))

# 甚至哥们还能换个函数表示，比如reshape
x.reshape(-1,4)
print(x.reshape(-1,4))
x.reshape(6,-1)
print(x.reshape(6,-1))

# 张量的形状也可以通过torch.zeros()函数来创建,创建一个形状为（2，3，4）的全零张量
torch.zeros((2, 3, 4))
print(torch.zeros((2, 3, 4)))

torch.ones((1, 3, 2))
print(torch.ones((1, 3, 2)))

# 未初始化的张量，这里出来的都是随机，未定义的浮点数，通常需要自己填充
torch.empty((2, 3, 4))
print(torch.empty((2, 3, 4)))

torch.randn(3, 4)
print(torch.randn(3, 4))

torch.zeros((1, 3, 2))
print(torch.zeros((1, 3, 2)))

torch.ones((1, 3, 3))
print(torch.ones((1, 3, 3)))

# 运算之加减乘除
x = torch.tensor([1,2,4,8])
y = torch.tensor([2,5,8,4])
x+y,x-y, x*x, y*y
print(x+y,x-y, x*x, y*y)

x.view(-1,2)
y.view(-1,2)
x.view(-1,2) + y.view(-1,2)
print(x+y,x-y, x*x, y*y,x*y,x@y)

x_reshaped = x.view(-1, 2)
y_reshaped = y.view(-1, 2)
result = x_reshaped @ y_reshaped.T  # 注意：为了进行矩阵乘法，需要转置其中一个张量
print(result)

# 多个张量相连
X = torch.arange(12, dtype=torch.float32).reshape((3,4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
torch.cat((X, Y), dim=0), torch.cat((X, Y), dim=1)
print(torch.cat((X, Y), dim=0))
print(torch.cat((X, Y), dim=1))

# 首先，将二维张量扩展为三维张量，'unsqueeze'方法可以在指定位置添加一个维度
X_3d = X.unsqueeze(2)  # 这会将X变为一个形状为(3, 4, 1)的张量
Y_3d = Y.unsqueeze(2)  # 这会将Y变为一个形状为(3, 4, 1)的张量

# 现在可以在第三个维度（dim=2）上进行拼接
result_dim2 = torch.cat((X_3d, Y_3d), dim=2)

# 打印结果
print(result_dim2)
# 布尔值
x==y
print(X==Y)

# 广播机制
X = torch.arange(12, dtype=torch.float32).reshape((4,3))
Y = torch.tensor([2.0, 1, 4])
X+Y
print(X+Y)

# 索引和切片
X[-1], X[1:3]
print(X[-1], X[1:3])
X[1, 2] = 110
print(X)

# 转化成其他对象
A = X.numpy()
B = torch.tensor(A)
type(A), type(B)
a = torch.tensor([3.5])
a, a.item(), float(a), int(a)
print(a, a.item(), float(a), int(a))