# 第一段python脚本
import sys
import Test_Code  # 导入关联文件
import Test_Code  # 即使两次import也只显示一次结果
from importlib import reload  # 用次方次可以实现多次导入文件
reload(Test_Code)
print(sys.platform)  # 显示python平台
print(2 ** 10)
x = 'Spam!'
print(x * 8)





