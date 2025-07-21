# agents/output_agent.py

from llm.groq_wrapper import GroqLLM

class OutputAgent:
    def __init__(self, llm: GroqLLM):
        self.llm = llm

    def run(self, code: str, sample_input: str) -> str:
        """
        Simulates or predicts the output of the code on the given input.
        """
        prompt = f"""
You are a coding assistant.

The following Python code and input are provided. Please predict the final output this code will generate.

Code:
{code}

Input:
{sample_input}

Return only the output in plain text.
"""
        return self.llm.generate(prompt)
