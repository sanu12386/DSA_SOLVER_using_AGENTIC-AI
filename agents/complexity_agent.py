# agents/complexity_agent.py

from llm.groq_wrapper import GroqLLM

class ComplexityAgent:
    def __init__(self, llm: GroqLLM):
        self.llm = llm

    def run(self, code: str) -> str:
        """
        Returns the time and space complexity of the given code.
        """
        prompt = f"""
You are a competitive programming assistant.

Analyze the following Python code and return the time and space complexity using Big-O notation. Also provide a short explanation.

Code:
{code}

Respond in this format:
- Time Complexity:
- Space Complexity:
- Explanation:
"""
        return self.llm.generate(prompt)
