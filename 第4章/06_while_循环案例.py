# while 案例：猜错就一直循环
# while 猜谜：猜错就一直循环
answer = '你的心上人'
guess = ''
while guess != answer:
    guess = input('你是什么人？')
    if guess == answer:
        print('✅正确')
