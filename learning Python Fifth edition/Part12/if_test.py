# and 和 or 运算总会返回一个对象
print(2 or 3)  # 2
print([] or 3)  # 3
print({} or [])  # []

print(2 and 3)  # 3
print([] and {})  # []
print(3 and [])  # []

