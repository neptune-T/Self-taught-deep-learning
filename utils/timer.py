import time
import numpy as np
# 定义计时器，性能分析
class Timer:  #@save
    """记录多次运行时间"""
   # 它初始化一个空的列表，存储每次运行时间的记录
    def __init__(self):
        self.times = []
        self.start()
   # 计时的起点
    def start(self):
        """启动计时器"""
        self.tik = time.time()
   # 每次调用 stop() 方法都会记录一次运行时间。方法返回最新记录的时间间隔。
    def stop(self):
        """停止计时器并将时间记录在列表中"""
        self.times.append(time.time() - self.tik)
        return self.times[-1]
   # 记录所有记录时间的平均值
    def avg(self):
        """返回平均时间"""
        return sum(self.times) / len(self.times)
   # 所有记录时间的总和
    def sum(self):
        """返回时间总和"""
        return sum(self.times)

    def cumsum(self):
        """返回累计时间"""
        return np.array(self.times).cumsum().tolist()

# 在使用计时器的时候写以下代码。
# from utils.timer import Timer
# t = Timer()
# ...运行一些代码...
# t.stop()
# print(f"Average time per run: {t.avg()} seconds")

