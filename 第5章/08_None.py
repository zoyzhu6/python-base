# 学习目标：None空值，相当于Java的null
#
# None：空值
#
# ⚠️ Java vs Python 差异：
#   Java：null
#   Python：None   ← 首字母大写，是个对象
# None = 空值，类似 Java 的 null
msg = None
print(type(msg))   # <class 'NoneType'>
print(bool(msg))   # False

if not msg:
    print('你好')

# msg + 1         # ❌ None 不能参与运算
# msg + 'hello'    # ❌ None 不能拼接字符串
