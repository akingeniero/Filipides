
# Project Title: Filipides

## Project Context

This project aims to confirm the hypothesis that generative intelligence does not inherently possess ethical barriers regarding its usage. By leveraging social network trace extraction, it is possible to conduct sentiment analysis and political framing, as well as generate fictitious support that can amplify our confirmation biases and the backfire effect.

## General Functionality

The program operates by extracting data from social networks and performing various analyses:

1. **Sentiment Analysis**: Evaluates the emotional tone of social media posts.
2. **Political Framing**: Identifies and categorizes political contexts and biases in the content.
3. **Fictitious Support Generation**: Creates artificial support to enhance confirmation biases and backfire effects.

### How It Works

1. **Data Extraction**: The program connects to social media platforms using valid credentials to extract relevant data.
2. **Analysis Production**: Utilizes long language model to perform analysis.

### Configuration Requirements

To run the program, ensure you have the following configurations set up:

- **Twitter Account**: A valid Twitter account to access the Twitter API.
- **Google Account**: A valid Google account for various integrations.
- **OpenAI API Key**: An API key from OpenAI to perform generative tasks.
- **Llama API Key**: An API key from LlamaAPI to perform generative tasks.


### Configuration Requirements

To run the program, ensure you have the following configurations set up in `conf.py`:

```python
user_dic = {
"twitter_user": {
"username": "YOUR_TWITTER_USERNAME",
"password": "YOUR_TWITTER_PASSWORD",
"email": "YOUR_EMAIL",
"account_password": "YOUR_EMAIL_PASSWORD"
}
}
llama_dict = {
"llama": {
"key": "YOUR_LLAMA_API_KEY",
"llms": ["llama3-70b", "llama2-70b"]
}
}
openai_dict = {
"openAI": {
"key": "YOUR_OPENAI_API_KEY",
"llms": ["gpt-4-turbo", "gpt-4o", "gpt-3.5-turbo"],
}
}
```
## Documentation

For detailed documentation on each module and additional configuration options, open the `index.html` file in the `docs/build/html` directory in a web browser:

```bash
open docs/build/html/index.html
```

