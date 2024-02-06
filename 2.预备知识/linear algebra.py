# 考试哩，完了又tm玩了2天文明，重点还没打完
#  @Time    : 2023/11/20 21:20
# 突然做了半天，才发现都是前面玩剩下的，下次复习直接跳过

# 标量的运算，之前好像写过
import torch
x = torch.tensor(3.0)
y = torch.tensor(2.0)
print(x + y, x * y, x / y, x**y)

# 向量的运算,好像也写过
x = torch.arange(4)
x = x.view(2, 2)
print(x)

# 矩阵，好像之前也写过
A = torch.arange(20).reshape(-1, 4)
print(A)
# 转置
print(A.t())

# 张量和它的运算
X = torch.arange(24).reshape(2, 3, 4)
print(X)

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = A.clone()  # 通过分配新内存，将A的一个副本分配给B
print(A, A + B)
# 或者可以这样
# A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
# B=A+A
# print(B)
# 降维
x = torch.arange(4, dtype=torch.float32)
print(x, x.sum())
# 点积

# 解释下代码，好像前面提到过，没有必要再解释一边
# 这段代码首先定义了一个张量 x，其包含从0到3的四个浮点数，
x = torch.arange(4, dtype=torch.float32)
# 然后定义了一个张量 y
y = torch.ones(4, dtype = torch.float32)
# 点积就是把它们对应相乘相加
print(x, y, torch.dot(x, y))

# 矩阵-向量积
A.shape, x.shape, torch.mv(A, x)
# 矩阵乘法
B = torch.ones(4, 3)
print(torch.mm(A, B))

# 还可以换成b和c
C = torch.ones(3, 5)
print(torch.mm(B, C))

# 做题
# 证明一个矩阵A的转置的转置是A
A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
print(A.t())
print(A.t().t())

# 给出两个矩阵A和B，证明“它们转置的和”等于“它们和的转置
A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = torch.arange(20, dtype=torch.float32).reshape(5, 4)
print(A.t() + B.t())
C = A + B
print(C.t())

