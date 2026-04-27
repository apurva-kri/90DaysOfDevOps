#langchain
from langchain_ollama import ChatOllama
from langchain_core.tools import tool  # here tool is a decorator if we use it on the above of any function then that function will become tool
from langchain.agents import create_agent
#system package
import subprocess #package that can run commands on your terminal

SYSTEM_PROMPT = """
You are a docker expert. Answer in one to two lines max.

STRICT RULES: 
- Only report what the tool actually returned. Never assume or make up output.
- If the tool returns empty or no data, say exactly: "No containers are currently running."
- Never hallucinate. Never suggest commands unless asked.

If there is an actual error from the tool, then:
1/ Say what went wrong in one line
2/ Say the likely root cause in one line
3/ Say the fix in one line
"""

@tool
def show_running_container():
    """tool 1 showing running containers"""
    result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
    return result.stdout

@tool
def show_all_containers():
    """tool 1 showing running containers"""
    result = subprocess.run(["docker", "ps", "-a"], capture_output=True, text=True)
    return result.stdout

@tool
def show_container_logs_by_name(container_name):
    """tool 2 showing running container logs by name"""
    result = subprocess.run(["docker","logs", container_name], capture_output=True, text=True )
    return result.stdout

llm = ChatOllama(model="gemma4", temperature=0.7) #LLM #temp controls the randomness ranges from 0 to 1
tools = [show_running_container,show_container_logs_by_name,show_all_containers] #Tools

agent = create_agent(llm,tools)
user_input = input("Enter your message:\n")
response = agent.invoke({"messages" : [{'role' : 'system', 'content' : SYSTEM_PROMPT},{
        'role': 'user',
        'content': user_input,
        }]})

print(response['messages'][-1].content)