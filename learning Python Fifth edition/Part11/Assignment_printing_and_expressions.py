import sys
# 高级序列赋值语句
string = 'SPAM'
a, b = string[: 2]
c = string[2:]
print(a, b, c)  # S P AM

(a, b), c = string[: 2], string[2:]
print(a, b, c)  # S P AM

((a, b), c) = ('SP', 'AM')
print(a, b, c)  # S P AM

red, green, blue = range(3)
print(red, green, blue)  # 0 1 2

# 扩展序列解包
# 解包赋值总是返回列表
seq = [1, 2, 3, 4]
a, *b = seq
print(a, b)  # 1 [2, 3, 4]

*a, b = seq
print(a, b)  # [1, 2, 3] 4

a, *b, c = seq
print(a, b, c)  # 1 [2, 3] 4

a, *b = 'spam'
print(a, b)  # s ['p', 'a', 'm']

seq = [1, 2, 3, 4]
a, b, c, d, *e = seq  # 元素个数左边比右边多时，返回空列表
print(a, b, c, d, e)  # 1 2 3 4 []

a, b, *e, c, d = seq
print(a, b, c, d, e)  # 1 2 3 4 []

# *a = seq  # 语法错误，带星号名称无法单独出现
*a, = seq
print(a)  # [1, 2, 3, 4]

L = []
L += 'spam'  # 此处相当于调用'extend'方法，在原位置修改，而不是普通拼接，故可以是任意序列
print(L)  # ['s', 'p', 'a', 'm']

# L = L + 'spam'  # 语法错误

L = [1, 2]
M = L
L = L + [3, 4]
print(L, M)  # [1, 2, 3, 4] [1, 2]

L = [1, 2]
M = L
L += [3, 4]
print(L, M)  # [1, 2, 3, 4] [1, 2, 3, 4]

# Python3.X中print函数的调用
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z, sep='')  # sep指定分隔符  spam99['eggs']
print(x, y, z, sep=',')  # spam,99,['eggs']
print(x, y, z, end='')  # 指定行位符号，默认换行

# 手动重定向输出流
temp = sys.stdout
sys.stdout = open('log.txt', 'a')
print('spam')
print(1, 2, 3)
sys.stdout.close()

sys.stdout = temp  # 将标准输出切换回去
print('Back here')
print(open('log.txt').read())
# spam
# 1 2 3

# 自动流重定向
log = open('log.txt', 'w')
print(1, 2, 3, file=log)
log.close()

# 拥有界限符的结构自然可以跨越多行
L = ['Good',
     'Bad',
     'Ugly']







