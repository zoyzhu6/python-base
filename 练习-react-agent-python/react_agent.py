# 第一步：建立模拟LLM

class MockLLM:
    """A mock LLM that returns scripted responses for testing."""

    def __init__(self, responses: list[str]):
        self.responses = responses
        self.call_count = 0

    def generate(self, prompt: str) -> str:
        """Return the next scripted response."""
        if self.call_count >= len(self.responses):
            return "Thought: I now know the final answer.\nFinal Answer: Unable to determine."
        response = self.responses[self.call_count]
        self.call_count += 1
        return response

# Test it
llm = MockLLM(["First response", "Second response"])
print(llm.generate("Hello"))
print(llm.generate("Hello again"))


# 第二步：定义你的第一个工具：计算器
import ast
import operator

# Safe operators: no exec, no imports, no builtins
SAFE_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

def _safe_eval(node):
    """Walk the AST and evaluate only safe math operations."""
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
    """Safely evaluate a math expression using AST parsing."""
    try:
        tree = ast.parse(expression, mode="eval")
        result = _safe_eval(tree)
        return str(round(result, 4))
    except Exception as e:
        return f"Error: {e}"

# Test it
print(calculator("2 + 2"))
print(calculator("1889 ** 0.5"))
print(calculator("(10 + 5) * 3"))





# 第三步：添加搜索工具
def search(query: str) -> str:
    """Search a mock knowledge base. Replace with a real API in production."""
    knowledge = {
        "eiffel tower": "The Eiffel Tower was completed in 1889 in Paris, France. It is 330 meters tall.",
        "python": "Python was created by Guido van Rossum and first released in 1991.",
        "moon": "The Moon is Earth's only natural satellite. It is 384,400 km from Earth.",
        "react agent": "ReAct was introduced by Yao et al. in 2022. It interleaves reasoning and acting.",
        "population tokyo": "Tokyo has a population of approximately 14 million people.",
        "speed of light": "The speed of light in a vacuum is 299,792,458 meters per second.",
    }
    query_lower = query.lower()
    for key, value in knowledge.items():
        if key in query_lower:
            return value
    return f"No results found for: {query}"

# Test it
print(search("When was the Eiffel Tower built?"))
print(search("Tell me about Python"))



# 第四步：构建工具注册表
# Tool registry: maps names to functions + descriptions
tools = {
    "calculator": {
        "func": calculator,
        "desc": "Evaluates math expressions. Input: a math expression like '2 + 2' or '100 / 7'",
    },
    "search": {
        "func": search,
        "desc": "Searches for factual information. Input: a search query string",
    },
}

def get_tool_descriptions() -> str:
    """Format tool descriptions for the prompt."""
    lines = []
    for name, tool in tools.items():
        lines.append(f"  - {name}: {tool['desc']}")
    return "\n".join(lines)

def get_tool_names() -> str:
    return ", ".join(tools.keys())

print("Available tools:")
print(get_tool_descriptions())




# 第五步：创建 ReAct 提示模板
REACT_PROMPT = """You are a helpful assistant. You have access to these tools:

{tool_descriptions}

Use this EXACT format for every response:

Question: the input question you must answer
Thought: reason about what to do next
Action: the tool to use (must be one of [{tool_names}])
Action Input: the input to pass to the tool
Observation: the result of the action
... (repeat Thought/Action/Action Input/Observation as needed)
Thought: I now know the final answer
Final Answer: the final answer to the original question

Important rules:
- Always start with a Thought
- Always use a tool before giving the Final Answer (unless you already know)
- The Action must be exactly one of: {tool_names}
- When you have enough information, respond with Final Answer

Begin!

Question: {question}
{scratchpad}"""

def build_prompt(question: str, scratchpad: str = "") -> str:
    return REACT_PROMPT.format(
        tool_descriptions=get_tool_descriptions(),
        tool_names=get_tool_names(),
        question=question,
        scratchpad=scratchpad,
    )

# Preview the prompt
prompt = build_prompt("What is 2 + 2?")
print(prompt[:200] + "...")






