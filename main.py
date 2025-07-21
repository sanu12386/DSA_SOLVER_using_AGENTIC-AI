import streamlit as st
from dotenv import load_dotenv

# Agent imports
from agents.input_agent import InputAgent
from agents.planner_agent import PlannerAgent
from agents.approach_agent import ApproachAgent
from agents.code_agent import CodeAgent
from agents.dryrun_agent import DryRunAgent
from agents.output_agent import OutputAgent
from agents.complexity_agent import ComplexityAgent

from llm.groq_wrapper import GroqLLM

# Load environment variables
load_dotenv()

# Initialize LLM
llm = GroqLLM()

# Initialize Agents
input_agent = InputAgent()
planner_agent = PlannerAgent()
approach_agent = ApproachAgent(llm)
code_agent = CodeAgent(llm)
dry_run_agent = DryRunAgent(llm)
output_agent = OutputAgent(llm)
complexity_agent = ComplexityAgent(llm)

# Streamlit UI setup
st.set_page_config(page_title="Agentic AI - DSA Solver", layout="wide")
st.title("🧠 Agentic AI: DSA Problem Solver")

question = st.text_area("📌 Enter your DSA Question")
sample_input = st.text_input("📥 Enter sample input for dry run and output testing")

if st.button("🚀 Solve DSA Question"):
    if question.strip() == "":
        st.warning("Please enter a DSA question.")
    elif sample_input.strip() == "":
        st.warning("Please enter a sample input.")
    else:
        with st.spinner("🤖 Generating response..."):
            try:
                # Step 0: Input Processing
                cleaned_question = input_agent.process_input(question)
                st.subheader("📥 Step 0: Input Cleaning")
                st.markdown(cleaned_question)

                # Step 1: Planning
                plan = planner_agent.run(question)
                st.subheader("🧠 Step 1: Plan")
                st.markdown(plan)

                # Step 2: Approach
                approach = approach_agent.run(cleaned_question)
                st.subheader("💡 Step 2: Approach")
                st.code(approach)

                # Step 3: Code Generation
                code = code_agent.run(problem=cleaned_question, approach=approach)
                st.subheader("💻 Step 3: Code")
                st.code(code, language='python')

                # Step 4: Dry Run
                dry_run = dry_run_agent.run(code, sample_input)
                st.subheader("🧪 Step 4: Dry Run")
                st.markdown(dry_run)

                # Step 5: Output Generation
                output = output_agent.run(code, sample_input)
                st.subheader("📤 Step 5: Output")
                st.code(output)

                # Step 6: Complexity Analysis
                complexity = complexity_agent.run(code)
                st.subheader("⏱️ Step 6: Time & Space Complexity")
                st.markdown(complexity)

                st.success("🎉 Completed!")

            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")
