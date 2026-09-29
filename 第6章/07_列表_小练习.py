# 学习目标：列表练习成绩统计
#
# 练习：成绩统计
scores = []  # ⭐ 核心语法
while True:
    s = input('成绩：')
    if s == '结束':
        break
    scores.append(int(s))

print(f'人数：{len(scores)}')
print(f'最高：{max(scores)}')
print(f'平均：{sum(scores)/len(scores):.1f}')
