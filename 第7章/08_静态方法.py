# 静态方法：@staticmethod，不需要 self/cls
#
# ⚠️ Java vs Python 差异：
#   Java：public static int add(int a, int b) { return a + b; }
#   Python：@staticmethod / def add(a, b): return a + b
#
#   就是放在类里的工具函数，和类本身关系不大

class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(1, 2))
