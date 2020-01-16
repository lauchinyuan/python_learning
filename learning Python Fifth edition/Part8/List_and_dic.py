# 基本列表操作
print(len([1, 2, 3]))  # 3
print([1, 2, 3] + [4, 5, 6])
print(['NI'] * 4)

print(3 in [1, 2, 3])

res = [c * 4 for c in 'SPAM']
print(res)  # ['SSSS', 'PPPP', 'AAAA', 'MMMM']

res = []
for c in 'SPAM':
    res.append(c * 4)
print(res)  # ['SSSS', 'PPPP', 'AAAA', 'MMMM']

# 索引、分片和矩阵
L = ['spam', 'Spam', 'SPAM！']
print(L[2])  # 索引不返回新对象，即是列表子对象
print(L[-2])
print(L[1:])  # 分片返回一个新的列表对象

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])  # 5

# 原位置修改列表
L[1] = 'eggs'
print(L)  # ['spam', 'eggs', 'SPAM！']
L[0:2] = ['eat', 'more']
print(L)  # ['eat', 'more', 'SPAM！']
L = [1, 4, 5, 3]
L[1:1] = [6, 7]  # 注意此式子的理解
print(L)  # [1, 6, 7, 4, 5, 3]

L = [1]
L[:0] = [2, 3, 4]
print(L)  # [2, 3, 4, 1]
L[len(L):] = [5, 6, 7]  # 相当于扩展
print(L)

# 列表方法调用
L = ['eat', 'more', 'SPAM']
L.append('please')  # ['eat', 'more', 'SPAM', 'please']
print(L)

L.sort()
print(L)  # ['SPAM', 'eat', 'more', 'please']

# 关于列表排序
L = ['abc', 'ABD', 'aBe']
L.sort()
print(L)  # ['ABD', 'aBe', 'abc']

L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower)
L.sort(reverse=True)  # 从大到小
print(L)

L = ['abc', 'ABD', 'abe']
print(sorted(L, reverse=True))

# 其他常见列表方法
L = [1, 2]
L.extend([3, 4, 5])
print(L)  # [1, 2, 3, 4, 5]
print(L.pop())  # 删除并返回最后一个数5
L.reverse()
print(L)  # [4, 3, 2, 1]
list(reversed(L))  # 结果同上

L = []
L.append(1)
L.append(2)
print(L)  # [1, 2]
L.pop()
print(L)  # [1]

L = ['spam', 'eggs', 'ham']
print(L.index('eggs'))  # 查找一个元素索引值 1
L.insert(1, 'toast')
print(L)  # ['spam', 'toast', 'eggs', 'ham']
L.remove('eggs')
print(L)
print(L.pop(1))  # toast
print(L)  # ['spam', 'ham']
print(L.count('spam'))  # 1  # 计算个数

L = ['spam', 'eggs', 'ham', 'toast']
del L[0]  # 删除操作
print(L)

del L[1:]
print(L)  # ['spam', 'ham']

# 字典
D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(D['spam'])  # 2
print(D)
print(len(D))
print('ham' in D)
print(list(D.keys()))  # ['spam', 'ham', 'eggs']

print(D)  # {'spam': 2, 'ham': 1, 'eggs': 3}
D['ham'] = ['grill', 'bake', 'fry']
print(D)  # {'spam': 2, 'ham': ['grill', 'bake', 'fry'], 'eggs': 3}
del D['eggs']
print(D)  # {'spam': 2, 'ham': ['grill', 'bake', 'fry']}
D['brunch'] = 'Bacon'
print(D)  # {'spam': 2, 'ham': ['grill', 'bake', 'fry'], 'brunch': 'Bacon'}

# 其他字典方法
D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(list(D.values()))  # [2, 1, 3]
print(list(D.items()))  # [('spam', 2), ('ham', 1), ('eggs', 3)]
print(D.get('spam'))  # 2
print(D.get('toast'))  # None,通过此方法获取字典值，可以避免不存在时出现意外
print(D.get('toast', 88))  # 键值不存在时，返回默认的键值88

D = {'spam': 2, 'ham': 1, 'eggs': 3}
D2 = {'toast': 4, 'muffin': 5}
D.update(D2)  # 整合
print(D)  # {'spam': 2, 'ham': 1, 'eggs': 3, 'toast': 4, 'muffin': 5}

print(D.pop('muffin'))  # 5,删除并返回
print(D.pop('toast'))

# 实例：电影的数据库
table = {'1975': '中国大陆',
         '1979': '台湾',
         '1983': '香港'}
year = '1983'
print(table[year])
for year in table:
    print(year + '\t' + table[year])
# 1975	中国大陆
# 1979	台湾
# 1983	香港

# 用字典模拟灵活的列表：整数键
L = []
# L[99] = 'spam' 非法，超过范围

D = {}
D[99] = 'spam'
print(D[99])
print(D)  # {99: 'spam'}

# 对稀疏数据结构使用字典：用元组作键
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
print(Matrix[(2, 3, 4)])  # 88
print(Matrix)  # {(2, 3, 4): 88, (7, 8, 9): 99}

if (2, 3, 6) in Matrix:
    print(Matrix[2, 3, 6])
else:
    print(0)

try:
    print(Matrix[2, 3, 6])
except KeyError:
    print(0)

print(Matrix.get((2, 3, 6), 0))

# 字典的嵌套
rec = {}
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['job'] = 'developer'
print(rec['name'])

D = dict([('name', 'Bob'), ('age', 40)])
print(D)  # {'name': 'Bob', 'age': 40}  # {'name': 'Bob', 'age': 40}

# 字典推导
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)  # {'a': 1, 'b': 2, 'c': 3}
D = {x: x ** 2 for x in [1, 2, 3, 4]}
D = {c: c * 4 for c in 'SPAM'}
print(D)
D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)  # {'spam': 'SPAM!', 'eggs': 'EGGS!', 'ham': 'HAM!'}
D = dict.fromkeys(['a', 'b', 'c'], 0)
print(D)  # {'a': 0, 'b': 0, 'c': 0}
D = {k: 0 for k in ['a', 'b', 'c']}
D = dict.fromkeys('spam')
print(D)  # {'s': None, 'p': None, 'a': None, 'm': None}
D = {k: None for k in 'spam'}

# 字典视图
D = {'a': 1, 'b': 2, 'c': 3}
K = D.keys()
V = D.values()
print(list(K))  # ['a', 'b', 'c']
print(list(V))  # [1, 2, 3]
del D['b']
print(list(K))  # ['a', 'c']
print(list(V))  # [1, 3]

D = {'a': 1, 'b': 2, 'c': 3}
for k in sorted(D):
    print(k, D[k])
# a 1
# b 2
# c 3

# 3.X中字典大小比较不再有效

