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

# 不可变性
# S[0] = 'z'  # 错误字符串内容无法改变
S = 'z' + S[1:]  # 产生新对象即可等效为改变
print(S)
S = 'shrubbery'
L = list(S)  # 将字符串扩展为由独立字符构成的列表
print(L)
L[1] = 'c'  # 列表对象可变
nc = ''.join(L)  # 通过改变列表对象来间接建立一个新的字符串对象
print(nc)

B = bytearray(b'spam')  # 通过bytearray实现序列操作
B.extend(b'eggs')
print(B)  # 结果为bytearray(b'spameggs')
bd = B.decode()
print(bd)  # 结果为spameggs

S = 'Spam'
sf = S.find('Sp')  # 返回匹配字串的偏移量，不匹配时返回-1
print(sf)  # 结果为0
ns = S.replace('pa', 'Lau')
print(S)   # 注意原字符串不变
print(ns)  # 结果为SLaum

line = 'aaa,bbb,ccc,ddd'
print(line.split(','))  # 根据分隔符将字符串拆分为子串
print(S.upper())  # 将小写转换为大写
print(S.isalpha())  # 内容检测，isalpha,isdigit等，返回TRUE
line = 'aaa,bbb,ccc,ddd\n'
print(line.rstrip())  # 移除右方空格
print(line.rstrip().split(','))  # 两次操作结合

# 字符串格式化表达式
print('%s,eggs,and %s' % ('a', 'b'))  # 格式化替换表达式（全Python支持）
print('{0},eggs and {1}'.format('a', 'b'))  # 条件方式（Python2.6+，3.0+）
print('{},eggs and {}'.format('a', 'b'))  # 免数字操作（Python2.7+, 3.1+）

# 数值格式化表达式
print('{:,.2f}'.format(296999.2567))  # 分隔符将小数和整数分别指定格式
print('%.2f|%+05d' % (3.14159, -42))  # %+05d带填充效果




