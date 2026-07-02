from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from tools import query_excel, search_web
from llm import llm



memory = MemorySaver()


agent = create_react_agent(
    model=llm,
    tools=[query_excel, search_web],
    checkpointer=memory
)


