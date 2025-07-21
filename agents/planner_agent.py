# agents/planner_agent.py

class PlannerAgent:
    def run(self, problem: str) -> str:
        """
        Accepts the problem and prepares it for the next stages.
        Acts as the root initiator in the agentic DSA pipeline.
        """
        plan = f"""🧠 Step 1: Received Problem Statement

Let's solve this DSA problem step by step:
------------------------------------------
{problem}

Proceeding to generate the approach next..."""
        return plan
