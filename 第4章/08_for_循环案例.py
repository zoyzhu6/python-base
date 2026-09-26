# for 加密案例
#
# ord() 字符→编码，chr() 编码→字符
# 加密：每个字符的 Unicode 编码 +1
text = input('输入要加密的文字：')
secret = ''
for t in text:
    secret += chr(ord(t) + 1)
print(f'加密后：{secret}')
