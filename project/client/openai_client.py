from openai import OpenAI

from project.utils.config import Config
import logging

logger = logging.getLogger(__name__)


class OpenAIClient:

    def __init__(self):
        self.config = Config()
        self.client = OpenAI(api_key=self.config.get_llm_key())
        self.prompt = self.config.get_llm_prompt()
        self.content = self.config.get_llm_content()
        logger.info("OpenAIClient initialized")

    def analyze_tweets(self, review):
        prompt = self.prompt.replace("{text_tweet}", review)
        logger.info(f"Generating text with prompt: {prompt} and review tweets: {review}")

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": self.content
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
