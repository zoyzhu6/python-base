# 学习目标：if嵌套，缩进控制层级
#
# 嵌套分支：if 里面再写 if
#
# ⚠️ 和 Java 一样，靠缩进区分层级
# if 里面再写 if
age = int(input('年龄：'))
has_report = input('提交体检报告？(是/否)：')
level = int(input('会员等级(1/2/3)：'))

if 18 <= age <= 45:
    if has_report == '是':
        if level == 1:
            print('纪念T恤')
        elif level == 2:
            print('专业跑鞋')
    else:
        print('没提交报告，不能参赛')
else:
    print('年龄不符')
