# 安全计算器：用 AST 解析数学表达式，不用 eval()
#
# 为什么不用 eval()？
#   eval("os.system('rm -rf /')") 能执行任意代码，危险
#   AST 解析只认数学运算，其他一律拒绝

import ast          # Python 内置：把代码字符串解析成语法树
import operator     # Python 内置：加减乘除的函数版本

# 白名单：只允许这些运算符
# key 是 AST 节点类型，value 是对应的数学运算函数
SAFE_OPS = {
    ast.Add: operator.add,        # +
    ast.Sub: operator.sub,        # -
    ast.Mult: operator.mul,      # *
    ast.Div: operator.truediv,    # /
    ast.Pow: operator.pow,       # ** 次方
    ast.USub: operator.neg,      # 负号 -5
}


def _safe_eval(node):
    """递归遍历语法树，只计算数学运算"""

    # 情况1：是整个表达式，取里面的 body 继续算
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)

    # 情况2：是数字常量（比如 2 或 3.14），直接返回值
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    # 情况3：是二元运算（比如 2 + 3）
    # node.left  左边的子节点
    # node.op    运算符类型（+ - * /）
    # node.right 右边的子节点
    if isinstance(node, ast.BinOp) and type(node.op) in SAFE_OPS:
        # 递归算左边，递归算右边，然后调对应的运算函数
        return SAFE_OPS[type(node.op)](
            _safe_eval(node.left),
            _safe_eval(node.right)
        )

    # 情况4：是一元运算（比如 -5）
    if isinstance(node, ast.UnaryOp) and type(node.op) in SAFE_OPS:
        return SAFE_OPS[type(node.op)](_safe_eval(node.operand))

    # 其他情况（函数调用、变量名、导入等）一律拒绝
    raise ValueError(f"不支持的操作: {ast.dump(node)}")


def calculator(expression: str) -> str:
    """安全计算数学表达式"""
    try:
        # 第1步：把字符串解析成语法树（不执行！）
        tree = ast.parse(expression, mode="eval")
        # 第2步：递归遍历语法树，只算允许的数学运算
        result = _safe_eval(tree)
        # 第3步：保留4位小数
        return str(round(result, 4))
    except Exception as e:
        return f"错误: {e}"


# 测试
print(calculator("2 + 2"))           # 4
print(calculator("1889 ** 0.5"))     # 平方根
print(calculator("(10 + 5) * 3"))    # 45
