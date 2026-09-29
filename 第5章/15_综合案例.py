# 学习目标：综合函数做健身统计
#
# 综合案例：健身统计
def calc_total(*nums):
    """计算总运动量"""
    return sum(nums)

def calc_avg(total, days=7):
    """计算平均值"""
    return total / days

def check_success(total, goal=120):
    """判断是否达标"""
    if total >= goal:
        return '✅恭喜！挑战成功！'
    return '❌抱歉！挑战失败！'

def main(title, duration, goal):
    """主函数：输入每天运动量 → 计算 → 输出结果"""
    print(f'【{title}】【{duration}天】✊挑战赛')
    n1 = int(input('第1天：'))
    n2 = int(input('第2天：'))
    n3 = int(input('第3天：'))

    total = calc_total(n1, n2, n3)
    avg = calc_avg(total, duration)
    result = check_success(total, goal)

    print(f'总数：{total}，平均值：{avg:.1f}')
    print(result)

main('俯卧撑', 3, 40)
