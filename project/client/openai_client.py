from openai import OpenAI


class OpenAIClient:
    """
    OpenAIClient provides methods to interact with the OpenAI API for analyzing tweets.

    Attributes:
        client (OpenAI): An instance of the OpenAI API client.
        ui_manager: An instance of the UI manager for user interaction.
        prompts (dict): A dictionary of prompts for different tasks.
    """

    def __init__(self, llm_class, ui_manager):
        """
        Initializes the OpenAIClient with the given API key.

        Args:
            llm_class (Llm): An instance of the LLM class.
            ui_manager: An instance of the UI manager for user interaction.
        """
        self.client = OpenAI(api_key=llm_class.get_api_key())
        self.ui_manager = ui_manager
        self.prompts = llm_class.get_prompts()

    def choose_prompt(self):
        """
        Allows the user to choose a prompt from the dictionary of prompts.

        Returns:
            str: The selected prompt.
        """
        return self.ui_manager.prompt_select(self.prompts)

    def analyze_tweets(self, review):
        """
        Analyzes a summary of tweets using the OpenAI GPT-3.5-turbo model.

        Args:
            review (str): A summary of tweets to be analyzed.

        Returns:
            str: The analysis result from the OpenAI API.
        """
        prompt_template = self.choose_prompt()
        prompt = prompt_template.replace("{text_tweet}", review)

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert assistant specialized in analyzing tweets. Your task is to provide a "
                        "comprehensive analysis based on the given prompt and tweet content. Be detailed and precise "
                        "in your response."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
