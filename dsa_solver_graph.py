from langgraph.graph import StateGraph, END
from agents.input_agent import InputAgent
from agents.planner_agent import PlannerAgent  # ✅ New
from agents.approach_agent import ApproachAgent
from agents.code_agent import CodeAgent
from agents.dryrun_agent import DryRunAgent
from agents.output_agent import OutputAgent
from agents.complexity_agent import ComplexityAgent
from llm.groq_wrapper import GroqLLM

llm = GroqLLM(api_key="your_groq_api_key")

input_agent = InputAgent(llm)
planner_agent = PlannerAgent()  # ✅ New
approach_agent = ApproachAgent(llm)
code_agent = CodeAgent(llm)
dry_run_agent = DryRunAgent(llm)
output_agent = OutputAgent(llm)
complexity_agent = ComplexityAgent(llm)

graph = StateGraph()

graph.add_node("input", input_agent.run)
graph.add_node("planner", planner_agent.run)  # ✅ New
graph.add_node("approach", approach_agent.run)
graph.add_node("code", code_agent.run)
graph.add_node("dry_run", dry_run_agent.run)
graph.add_node("output", output_agent.run)
graph.add_node("complexity", complexity_agent.run)

graph.set_entry_point("input")
graph.add_edge("input", "planner")      # ✅ New
graph.add_edge("planner", "approach")   # ✅ New
graph.add_edge("approach", "code")
graph.add_edge("code", "dry_run")
graph.add_edge("dry_run", "output")
graph.add_edge("output", "complexity")
graph.add_edge("complexity", END)

dsa_solver = graph.compile()
