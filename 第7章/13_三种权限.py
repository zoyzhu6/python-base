# 学习目标：_name约定保护 __name私有改名
#
# 权限控制：Python 没有真正的 private
#
# ⚠️ Java vs Python 差异：
#   Java：private / protected / public 关键字
#   Python：靠命名约定，不是强制的
#
#   name     公有：随便访问
#   _name    保护：约定不外部访问，但技术上能访问
#   __name   私有：Python 自动改名 _Person__name，外部访问不到
#
#   ⚠️ 注意：这都是约定！不是编译器强制！

class Person:  # ⭐ 定义类  # ⭐ 核心语法
    def __init__(self, name, age, idcard):  # ⭐ 类方法
        self.name = name        # 公有
        self._age = age         # 保护（约定）
        self.__idcard = idcard  # 私有（改名 _Person__idcard）

p = Person('张三', 18, '110...')
print(p.name)      # ✅
print(p._age)      # 能访问但不推荐
# print(p.__idcard) # ❌ 报错（实际是 _Person__idcard）
