import math
import random
import decimal
from decimal import Decimal
from fractions import Fraction
# 变量与基础表达式
a = 3
b = 4
print(a + 1, a - 1)

# c * 2  # 错误，c没有被定义

# 除法运算
print(b/2 + a)  # 在Python3.X中会执行带小数的真除法，结果为5.0
# 在Python2.X中结果为5
print(b//2 + a)  # 在Python3.X中执行整数除法,结果为5

# 数值的显示格式
num = 1 / 3.0
print(num)

print('%e' % num)  # 科学计数法
print('%4.2f' % num)

# 普通比较和链式比较
X = 2
Y = 4
Z = 6
print(X < Y < Z)  # 支持链式比较
print(X < Y and Y < Z)  # 结果同上

print(X < Y > Z)
print(X < Y and Y > Z)

print(1 < 2 < 3.0 < 4)
print(1 > 2 > 3.0 > 4)
print(1 == 2 < 3)  # 此链式比较较为晦涩，但结果和C语言不同
print(1 == 2 and 2 < 3)  # 同上，注意得到的是False

# 浮点数比特位数有限
print(1.1 + 2.2 == 3.3)  # 特别注意浮点数的比较，此处返回False
print(1.1 + 2.2)  # 注意结果为3.3000000000000003
print(int(1.1) + int(2.2) == int(3.3))  # 经过转换后结果为True

# 除法
# Python3.X中/表示真除法
print(10/4)  # 结果为2.5
print(10/4.0)  # 2.5
print(10//4)  # 2
print(10//4.0)  # 2.0

# 除法在Python不同版本中不同，
# 若需使用整数截断除法，建议使用//
# 若对于整数需要小数部分的浮点数结果，建议使用float调用将数转换为浮点数

# 向下取整除法VS截断除法
# //结果为向下取整除法
m = math.floor(2.5)
print(m)  # 2
m = math.floor(-2.5)
print(m)  # -3
m = math.trunc(2.5)
print(m)  # 2
m = math.trunc(-2.5)
print(m)  # -2

print(5/2)  # 2.5
print(5/-2)  # -2.5
print(5//2)  # 2
print(5//-2)  # -3
print(5//2.0)  # 2.5
print(5//-2.0)  # -3.0

# 使用趋近于0的截断除法
print(math.trunc(5/2))  # 结果为2，而不是3

# 复数
print(2 + -3j)  # 相当于2-3j
print(1j * 1j)  # (-1+0j)
print(2 + 1j * 3)  # (2+3j)
print((2 + 1j) * 3)

# 十六进制、二进制与八进制
print(0o1, 0o20, 0o377)  # 八进制,打印结果为整数
print(0x01, 0x10, 0xFF)  # 十六进制
print(0b1, 0b10000, 0b11111111)  # 二进制
# 以上三者结果皆为1 16 255

print(oct(64), hex(64), bin(64))  # 使用指定数制显示
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))  # 通过int()方法将其他进制转换为二进制
# 这对于文件方式读取的字符串数字来说很有意义
print(int('0x40', 16), int('0b1000000', 2))  # 也可以加上字面量

# 进制格式化
print('{0:o},{1:x},{2:b}'.format(64, 64, 64))  # 100,40,1000000
print('%o,%x,%x,%X' % (64, 64, 255, 255))  # 100,40,ff,FF

X = 0xFFFFFFFFFFFFFFFFFFFFFFF
print(X)  # 4951760157141521099596496895
print(oct(X))  # 0o3777777777777777777777777777777
print(bin(X))  # 0b11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

# 按位操作
x = 1
print(x << 2)  # 4
print(x | 2)  # 3
print(x & 1)  # 1
x = 0b0001
print(bin(x << 2))  # 0b100
print(bin(x | 0b010))  # 0b11

X = 0xFF
print(bin(X))
print(X ^ 0b10101010)  # 亦或，85
print(bin(X ^ 0b10101010))
print(int('01010101', 2))  # 85
print(hex(85))  # 0x55

X = 99
print(bin(X), X.bit_length(), len(bin(X)) - 2)  # 0b1100011 7 7

# 其他内置数值工具
# math模块
print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))  # 三角函数
print(math.sqrt(144), math.sqrt(2))
print(pow(2, 4), 2 ** 4, 2.0 ** 4.0)  # 16.0 16 16.0
print(abs(-42.0), sum((1, 2, 3, 4)))
print(min(3, 1, 2, 4), max(3, 1, 2, 4))
print(math.floor(2.567), math.floor(-2.3))  # 向下取整
print(round(2.567), round(2.467), round(2.567, 2))  # 四舍五入+指定小数位数
print('%.1f' % 2.567, '{0:.2f}'.format(2.567))  # 混合格式化输出

print(math.sqrt(144))  # 使用模块计算平方根
print(144 ** .5)  # 表达式法
print(pow(144, .5))  # 内置函数法

# random模块
rd = random.Random()
print(rd)
print(random.randint(1, 10))  # 随机整数
print(random.choice(['China', 'Taiwan', 'Hongkong']))
suits = ['Heart', 'clubs', 'diamond', 'spades']  # 扑克四色
random.shuffle(suits)  # 洗牌
print(suits)

# 其他数值类型
print(0.1 + 0.1 + 0.1 - 0.3)  # 注意：结果非零，浮点数运算缺乏精确性
# 可以用小数模块替代
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))  # 0.0
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.30'))  # 0.00

# 设置全局小数精度
print(Decimal(1)/Decimal(7))  # 0.1428571428571428571428571429
decimal.getcontext().prec = 4  # 设置小数位数
print(Decimal(1)/Decimal(7))  # 0.1429

print(1999 + 1.33)
pay = decimal.getcontext().prec = 20
print(Decimal(str(1999 + 1.33)))

# 小数上下文管理器
print(Decimal('1.00')/Decimal('3.00'))  # 0.333333333333...
with decimal.localcontext() as ctx:  # 临时改变精度
    ctx.prec = 2
    print(Decimal('1.00') / Decimal('3.00'))  # 0.33
print(Decimal('1.00')/Decimal('3.00'))  # 精度返回原来设置

# 分数类型
x = Fraction(1, 3)
y = Fraction(4, 6)
print(x, y)
print(x + y)
print(x - y)
print(x * y)
print(Fraction('.25'))  # 1/4
print(Fraction('1.25'))  # 5/4

# 分数和小数中的数值精度
a = 1/3.0
b = 4/6.0
print(a, b, a + b, a - b, a * b, a / b)
print((1/3) + (6/12))
print(Fraction(6, 12))  # 自动化简为1/2

# 分数转换和混用类型
print(2.5.as_integer_ratio())  # 将浮点数转化为整数相除的形式
f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z)  # 效果同上，结果为5/2

