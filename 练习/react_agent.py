# ReAct Agent 完整实现
# 参考：https://www.pythonalchemist.com/blog/react-agent-python

import ast
import operator
import re


# ========== Step 2: 计算器工具 ==========

SAFE_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

def _safe_eval(node):
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in SAFE_OPS:
        return SAFE_OPS[type(node.op)](_safe_eval(node.left), _safe_eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in SAFE_OPS:
        return SAFE_OPS[type(node.op)](_safe_eval(node.operand))
    raise ValueError(f"Unsupported: {ast.dump(node)}")

def calculator(expression: str) -> str:
    tree = ast.parse(expression, mode="eval")
    result = _safe_eval(tree)
    return str(round(result, 4))


# ========== Step 3: 搜索工具 ==========

def search(query: str) -> str:
    knowledge = {
        "eiffel tower": "The Eiffel Tower was completed in 1889 in Paris, France.",
        "python": "Python was created by Guido van Rossum and first released in 1991.",
        "moon": "The Moon is Earth's only natural satellite. It is 384,400 km from Earth.",
    }
    q = query.lower()
    for key, value in knowledge.items():
        if key in q:
            return value
    return f"No results for: {query}"


# ========== Step 4: 工具注册表 ==========

tools = {
    "calculator": {
        "func": calculator,
        "desc": "Evaluates math expressions. Input: '2 + 2' or '100 / 7'",
    },
    "search": {
        "func": search,
        "desc": "Searches for facts. Input: a search query string",
    },
}


# ========== Step 6: 解析 LLM 响应 ==========

def parse_response(text: str) -> dict:
    # 先检查 Final Answer
    m = re.search(r"Final Answer:\s*(.+)", text, re.DOTALL)
    if m:
        return {"type": "final", "answer": m.group(1).strip()}

    # 提取 Thought / Action / Action Input
    thought = re.search(r"Thought:\s*(.+)", text)
    action = re.search(r"Action:\s*(.+)", text)
    action_input = re.search(r"Action Input:\s*(.+?)(?=\nObservation:|\nThought:|\nAction:|$)", text, re.DOTALL)

    if action and action_input:
        return {
            "type": "action",
            "thought": thought.group(1).strip() if thought else "",
            "action": action.group(1).strip(),
            "action_input": action_input.group(1).strip(),
        }
    return {"type": "error", "raw": text}


# ========== Step 7: 执行工具 ==========

def execute_tool(action: str, action_input: str) -> str:
    if action not in tools:
        return f"Error: Unknown tool '{action}'"
    try:
        return tools[action]["func"](action_input)
    except Exception as e:
        return f"Error: {e}"


# ========== Step 1: Mock LLM ==========

class MockLLM:
    def __init__(self, responses: list[str]):
        self.responses = responses
        self.call_count = 0

    def generate(self, prompt: str) -> str:
        if self.call_count >= len(self.responses):
            return "Final Answer: Unknown."
        resp = self.responses[self.call_count]
        self.call_count += 1
        return resp


# ========== Step 5: 构建 Prompt ==========

SYSTEM_PROMPT = """You are a ReAct agent. Think step by step.

Available tools:
{tool_descriptions}

Format your response EXACTLY like:
Thought: your reasoning
Action: tool_name
Action Input: the input to the tool

When you know the final answer:
Thought: I now know the final answer.
Final Answer: your answer

Question: {question}
{scratchpad}"""


def build_prompt(question: str, scratchpad: str) -> str:
    tool_descs = "\n".join(f"- {n}: {t['desc']}" for n, t in tools.items())
    return SYSTEM_PROMPT.format(
        tool_descriptions=tool_descs,
        question=question,
        scratchpad=scratchpad,
    )


# ========== Step 8: Agent 主循环 ==========

def run_agent(question: str, llm, max_steps=5):
    scratchpad = ""
    for i in range(max_steps):
        print(f"\n--- Iteration {i+1} ---")

        prompt = build_prompt(question, scratchpad)
        response = llm.generate(prompt)
        print(response)

        parsed = parse_response(response)

        if parsed["type"] == "final":
            return parsed["answer"]

        if parsed["type"] == "action":
            obs = execute_tool(parsed["action"], parsed["action_input"])
            print(f"Observation: {obs}")
            scratchpad += f"\n{response}\nObservation: {obs}\n"

    return "Max steps reached."


# ========== Step 9: 跑起来 ==========

if __name__ == "__main__":
    llm = MockLLM([
        "Thought: I need to find when the Eiffel Tower was built.\nAction: search\nAction Input: Eiffel Tower",
        "Thought: The Eiffel Tower was built in 1889. Now I calculate the square root.\nAction: calculator\nAction Input: 1889 ** 0.5",
        "Thought: I now know the final answer.\nFinal Answer: The square root of 1889 is approximately 43.46.",
    ])

    answer = run_agent(
        "What is the square root of the year the Eiffel Tower was built?",
        llm,
    )
    print(f"\n✅ Final: {answer}")
