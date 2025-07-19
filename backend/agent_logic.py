from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from streaming_callback import StreamingCallback

def generate_tasks_stream(goal):
    callback = StreamingCallback()

    llm = ChatOllama(
        model="mistral",
        streaming=True,
        callbacks=[callback]
    )

    prompt = PromptTemplate(
        input_variables=["goal"],
        template="Break the goal '{goal}' into 5 concise, actionable subtasks. Return as a numbered list."
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    chain.run(goal)

    return callback.get_stream()