import sys
# 单引号和双引号是一样的
title = "Meaning"' of '"Life"
print(title)

# 转义序列代表特殊字符（一个特殊字符）
s = 'a\nb\tc'
print(s)
print(len(s))  # 结果为5，他会返回字符串实际长度，无论该字符是如何编码或显示的

# 注意\0与C语言不同
s = 'a\0b\0c'
print(len(s))  # 5

x = 'C:\py\code'
print(x)  # 当反斜杠无意义时，直接保留反斜杠C:\py\code
print(len(x))  # 10

# 原始字符串阻止转义
x = r'\n\n\t'
print(x)  # 原始输出

# 三引号编写多行快字符串
mantra = '''Always Look
on the bright
side of life'''
print(mantra)  # 原格式输出

# 实际应用中的字符串
myjob = 'hacker'
for c in myjob:
    print(c, end=' ')

# 扩展分片：第三个限制和分片对象
S = 'abcdefghijklmnop'
print(S[1:10:2])  # bdfhj
print(S[::2])  # acegikmo
print(S[::-1])  # ponmlkjihgfedcba

# 分片等同于使用一个分片对象进行索引
print('spam'[1:3])  # pa
print('spam'[::-1])  # maps
print('spam'[slice(None, None, -1)])  # 结果同上

# 字符串转换工具
print(int('42'))
print(str(42))

# 字符串代码转换
print(ord('s'))  # 得到ASCII码
print(chr(115))  # 将ASCII码转换为字符

# 修改字符串
S = 'spam'
S = S + 'SPAM!'
print(S)
S = S[:4] + 'Burger' + S[-1]
print(S)  # spamBurger!

S = 'splot'
S = S.replace('pl', 'pamal')
print(S)  # spamalot

# 格式化创建字符串(实际上是创建了新的字符串对象)
S = 'That is %d %s bird!' % (1, 'dead')
print(S)  # That is 1 dead bird!
S = 'That is {0} {1} bird!'.format(1, 'dead')
print(S)

# 字符串方法
# 方法调用表达式object.method(arguments)
S = 'xxxxSPAMxxxSPAMxxxx'
where = S.find('SPAM')
print(where)  # 4,未找到时返回-1
S.replace('SPAM', 'EGGS', 1)  # 只替代一个

# 利用列表可变性修改字符串
S = 'spammy'
L = list(S)
L[3] = 'x'
L[4] = 'x'
S = ''.join(L)
print(S)

# 字符串方法示例：解析文本
line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
print(col1)  # aaa
print(col3)  # ccc

cols = line.split()
print(cols)  # ['aaa', 'bbb', 'ccc']
line = 'Bob,hacker,40'
print(line.split(','))  # ['Bob', 'hacker', '40']

# 实际运用中其他常见字符串方法
line = 'The knights who say NI\n'
print(line.endswith('\n'))  # True
print(line.startswith('The'))  # True

# 高级格式化表达式举例
x = 1234
res = 'integers:...%d...%-6d...%06d' % (x, x, x)
print(res)  # integers:...1234...1234  ...001234

x = 1.23456789
print('%e|%f|%g' % (x, x, x))  # 1.234568e+00|1.234568|1.23457
print('%E' % x)  # 1.234568E+00

print('%-6.2f|%05.2f|%+06.1f' % (x, x, x))  # 1.23  |01.23|+001.2

# 基于字典的格式化表达式
print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})  # 1 more spam

reply = '''
Greetings...
Hello %(name)s!
Your age is %(age)s
'''
value = {'name': 'bob', 'age': 40}
print(reply % value)
# Greetings...
# Hello bob!
# Your age is 40

food = 'spam'
qty = 10
d = vars()  # {'food': 'spam', 'qty': 10}
print(d)

print('%(qty)d more %(food)s' % vars())  # 10 more spam

# 字符串格式化方法调用
temple = '{0}, {1} and {2}'
print(temple.format('spam', 'ham', 'eggs'))  # spam, ham and eggs
temple = '{motto}, {pork} and {food}'
print(temple.format(motto='spam', pork='ham', food='eggs'))  # spam, ham and eggs
temple = '{motto}, {0} and {food}'
print(temple.format('ham', motto='spam', food='eggs'))
temple = '{}, {} and {}'
print(temple.format('spam', 'ham', 'eggs'))
X = '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2])
print(X)  # 3.14, 42 and [1, 2]

st = 'My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})  # My laptop runs win32
print(st)
st = 'My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'})
print(st)

# 以下方法只有单个正偏移量在表达式中有效
somelist = list('SPAM')
st = 'first = {0[0]}, third = {0[2]}'.format(somelist)
print(st)  # first = S, third = A

# 高级格式化方法举例
st = '{0:10} = {1:10}'.format('spam', 123.4567)  # 10表示字宽
print(st)  # spam       =   123.4567
st = '{0:>10} = {1:<10}'.format('spam', 123.4567)  # <左对齐，>右对齐
print(st)  #       spam = 123.4567
st = '{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop'))
print(st)  #      win32 = laptop

st = '{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159)
print(st)  # 3.141590e+00, 3.142e+00, 3.14159

print('%.*f' % (4, 1/3.0))  # 后面再确定精度 0.3333
print('{0:,d}'.format(9999999999))  # 9,999,999,999
