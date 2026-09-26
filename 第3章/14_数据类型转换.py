# 类型转换：int() float() str()
# int() 转整型：int(15.6)=15, int('79')=79
# float() 转浮点型：float('15.6')=15.6
# str() 转字符串：str(18)='18'

result = float('15.6')
print(type(result), result)

# int('7 9')  # ❌ 有空格不行
# int('你好')  # ❌ 非数字不行
