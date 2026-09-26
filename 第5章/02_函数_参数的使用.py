# 函数参数
#
# ⚠️ 和 Java 类似，但不用写参数类型
# num, dish 是形参，只能在函数内部用
def order(num, dish):
    print(f'您点的是：{num}份 {dish}')
    print(f'{dish}可是很好吃的！')
    print(f'你只点了{num}份，够吃吗？\n')

# print(num)  # ❌ 形参在函数外用不了

order(1, '辣椒炒肉')
order(2, '辣子鸡')

# order(3)                  # ❌ 少传一个参数
# order(4, '宫保鸡丁', 7)    # ❌ 多传一个参数
