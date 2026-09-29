# 学习目标：copy.copy浅拷贝 copy.deepcopy深拷贝
#
# copy.copy浅拷贝外层新内层共享，deepcopy完全独立
import copy

a = [1, 2, [3, 4]]

# 浅拷贝：外层新对象，内层还是共享
b = copy.copy(a)
b[2][0] = 99
print(a[2][0])   # 99（内层被改了）

# 深拷贝：完全独立
c = copy.deepcopy(a)
c[2][0] = 0
print(a[2][0])   # 99（没受影响）