# 第六步：解析LLM响应
import re

def parse_response(text: str) -> dict:
    """Parse the LLM response to extract thought, action, or final answer."""

    # Check for Final Answer first
    final_match = re.search(r"Final Answer:\s*(.+)", text, re.DOTALL)
    if final_match:
        return {"type": "final", "answer": final_match.group(1).strip()}

    # Check for Action + Action Input. The Action Input pattern uses re.DOTALL
    # with a non-greedy capture so multi-line inputs (e.g. JSON blobs) are fully
    # captured, stopping at the next ReAct keyword or end-of-string.
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

    return {"type": "error", "raw": text}

# Test with different responses
test1 = "Thought: I need to calculate this.\nAction: calculator\nAction Input: 2 + 2"
test2 = "Thought: I now know.\nFinal Answer: The answer is 42."

print("Test 1:", parse_response(test1))
print("Test 2:", parse_response(test2))







# 第七步：安全执行工具
def execute_tool(action: str, action_input: str) -> str:
    """Look up and execute a tool. Returns the observation."""
    tool_name = action.strip().lower()

    if tool_name not in tools:
        available = ", ".join(tools.keys())
        return f"Error: Unknown tool '{tool_name}'. Available: {available}"

    try:
        result = tools[tool_name]["func"](action_input)
        return result
    except Exception as e:
        return f"Error executing {tool_name}: {e}"

# Test it
print(execute_tool("calculator", "10 * 5"))
print(execute_tool("search", "Python programming"))
print(execute_tool("weather", "London"))  # doesn't exist








# 第八步：构建代理循环
def run_agent(question: str, llm, max_iterations: int = 10) -> str:
    """Run the ReAct agent loop."""
    scratchpad = ""

    for i in range(max_iterations):
        # 1. Build prompt with accumulated context
        prompt = build_prompt(question, scratchpad)

        # 2. Get LLM response
        response = llm.generate(prompt)
        print(f"\n--- Iteration {i + 1} ---")
        print(response)

        # 3. Parse the response
        parsed = parse_response(response)

        # 4. Final Answer? We're done!
        if parsed["type"] == "final":
            print(f"\n✔ Agent finished in {i + 1} iteration(s)")
            return parsed["answer"]

        # 5. Action? Execute the tool
        if parsed["type"] == "action":
            observation = execute_tool(parsed["action"], parsed["action_input"])
            # 6. Append to scratchpad (agent's memory)
            scratchpad += f"\nThought: {parsed['thought']}"
            scratchpad += f"\nAction: {parsed['action']}"
            scratchpad += f"\nAction Input: {parsed['action_input']}"
            scratchpad += f"\nObservation: {observation}\n"
        else:
            scratchpad += "\nObservation: Format error. Use Thought/Action/Action Input or Final Answer.\n"

    return "Agent reached max iterations without a final answer."



# 第九步：快跑，你的经纪人！

# Script the LLM responses for our multi-step question
llm = MockLLM([
    # Iteration 1: Search for the Eiffel Tower
    """Thought: I need to find when the Eiffel Tower was built.
Action: search
Action Input: Eiffel Tower""",

    # Iteration 2: Calculate the square root
    """Thought: The Eiffel Tower was completed in 1889. Now I calculate the square root.
Action: calculator
Action Input: 1889 ** 0.5""",

    # Iteration 3: Final answer
    """Thought: I now know the final answer.
Final Answer: The square root of 1889 (the year the Eiffel Tower was built) is approximately 43.46.""",
])

# Run it!
answer = run_agent(
    "What is the square root of the year the Eiffel Tower was built?",
    llm
)
print(f"\n👉 Final Answer: {answer}")


# 第十步：Swap in a Real LLM

from openai import OpenAI

class OpenAILLM:
    """Uses the new Responses API (recommended over Chat Completions)."""

    def __init__(self, model="gpt-5.4"):
        self.client = OpenAI()
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )
        return response.output_text

# Use it exactly like the mock:
# llm = OpenAILLM()
# answer = run_agent("Your question here", llm)
