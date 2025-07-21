class CodeAgent:
    def __init__(self, llm):
        self.llm = llm

    def run(self, problem: str, approach: str, language: str = "python") -> str:
        prompt = f"""
You're a senior software engineer solving DSA problems.

Problem:
{problem}

Approach:
{approach}

Write clean, readable {language} code that follows the above approach.
Only provide code. Do not include any explanation.
"""
        return self.llm.generate(prompt)
