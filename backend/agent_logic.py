from langchain_community.chat_models import ChatOllama
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from streaming_callback import StreamingCallback
from tools import tools

def generate_tasks_stream(goal: str):
    
    callback = StreamingCallback()

    
    llm = ChatOllama(
        model="mistral",
        streaming=True,
        callbacks=[callback],
        temperature=0.7
    )

    
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
        handle_parsing_errors=True,
        max_iterations=6,
        agent_kwargs={
            "prefix": (
                "You can use the following tools:\n"
                "- Current Date Tool: returns today's system date.\n"
                "- Current Time Tool: returns current system time.\n"
                "- File Reader Tool: reads contents of sample_data.txt.\n\n"
                "Format your reasoning exactly like this:\n"
                "Thought: I need the current date.\n"
                "Action: Current Date Tool\n"
                "Action Input: ''\n"
                "Observation: 2025-07-20\n"
                "Thought: Now I need the file contents...\n"
                "Action: File Reader Tool\n"
                "Action Input: ''\n"
                "Observation: (contents of sample_data.txt)\n"
                "Final Answer: [One complete summary or checklist. Do not loop or repeat.]\n"
                )
            }
    )


    callback.reset()
    agent.run(goal)

    
    return callback.get_stream()