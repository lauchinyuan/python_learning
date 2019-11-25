# 基本对象类型
import math
import random
import re

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

# 寻求帮助
print(dir(S))  # 利用dir()方法查看对象的所有属性，其中方法也是函数属性
print(S.__add__('ha ha ha'))  # 程序相对跑得慢
help(S.format)  # 使用help方法查看帮助，help是面向系统代码的接口

# 字符串编程的其他方式
print(ord('A'))  # 使用ord查看十进制ASCII码
S = 'A\0B\0C'
print(len(S))  # 返回值为5，'\0'不是字符串的终点
print(S)  # 结果为A B C

# 三引号有利于HTML、XML、JSON代码
S = """  
三个
引号
时
自动
加
换行符
"""
print(S)
S = r'原始格式照例输出\n'  # 原始格式输出（raw）
print(S)

# Unicode支持
print('sp\xc4m')  # 普通unicode格式，结果为spA(特殊)m
print(b'a\x01c')  # 基于字节的数据
'spam'.encode('utf8')  # 使用UTF-8编码
'spam'.encode('utf16')  # 使用UTF-16编码

# 模式匹配
match = re.match('Hello[ \t]*(.*)world', 'Hello   Python world')  # 匹配子字符串，从Hello开始，后面跟着制表符和空格
# 接着任意字符并将其保存至匹配组中，最后以单词world结尾
print(match.group(1))

# 列表
# 序列操作
# 列表是序列的一种，支持前面讨论的对字符串进行的序列操作
L = [123, 'Spam', 1.23]
print(len(L))  # 结果为3
print(L[0])  # 从0开始计数
print(L[:-1])  # 对列表切片返回一个新列表
print(L+[4, 5, 6])  # 连接
print(L*2)  # 重复
print(L)  # 原来L列表不变

# 特定类型操作
# 列表没有固定类型约束和固定大小
# 大多数列表的方法都会原位置改变列表对象，而不是创建一个新的列表
L.append('NI')  # 在列表末尾附加新对象
print(L)
L.pop(2)  # 删除第三个列表元素
print(L)

M = ['aa', 'cc', 'bb']
M.sort()  # 按升序排序
print(M)
M.reverse()  # 顺序翻转
print(M)

# 边界检查
# print(L[99])  # 不允许引用不存在的元素
# L[99] = 1  # 不允许
# print(L[99])









