class InputAgent:
    def __init__(self, llm=None):
        self.llm = llm

    def process_input(self, user_input: str) -> str:
        cleaned_input = user_input.strip()
        return f"✅ Input received and cleaned:\n{cleaned_input}"

    def run(self, state: dict) -> dict:
        user_input = state.get("input", "")
        result = self.process_input(user_input)
        state["processed_input"] = result
        return state
