# w覆盖写 a追加写
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('第一行\n')
    f.write('第二行\n')

# a 模式：追加写
with open('test.txt', 'a', encoding='utf-8') as f:
    f.write('追加一行\n')
