# agents/approach_agent.py

from llm.groq_wrapper import GroqLLM

class ApproachAgent:
    def __init__(self, llm: GroqLLM):
        self.llm = llm

    def run(self, problem: str) -> str:
        """
        Uses the LLM to generate a brief, optimal approach for solving the given DSA problem.
        """
        prompt = f"""
You are a competitive programming expert.
Read the following DSA problem and explain the best possible approach to solve it in 5-6 concise bullet points:

Problem:
{problem}
"""
        return self.llm.generate(prompt)
