import pickle
import json
import struct
import types
# 元组
print((1, 2) + (3, 4))  # (1, 2, 3, 4)
print((1, 2) * 4)  # (1, 2, 1, 2, 1, 2, 1, 2)
T = (1, 2, 3, 4)
print(T[0], T[1:3])  # 1 (2, 3)

# 元组的特殊语法：逗号和圆括号
x = (40)  # 认为是表达式
print(x)
x = (40,)  # 认为是元组
print(x)  # (40,)

# 转换，方法和不可变性
T = ('cc', 'aa', 'dd', 'bb')  # 元组不能使用sort方法
tem = list(T)
tem.sort()
print(tem)  # ['aa', 'bb', 'cc', 'dd']

print(sorted(T))  # ['aa', 'bb', 'cc', 'dd']
T = (1, 2, 3, 4, 5)
L = [x + 20 for x in T]  # 元组可用于推导
print(L)

T = (1, 2, 3, 2, 4, 2)
print(T.index(2))
T.count(2)  # 计算元素个数

# 元组的不可变性只是指元组顶层，而非其内容
T = (1, [2, 3], 4)
T[1][0] = 'spam'
print(T)  # (1, ['spam', 3], 4)

bob = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
jobs, name, age = bob.values()
print(name, jobs)  # 40.5 Bob

# 文件
myfile = open('myfile.txt', 'w')
myfile.write('hello text file\n')
myfile.write('goodbye text file\n')
myfile.close()

myfile = open('myfile.txt')
print(myfile.readline())  # hello text file
print(myfile.readline())  # goodbye text file
print(myfile.readline())  # '\n'作为文件的结尾，并非空格

print(open('myfile.txt').read())
# hello text file
# goodbye text file

for line in open('myfile.txt'):
    print(line, end='')
# hello text file
# goodbye text file

# 在文件中存储Python对象：转换
X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s, %s, %s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

chars = open('datafile.txt').read()
print(chars)
# Spam
# 43, 44, 45
# [1, 2, 3]${'a': 1, 'b': 2}

F = open('datafile.txt')  # 读取到的是字符对象
line = F.readline()
print(line)  # 'Spam\n'
line.rstrip()
print(line)  # 'Spam'

line = F.readline()
print(line)  # 43, 44, 45
parts = line.split(',')  # 转换为列表
print(parts)  # ['43', ' 44', ' 45\n']

print(int(parts[1]))  # 44,将字符串列表转换为数字
numbers = [int(p) for p in parts]
print(numbers)  # [43, 44, 45]

line = F.readline()
print(line)  # '[1, 2, 3]${'a': 1, 'b': 2}\n'

parts = line.split('$')
print(parts)  # ['[1, 2, 3]', "{'a': 1, 'b': 2}\n"]
print(eval(parts[0]))  # [1, 2, 3]
objects = [eval(p) for p in parts]
print(objects)  # [[1, 2, 3], {'a': 1, 'b': 2}]

# 存储Python原生对象：pickle
D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
pickle.dump(D, F)
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)
print(E)  # {'a': 1, 'b': 2}

# 用JSON格式存储Python对象
name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mar'], age=40.5)
print(rec)  # {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mar'], 'age': 40.5}

S = json.dumps(rec)
print(S)  # {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mar'], 'age': 40.5}
O = json.loads(S)
print(O)  # {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mar'], 'age': 40.5}
print(O == rec)  # True

json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
print(open('testjson.txt').read())
# {
#     "name": {
#         "first": "Bob",
#         "last": "Smith"
#     },
#     "job": [
#         "dev",
#         "mar"
#     ],
#     "age": 40.5
# }

P = json.load(open('testjson.txt'))
print(P)  # {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mar'], 'age': 40.5}

# 存储打包二进制数据：struct
F = open('data.bin', 'wb')
data = struct.pack('>i4sh', 7, b'spam', 8)
print(data)  # b'\x00\x00\x00\x07spam\x00\x08'
F.write(data)
F.close()

F = open('data.bin', 'rb')
data = F.read()
print(data)  # b'\x00\x00\x00\x07spam\x00\x08'
values = struct.unpack('>i4sh', data)
print(values)  # (7, b'spam', 8)

# 对象灵活性
L = ['abc', [(1, 2), ([3], 4)], 5]
print(L[1])  # [(1, 2), ([3], 4)]
print(L[1][1])  # ([3], 4)
print(L[1][1][0])  # [3]
print(L[1][1][0][0])  # 3

# 应用 VS 复制
X = [1, 2, 3]
L = ['a', X, 'b']
D = {'x': X, 'y': 2}
X[1] = 'surprise'
print(L)  # ['a', [1, 'surprise', 3], 'b'] 此时L会改变
print(D)  # {'x': [1, 'surprise', 3], 'y': 2} 此时D也会改变
L = [1, 2, 3]
D = {'a': 1, 'b': 2}
A = L[:]
B = D.copy()
A[1] = 'Ni'
B['c'] = 'Spam'
print(L)  # [1, 2, 3]
print(D)  # {'a': 1, 'b': 2}
print(A, B)  # [1, 'Ni', 3] {'a': 1, 'b': 2, 'c': 'Spam'}

# 避免被修改的改进
X = [1, 2, 3]
L = ['a', X[:], 'b']
D = {'x': X[:], 'y': 2}

# 无参数的分片以及字典的copy方法只能进行顶层复制，若要完全独立的复制则要使用copy模块
# 比较、等价性和真值
L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]
print(L1 == L2)  # 递归比较，True
print(L1 is L2)  # 同一性比较，False

L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]
print(L1 < L2, L1 == L2, L1 > L2)  # False False True

# 字典的比较
D1 = {'a': 1, 'b': 2}
D2 = {'a': 1, 'b': 3}
print(sorted(D1.items()) > sorted(D2.items()))
print(sorted(D1.items()) < sorted(D2.items()))

# 类型的对象
# 以下结果均为True
type([1]) == type([])
type([1]) == list
isinstance([1], list)
def f():
    pass
type(f) == types.FunctionType

# 重复会增加层次深度
L = [4, 5, 6]
X = L * 4
Y = [L] * 4
print(X)  # [4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6]
print(Y)  # [[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]]  # Y 会有联动修改的危险
L[1] = 0
print(Y)  # [[4, 0, 6], [4, 0, 6], [4, 0, 6], [4, 0, 6]]

# 解决方案1
L = [4, 5, 6]
Y = [list(L)] * 4
print(Y)  # [[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]]
# Y 和 L不再共同引用同一对象，但Y中的每一项（共4项）都共用同一对象
Y[0][1] = 99
print(Y)  # [[4, 99, 6], [4, 99, 6], [4, 99, 6], [4, 99, 6]]

# 完美解决方式
L = [4, 5, 6]
Y = [list(L) for i in range(4)]
print(Y)  # [[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]]









