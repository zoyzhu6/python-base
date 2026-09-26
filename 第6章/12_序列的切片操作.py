# 切片 [起:止:步长]
#
# ⚠️ Java 没有切片！Python 独有
#   ❌ Java：subList(1, 4)  要写循环
#   ✅ Python：nums[1:4]  一行搞定
#   nums[::-1]  反转列表

#
# ⚠️ Java 没有切片！
#   Python：nums[1:4] 取第1到第3个
#   nums[::-1] 反转
nums = [10, 20, 30, 40, 50, 60]
print(nums[1:4])     # [20,30,40]
print(nums[:3])      # [10,20,30]
print(nums[2:])      # [30,40,50,60]
print(nums[::2])     # [10,30,50]
print(nums[::-1])    # 反转 [60,50,40,30,20,10]
