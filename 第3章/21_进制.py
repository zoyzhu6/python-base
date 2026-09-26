# 进制：0b二进制 0o八进制 0x十六进制，bin/oct/hex转换
# 0b 二进制  0o 八进制  0x 十六进制
n1 = 0b11001   # 25
n2 = 0x1cf     # 463

# bin() oct() hex() 转字符串
print(bin(25), oct(540), hex(463))

# int('数值', 进制) 转十进制
print(int('1cf', 16))   # 463
