from langchain_core.callbacks.base import BaseCallbackHandler

class StreamingCallback(BaseCallbackHandler):
    def __init__(self):
        self.queue = []

    def reset(self):
        self.queue = []

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.queue.append(token)

    def on_text(self, text: str, **kwargs) -> None:
        self.queue.append(f"\nThought: {text}\n")

    def on_tool_start(self, tool_name: str, input_str: str, **kwargs) -> None:
        self.queue.append(f"\nAction: {tool_name}\nInput: {input_str}\n")

    def on_tool_end(self, output: str, **kwargs) -> None:
        self.queue.append(f"Observation: {output}\n")

    def get_stream(self):
        for token in self.queue:
            yield token