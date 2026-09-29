# 学习目标：int() float() str() 类型转换
#
# 类型转换：int() float() str()
#
# ⚠️ Java vs Python 差异：
#   Java：int num = Integer.parseInt("18");
#   Python：num = int("18")   ← 函数调用，更简单
# int() 转整型：int(15.6)=15, int('79')=79
# float() 转浮点型：float('15.6')=15.6
# str() 转字符串：str(18)='18'

result = float('15.6')
print(type(result), result)

# int('7 9')  # ❌ 有空格不行
# int('你好')  # ❌ 非数字不行
