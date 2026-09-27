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