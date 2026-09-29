# 学习目标：for遍历列表，enumerate同时拿下标和值
#
# 列表遍历
#
# ⚠️ Java vs Python 差异：
#   Java：for (int i = 0; i < list.size(); i++)
#   Python：for item in list:  ← 直接遍历元素
#   enumerate() 同时拿下标和值
scores = [62, 50, 80, 95]

# for 遍历
for s in scores:
    print(s)

# enumerate：同时拿下标和值
for i, s in enumerate(scores):
    print(i, s)
