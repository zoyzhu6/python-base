# None：空值，类似Java的null，bool(None)=False
# None = 空值，类似 Java 的 null
msg = None
print(type(msg))   # <class 'NoneType'>
print(bool(msg))   # False

if not msg:
    print('你好')

# msg + 1         # ❌ None 不能参与运算
# msg + 'hello'    # ❌ None 不能拼接字符串
