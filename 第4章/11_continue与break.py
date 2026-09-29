# 学习目标：break跳出循环 continue跳过本次
#
# break / continue
#
# ⚠️ 和 Java 一样
# break：跳出整个循环
# continue：跳过本次，继续下一次
for i in range(1, 6):  # ⭐ 核心语法
    if i == 3:
        continue    # 跳过3
    if i == 5:
        break       # 到5就停
    print(i)
