from langchain_core.callbacks.base import BaseCallbackHandler

class StreamingCallback(BaseCallbackHandler):
    def __init__(self):
        self.queue = []

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.queue.append(token)

    def get_stream(self):
        for token in self.queue:
            yield token
