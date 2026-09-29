# 学习目标：raise手动抛异常
#
# raise手动抛出异常
def set_age(age):
    if age < 0:
        raise ValueError('年龄不能为负')
    return age

# set_age(-1)  # 会报错