print(x)
print(x + z)
print(float(x))
print(float(z))
print(Fraction.from_float(1.75))
print(Fraction(*1.75.as_integer_ratio()))

print(x + 2)  # 7/3
print(x + 2.0)  # 2.333333333335
print(x + (1./3))  # 0.6666666666666666
print(x + (4./3))  # 1.6666666666666665
print(x + Fraction(4, 3))  # 5/3

print(4.0/3)  # 1.3333333333333333
print((4.0/3).as_integer_ratio())  # (6004799503160661, 4503599627370496)

print(x)  # 1/3
a = x + Fraction(*(4.0/3).as_integer_ratio())
print(a)  # 22517998136852479/13510798882111488
print(a.limit_denominator(10))  # 5/3


#  python2.6之前的集合
x = set('abcde')
y = set('bdxyz')
print(x, y)  # {'d', 'c', 'b', 'e', 'a'} {'d', 'b', 'y', 'z', 'x'}顺序任意可变
print(x - y)  # {'e', 'c', 'a'}
print(x | y)  # {'c', 'x', 'e', 'd', 'a', 'z', 'y', 'b'}
print(x & y)  # {'b', 'd'}
print(x ^ y)  # {'e', 'c', 'z', 'y', 'x', 'a'}
print(x > y, x < y)  # False False

print('e' in x)  # True
print('e' in 'Camelot', 22 in [11, 22, 33])  # 字符串与列表使用in表达式的情况

z = x.intersection(y)  # 类似于x & y
z.add('Spam')  # 在集合中增加元素
print(z)  # {'d', 'b', 'Spam'}

# 由于集合是无序的，故不支持分片、索引操作
# 集合可以使用列表推导
# 空集合必须通过内置函数set来创建
for item in set('abc'):
    print(item * 3)
# aaa
# bbb
# ccc

S = set([1, 2, 3])
print(S | set([3, 4]))  # {1, 2, 3, 4}

# print(S | [3, 4])  # TypeError: unsupported operand type(s) for |: 'set' and 'list'
print(S.union([3, 4]))  # {1, 2, 3, 4} 但S仍为 {1, 2, 3}

# python3.X中的集合字面量
print({1, 2, 3, 4})
S.add('alot')  # 集合添加项
print(S)

S1 = {1, 2, 3, 4}
print(S1 & {1, 3})  # {1, 3}
print({1, 5, 3, 6} | S1)  # {1, 2, 3, 4, 5, 6}
print(S1 - {1, 3, 4})  # {2}
print(S1 > {1, 3})  # True

# python中认为{}仍是一个字典，故创建空集合要使用set
print(S1 - {1, 2, 3, 4})  # 减完为空集
t = type({})
print(t)  # <class 'dict'>
S = set()  # 创建空集正确方法
S.add(1.23)
print(S)  # {1.23}

# 不可变性限制与冻结集合
# 集合只能包含不可变的对象类型，故列表和字典不可嵌套到集合中
# S.add([1, 2, 3])  TypeError: unhashable type: 'list'
# S.add({'apple': '苹果'})  TypeError: unhashable type: 'dict'
S.add((1, 2, 3))  # 可以添加元组
print(S)  # {1.23, (1, 2, 3)}
print(S | {(4, 5, 6), (1, 2, 3)})  # {1.23, (4, 5, 6), (1, 2, 3)}

# python3.X 和2.7中集合推导
print({x ** 2 for x in [1, 2, 3, 4]})  # {1, 4, 9}

# 集合与列表
L = [1, 2, 1, 3, 2, 4, 5]
print(set(L))  # 转换为集合
L = list(set(L))  # 相当于去除重复项
print(L)  # [1, 2, 3, 4, 5]

print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]))  # {3, 7}
print(set('abcdefg') - set('abdghij'))  # {'e', 'c', 'f'}

# 可以借助集合进行顺序无关的等价性测试
L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1 == L2)  # False
print(set(L1) == set(L2))  # True
print(sorted(L1) == sorted(L2))  # True

# 布尔型
t = type(True)
print(t)  # <class 'bool'>
print(isinstance(True, int))  # True,实质上布尔型为int的子类



