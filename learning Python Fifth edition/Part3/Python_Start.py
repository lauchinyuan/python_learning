# 第一段python脚本
import sys
# import Test_Code  # 导入关联文件
import Test_Code  # 即使两次import也只显示一次结果
from Test_Code import new_title # 使用from...import 语句进行导入
print(new_title)  # 直接变量调用即可，实质上from...import复制了模块的属性
# from importlib import reload  # 用此方法可以实现多次导入文件
# reload(Test_Code)
print(sys.platform)  # 显示python平台
print(2 ** 10)
x = 'Spam!'
print(x * 8)
print(Test_Code.title)  # 导入Test_Code中的title属性

all_attribute = dir(Test_Code)  # 使用dir获得模块所有可用的变量名列表
print(all_attribute)

