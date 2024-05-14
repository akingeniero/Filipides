class Llm:
    """
    Llm manages the configuration for a language model, including API key and prompts.

    Attributes:
        api_key (str): The API key for accessing the language model service.
        prompts (dict): A dictionary of prompts used with the language model.
    """

    def __init__(self, api_key: str, prompts: dict):
        """
        Initializes the Llm with the given API key and prompts.

        Args:
            api_key (str): The API key for accessing the language model service.
            prompts (dict): A dictionary of prompts used with the language model.
        """
        self.api_key = api_key
        self.prompts = prompts

    def get_api_key(self) -> str:
        """
        Retrieves the API key.

        Returns:
            str: The API key.
        """
        return self.api_key
