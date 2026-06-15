import streamlit as st
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
import time
​st.set_page_config(page_title="Axon Pro", page_icon="⚡", layout="wide")
st.markdown("""<style>.main-title { text-align: center; color: #007BFF; font-size: 50px; font-weight: bold; } .stApp { background-color: #0E1117; } div.stButton > button { border: 2px solid #007BFF; color: white; border-radius: 8px; }</style>""", unsafe_allow_html=True)
st.markdown('<div class="main-title">⚡ AXON PRO AI</div>', unsafe_allow_html=True)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/8649/8649595.png", width=150)
st.sidebar.title("Axon Control Panel")
​def run_axon_engine(task_desc):
api_key = st.secrets["OPENAI_KEY"]
llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=api_key)
coder = Agent(role='Senior Engineer', goal='Write clean, efficient code.', backstory="Expert Python Developer.", llm=llm)
reviewer = Agent(role='Quality Auditor', goal='Critically review code for bugs.', backstory="Senior QA Lead.", llm=llm)
code_task = Task(description=task_desc, agent=coder, expected_output="Production ready Python code")
review_task = Task(description="Critically review the code above.", agent=reviewer, expected_output="Refined and safe code")
crew = Crew(agents=[coder, reviewer], tasks=[code_task, review_task], process=Process.sequential)
return crew.kickoff()
​user_input = st.text_area("What do you want Axon to build?", placeholder="Example: Create a calculator app...")
if st.button("🚀 Deploy Axon Agents"):
if not user_input:
st.warning("Please provide a task!")
else:
with st.status("Initializing Axon Engine...", expanded=True) as status:
st.write("🕵️‍♂️ Agents assigned...")
time.sleep(1)
st.write("💻 Engineer is crafting your code...")
time.sleep(1)
result = run_axon_engine(user_input)
st.write("🔍 Auditor is checking for bugs...")
time.sleep(1)
status.update(label="✅ Build Complete!", state="complete", expanded=False)
st.balloons()
st.success("Axon Pro has finished the job!")
st.code(result, language='python')
