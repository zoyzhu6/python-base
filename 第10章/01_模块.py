# 模块 import
#
# ⚠️ Java vs Python 差异：
#   Java：import java.util.ArrayList;
#   Python：import math   ← 导入整个文件
# 同目录下有 math_utils.py，里面有 add 函数
# import math_utils
# print(math_utils.add(1, 2))

# from 模块名 import 函数名：只导入需要的
# from math_utils import add
# print(add(1, 2))

# as 起别名
# import math_utils as mu
