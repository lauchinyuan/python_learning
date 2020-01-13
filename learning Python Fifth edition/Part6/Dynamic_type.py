import copy
# 共享引用和在原位置修改
L1 = [2, 3, 4]
L2 = L1
L1[0] = 24
print(L1)  # [24, 3, 4]
print(L2)  # [24, 3, 4]

# 复制对象则不会有上述问题
L1 = [2, 3, 4]
L2 = L1[:]
L1[0] = 24
print(L1)  # [24, 3, 4]
print(L2)  # [2, 3, 4]
# 复制字典或集合时无法使用上述方法（字典集合都无序）

# 共享引用和相等
# == 检查对象的值是否相等， is 检查对象的同一性
L = [1, 2, 3]
M = L
print(L == M, L is M)  # True, True

M = [1, 2, 3]  # M与L引用对象不同
print(L == M)  # True
print(L is M)  # False

X = 42
Y = 42
print(X == Y)
print(X is Y)  # 对于小数字时，两者都是True，与Python垃圾回收机制有关


