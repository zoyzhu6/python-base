# 列表遍历：for 循环 / enumerate 拿下标和值
scores = [62, 50, 80, 95]

# for 遍历
for s in scores:
    print(s)

# enumerate：同时拿下标和值
for i, s in enumerate(scores):
    print(i, s)
