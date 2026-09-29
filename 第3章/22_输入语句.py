# 学习目标：input()获取用户输入，返回字符串
#
# 输入：input()
#
# ⚠️ Java vs Python 差异：
#   Java：Scanner sc = new Scanner(System.in); sc.nextInt();
#   Python：input() 一行搞定，但返回值永远是字符串
# input() 获取用户输入，返回值永远是字符串
name = input('请输入姓名：')
age = int(input('请输入年龄：'))   # 要数字得自己转

print(f'{name}，明年{age + 1}岁')
