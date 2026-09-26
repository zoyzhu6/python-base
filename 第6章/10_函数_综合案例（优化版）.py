# 综合案例：健身统计
def calc_total(*nums):
    return sum(nums)

def main(title, days):
    nums = []
    for i in range(days):
        nums.append(int(input(f'第{i+1}天：')))
    total = calc_total(*nums)
    print(f'总数：{total}，平均：{total/days:.1f}')

main('俯卧撑', 3)
