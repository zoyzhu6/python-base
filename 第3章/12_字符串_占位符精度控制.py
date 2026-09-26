# 占位符精度：%5.2f
#
# ⚠️ Java vs Python 差异：和 C/Java 的 printf 格式化一样
# %5.2f：总宽5，小数点后2位；%-4.1s：左对齐，宽4
name = '张三'
weight = 65.55
age = 12

info = '我叫%4.1s，体重是%7.3f，年龄是%4d' % (name, weight, age)
print(info)
