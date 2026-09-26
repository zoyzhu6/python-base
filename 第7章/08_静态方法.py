# 静态方法：@staticmethod，不需要self/cls，工具函数
class Math:
    # @staticmethod 静态方法：不需要 self/cls，就是放类里的工具函数
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(1, 2))   # 3
