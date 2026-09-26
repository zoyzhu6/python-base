# 列表增删改查：append/insert/pop/remove/下标赋值
nums = [10, 20, 30]

# 增：append 末尾追加 / insert 指定位置插入 / extend 合并另一个列表
nums.append(40)
nums.insert(1, 99)
nums.extend([50, 60])

# 删：pop(下标) / remove(值) / clear()
nums.pop(0)
nums.remove(20)

# 改：nums[下标] = 新值
nums[0] = 66

print(nums)
