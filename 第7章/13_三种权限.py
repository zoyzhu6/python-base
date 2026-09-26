# 权限：公有name/保护_age/私有__idcard
class Person:
    def __init__(self, name, age, idcard):
        self.name = name        # 公有：随便访问
        self._age = age         # 保护：约定不外部访问，但不强制
        self.__idcard = idcard  # 私有：类外部访问不到

p = Person('张三', 18, '110101...')
print(p.name)      # ✅
print(p._age)      # 能访问但不推荐
# print(p.__idcard) # ❌ 报错
