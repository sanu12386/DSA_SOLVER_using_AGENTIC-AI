# agents/dryrun_agent.py

from llm.groq_wrapper import GroqLLM

class DryRunAgent:
    def __init__(self, llm: GroqLLM):
        self.llm = llm

    def run(self, code: str, sample_input: str) -> str:
        """
        Simulates a dry run of the code on the provided input.
        Outputs step-by-step variable changes and logic flow.
        """
        prompt = f"""
You are a teaching assistant.

Below is a piece of code and a sample input. Perform a dry run of the code.
Explain how the variables change in each iteration and how the logic flows.

Code:
{code}

Input:
{sample_input}
"""
        return self.llm.generate(prompt)
