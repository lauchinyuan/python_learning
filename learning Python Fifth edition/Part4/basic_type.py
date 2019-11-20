# 基本对象类型
import math
import random
a = 2**100
print(a)
# print(len(str(2**1000000)))
print(math.pi)  # 圆周率
print(random.random())
rc = random.choice([1, 2, 3, 4])  # 随机选取
print(rc)

# 序列操作
S = 'Spam'  # 字符串
lens = len(S)
print(lens, S[0], S[1])  # 索引从0开始
print(S[-1])  # Python支持反向索引，结果为'm'
print(S[len(S)-1])  # 负的索引号本质上是和字符串长度相加
print(S[1:3])  # 分片（Slice）操作，结果为'pa'，返回一个新对象
print(S[:3])  # 左分片默认为0
print(S[1:])  # 右分片默认为分片序列长度
print(S[:])  # 相当于复制字符串






