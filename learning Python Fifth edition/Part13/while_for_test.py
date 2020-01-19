x = 'spam'
while x:
    print(x, end=' ')
    x = x[1:]  # spam pam am m
else:
    print('\n')

# for循环
for x in ['spam', 'eggs', 'ham']:
    print(x, end=' ')  # spam eggs ham
else:
    print('\n')

Sum = 0
for x in [1, 2, 3, 4]:
    Sum = Sum + x
print(Sum)

# for循环中的元组赋值
T = [(1, 2), (3, 4)]
for (a, b) in T:
    print(a, b)

D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, D[key], sep='->')
# a->1
# b->2
# c->3

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)

# 嵌套for循环
items = ['aaa', 111, (4, 5), 2.01]
tests = ['lau', (4, 5)]
for key in tests:
    for item in items:
        if key == item:
            print(key, 'was found')
            break
    else:
        print(key, 'not found!')

# 并行遍历：zip和map
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
print(list(zip(L1, L2)))  # [(1, 5), (2, 6), (3, 7), (4, 8)]

for (x, y) in zip(L1, L2):
    print(x, y, ':', x + y)
# 1 5 : 6
# 2 6 : 8
# 3 7 : 10
# 4 8 : 12

T1, T2, T3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
print(list(zip(T1, T2, T3)))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# 注意：zip总是返回一个元组对象

S1 = 'abc'
S2 = 'xyz123'
print(list(zip(S1, S2)))  # [('a', 'x'), ('b', 'y'), ('c', 'z')]

# 使用zip构造字典
D2 = {}
keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]
for (k, v) in zip(keys, vals):
    D2[k] = v
print(D2)  # {'spam': 1, 'eggs': 3, 'toast': 5}

# 最简单形式
D3 = dict(zip(keys, vals))

# 循环中同时给出偏移量和元素：enumerate
S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)
# s appears at offset 0
# p appears at offset 1
# a appears at offset 2
# m appears at offset 3


