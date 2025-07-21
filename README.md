**🧠 Agentic DSA Assistant**
An interactive Streamlit app powered by LLM agents to help students solve Data Structures and Algorithms (DSA) problems step-by-step — from understanding the problem to generating, analyzing, and dry-running the code.

**🚀 Features**
📝 **InputAgent** – Cleans and validates user input

💡 **IdeaAgent** – Understands the DSA problem and proposes an approach

🧮 **CodeAgent** – Generates Python code based on the proposed approach

🔍 **DryRunAgent** – Simulates a dry run of the code with sample inputs

✅ **OutputAgent** – Evaluates output for correctness

**📸 Demo**-
<img width="1832" height="878" alt="image" src="https://github.com/user-attachments/assets/0ecb118b-0110-4eea-8b13-0b1da0ce4dd3" />

<img width="1753" height="585" alt="image" src="https://github.com/user-attachments/assets/0174dd4c-2e31-4caf-9989-ec6b2f0fc67c" />

<img width="1707" height="797" alt="image" src="https://github.com/user-attachments/assets/496a0ba1-2f38-404e-a962-0ce60e822687" />

<img width="1710" height="850" alt="image" src="https://github.com/user-attachments/assets/706050e6-16b2-44c4-9c6a-90033b319446" />

<img width="1651" height="795" alt="image" src="https://github.com/user-attachments/assets/82dbd40b-a6ca-4e28-8d74-f3b7f9c175fb" />

<img width="1752" height="748" alt="image" src="https://github.com/user-attachments/assets/d0d96045-a153-42e8-8995-7d5798cb8673" />

**📂 Project Structure**
.
├── agents/
│   ├── input_agent.py
│   ├── idea_agent.py
│   ├── code_agent.py
│   ├── dryrun_agent.py
│   └── output_agent.py
├── llm/
│   └── groq_wrapper.py
├── main.py
├── requirements.txt
└── README.md

**💻 Technologies Used**
Python

Streamlit

OpenAI-compatible LLM API (via Groq)

Prompt Engineering

Modular Agent Design







