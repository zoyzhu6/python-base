# 函数注解：参数:类型 ->返回值类型
def add(x: int, y: int) -> int:
    return x + y

def greet(name: str) -> None:
    print(f'你好{name}')

# 多返回值
def min_max(nums: list[int]) -> tuple[int, int]:
    return min(nums), max(nums)
