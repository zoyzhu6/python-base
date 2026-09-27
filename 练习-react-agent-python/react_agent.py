# ============================================
# ReAct Agent：推理 + 行动 循环
# 思路：LLM思考 → 调用工具 → 观察结果 → 再思考 → 直到给出最终答案
# ============================================


# ============================================
# 第一步：模拟一个LLM（不用真调OpenAI，先跑通流程）
# ============================================
class MockLLM:
    """模拟LLM：按预设脚本依次返回回复"""

    def __init__(self, responses: list[str]):
        self.responses = responses   # 预设的回复列表
        self.call_count = 0          # 记录调用了几次

    def generate(self, prompt: str) -> str:
        """每次调用，返回下一条预设回复"""
        # 如果预设回复用完了，就说不知道
        if self.call_count >= len(self.responses):
            return "Thought: I now know the final answer.\nFinal Answer: Unable to determine."
        response = self.responses[self.call_count]
        self.call_count += 1
        return response


# ============================================
# 第二步：工具1 —— 安全计算器
# ============================================
import ast          # 把代码字符串解析成语法树
import operator     # 加减乘除的函数版本

# 白名单：只允许这些运算符
SAFE_OPS = {
    ast.Add: operator.add,        # +
    ast.Sub: operator.sub,        # -
    ast.Mult: operator.mul,      # *
    ast.Div: operator.truediv,    # /
    ast.Pow: operator.pow,       # ** 次方
    ast.USub: operator.neg,      # 负号 -5
}

