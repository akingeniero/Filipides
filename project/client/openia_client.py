from openai import OpenAI

class OpenAIClient:
    """
    OpenAIClient provides methods to interact with the OpenAI API for analyzing tweets.

    Attributes:
        client (OpenAI): An instance of the OpenAI API client.
    """

    def __init__(self, api_key):
        """
        Initializes the OpenAIClient with the given API key.

        Args:
            api_key (str): The API key for accessing the OpenAI service.
        """
        self.client = OpenAI(api_key=api_key)

    def analyze_tweets(self, review):
        """
        Analyzes a summary of tweets using the OpenAI GPT-3.5-turbo model.

        Args:
            review (str): A summary of tweets to be analyzed.

        Returns:
            str: The analysis result from the OpenAI API.
        """
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": (
                    f"Based on the following summary of tweets:\n\n{review}\n"
                    "Perform an analysis that includes: 1. Evaluation of the general sentiment towards the "
                    "mentioned topic/party/entity. 2. Analysis of the ideology present in the discussions. 3. "
                    "Estimation of the average engagement of these posts. 4. Probability of confirmation biases in "
                    "the discussions. 5. Probability of bandwagon biases in public opinion."
                )}
            ],
            temperature=0.5,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
