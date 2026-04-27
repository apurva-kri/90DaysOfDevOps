from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "docker-mcp": {
                "transport": "stdio",
                "command": "C:\\Users\\apurv\\Downloads\\90DaysOfDevOps\\agenticai\\venv\\Scripts\\python.exe",
                "args": ["C:\\Users\\apurv\\Downloads\\90DaysOfDevOps\\agenticAI\\mcp_server.py"]
            }
        }
    )
    tools = await client.get_tools()
    llm = ChatOllama(model="gemma4", temperature=0)
    agent = create_agent(llm, tools)
    response = agent.invoke({
        "messages": [
            {"role": "system", "content": "You are a docker expert. Only report what the tool returned."},
            {"role": "user", "content": "How many containers are running"}
        ]
    })
    print(response['messages'][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