def _safe_eval(node):
    """递归遍历语法树，只算数学运算"""
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in SAFE_OPS:
        return SAFE_OPS[type(node.op)](_safe_eval(node.left), _safe_eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in SAFE_OPS:
        return SAFE_OPS[type(node.op)](_safe_eval(node.operand))
    raise ValueError(f"Unsupported operation: {ast.dump(node)}")

def calculator(expression: str) -> str:
    """安全计算数学表达式，不用eval()"""
    try:
        tree = ast.parse(expression, mode="eval")
        result = _safe_eval(tree)
        return str(round(result, 4))
    except Exception as e:
        return f"Error: {e}"


# ============================================
# 第三步：工具2 —— 模拟搜索（写死几个答案）
# ============================================
def search(query: str) -> str:
    """搜索知识库（真实环境换成搜索引擎API）"""
    knowledge = {
        "eiffel tower": "The Eiffel Tower was completed in 1889 in Paris, France.",
        "python": "Python was created by Guido van Rossum and first released in 1991.",
        "moon": "The Moon is Earth's only natural satellite. It is 384,400 km from Earth.",
    }
    query_lower = query.lower()
    for key, value in knowledge.items():
        if key in query_lower:
            return value
    return f"No results found for: {query}"


# ============================================
# 第四步：工具注册表 —— 把工具名映射到函数
# ============================================
tools = {
    "calculator": {
        "func": calculator,
        "desc": "计算数学表达式，比如 '2 + 2' 或 '100 / 7'",
    },
    "search": {
        "func": search,
        "desc": "搜索事实信息，输入搜索关键词",
    },
}

def get_tool_descriptions() -> str:
    """把所有工具描述拼成文字，给LLM看"""
    lines = []
    for name, tool in tools.items():
        lines.append(f"  - {name}: {tool['desc']}")
    return "\n".join(lines)

def get_tool_names() -> str:
    return ", ".join(tools.keys())


# ============================================
# 第五步：Prompt模板 —— 告诉LLM该怎么回复
# ============================================
REACT_PROMPT = """你是一个助手。你可以使用这些工具：

{tool_descriptions}

每次回复必须用这个格式：

Question: 你要回答的问题
Thought: 思考下一步该干什么
Action: 用哪个工具（必须是：{tool_names}）
Action Input: 给工具的输入
Observation: 工具返回的结果
...（重复 Thought/Action/Action Input/Observation）
Thought: 我知道最终答案了
Final Answer: 最终答案

现在开始！

Question: {question}
{scratchpad}"""

def build_prompt(question: str, scratchpad: str = "") -> str:
    """把问题和历史记录填进模板"""
    return REACT_PROMPT.format(
        tool_descriptions=get_tool_descriptions(),
        tool_names=get_tool_names(),
        question=question,
        scratchpad=scratchpad,
    )


# ============================================
# 第六步：解析LLM返回的文字
# ============================================
import re

def parse_response(text: str) -> dict:
    """从LLM返回的文字里，提取 Thought / Action / Final Answer"""

    # 情况1：已经给最终答案了
    final_match = re.search(r"Final Answer:\s*(.+)", text, re.DOTALL)
    if final_match:
        return {"type": "final", "answer": final_match.group(1).strip()}

    # 情况2：要调用工具
    action_match = re.search(r"Action:\s*(.+)", text)
    input_match = re.search(r"Action Input:\s*(.+?)(?=\nObservation:|\nThought:|\nAction:|$)", text, re.DOTALL)
    thought_match = re.search(r"Thought:\s*(.+)", text)

    if action_match and input_match:
        return {
            "type": "action",
            "thought": thought_match.group(1).strip() if thought_match else "",
            "action": action_match.group(1).strip(),
            "action_input": input_match.group(1).strip(),
        }

    # 情况3：格式不对
    return {"type": "error", "raw": text}


# ============================================
# 第七步：执行工具
# ============================================
def execute_tool(action: str, action_input: str) -> str:
    """根据工具名，调用对应的函数"""
    tool_name = action.strip().lower()

    if tool_name not in tools:
        available = ", ".join(tools.keys())
        return f"Error: Unknown tool '{tool_name}'. Available: {available}"

    try:
        result = tools[tool_name]["func"](action_input)
        return result
    except Exception as e:
        return f"Error executing {tool_name}: {e}"


# ============================================
# 第八步：Agent主循环 —— 思考→行动→观察→重复
# ============================================
def run_agent(question: str, llm, max_iterations: int = 10) -> str:
    """主循环：最多转10圈，转不出来就放弃"""
    scratchpad = ""   # 历史记录（Thought/Action/Observation的累积）

    for i in range(max_iterations):
        # 1. 把问题和历史拼成prompt
        prompt = build_prompt(question, scratchpad)

        # 2. 问LLM
        response = llm.generate(prompt)
        print(f"\n--- 第{i + 1}轮 ---")
        print(response)

        # 3. 解析LLM回复
        parsed = parse_response(response)

        # 4. 给最终答案了？结束！
        if parsed["type"] == "final":
            print(f"\n✔ 完成，用了{i + 1}轮")
            return parsed["answer"]

        # 5. 要调用工具？执行
        if parsed["type"] == "action":
            observation = execute_tool(parsed["action"], parsed["action_input"])
            # 6. 把这一轮的过程加到历史里（下一轮LLM能看到）
            scratchpad += f"\nThought: {parsed['thought']}"
            scratchpad += f"\nAction: {parsed['action']}"
            scratchpad += f"\nAction Input: {parsed['action_input']}"
            scratchpad += f"\nObservation: {observation}\n"
        else:
            scratchpad += "\nObservation: 格式错误，重新来。\n"

    return "转了太多圈，没得出答案。"


# ============================================
# 第九步：跑起来！
# ============================================
# 预设LLM的回复（真实环境就是调OpenAI）
llm = MockLLM([
    # 第1轮：先搜埃菲尔铁塔
    """Thought: I need to find when the Eiffel Tower was built.
Action: search
Action Input: Eiffel Tower""",

    # 第2轮：知道了1889，算平方根
    """Thought: The Eiffel Tower was built in 1889. Now calculate sqrt.
Action: calculator
Action Input: 1889 ** 0.5""",

    # 第3轮：给最终答案
    """Thought: I now know the final answer.
Final Answer: sqrt(1889) ≈ 43.46""",
])

# 问问题
answer = run_agent(
    "What is the square root of the year the Eiffel Tower was built?",
    llm
)
print(f"\n👉 最终答案: {answer}")
