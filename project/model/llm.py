class Llm:
    def __init__(self, api_key: str, prompts: dict):
        self.api_key = api_key
        self.prompts = prompts

    def get_api_key(self) -> str:
        return self.api_key
