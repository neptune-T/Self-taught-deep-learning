# @Time    : 2023/11/17 15:32
# 创建数据集csv文件
import os
import torch
# 创建data目录
os.makedirs(os.path.join('..', 'data'), exist_ok=True)
# 创建数据集csv路径
data_file = os.path.join('..', 'data', 'house_tiny.csv')
# 打开csv文件写入数据
with open(data_file, 'w') as f:
    # write写入列名和数据行：
    f.write('NumRooms,Alley,Price\n')  # 列名，表示房间数目，小巷类型，价格
    f.write('NA,Pave,127500\n')  # 第一行数据，表示没有房间数量数据（NA），小巷类型为铺设（Pave），价格为127500。
    f.write('2,NA,106000\n') # 后文同理
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')

# 如果没有安装pandas，只需取消对以下行的注释来安装pandas
# !pip install pandas
import pandas as pd
data = pd.read_csv(data_file)
print(data)

