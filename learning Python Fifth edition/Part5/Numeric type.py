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


