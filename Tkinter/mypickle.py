# pickle存放数据
from typing import Dict

import pickle

# 保存数据
var = 100
file = open('.\\file\\pickle_example.pickle', 'wb')  # wb代表写入二进制
pickle.dump(var, file)  # 将var的值存放到pickle文件中
file.close()

# 读取数据
file = open('.\\file\\pickle_example.pickle', 'rb')  # rb代表读取二进制
var_read = pickle.load(file)
file.close()
print(var_read)

