from LLMClient import LLMClient
from ReActAgent import ReActAgent
from tool import AVAILABLE_TOOLS

if __name__ == "__main__":
    client = LLMClient(model_name="gpt-4o-mini")
    agent = ReActAgent(llm_client=client, tools=AVAILABLE_TOOLS, max_steps=5)
    
    # A query that requires multiple tool uses
    query = "What time is it right now? Take the current hour (in UTC) and multiply it by 14."
    agent.run(query)

    query = "What date is it right now? add the yyyy+mm+dd together and tell me the result."
    agent.run(query)