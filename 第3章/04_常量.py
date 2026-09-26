# 常量：全大写命名
#
# ⚠️ Java vs Python 差异：
#   Java：final static int MAX = 100;  ← final 关键字，编译器强制
#   Python：MAX = 100                   ← 全大写只是约定，技术上能改
# 常量：全大写命名，约定不修改（Python 没有真正的常量）
ADULT_AGE = 18
MONTHS_IN_YEAR = 12
MAX_USERS = 1200

print(ADULT_AGE, MONTHS_IN_YEAR, MAX_USERS)
