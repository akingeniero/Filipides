import asyncio
import configparser
import twscrape
from openai import OpenAI
from twscrape import gather


async def main():
    config = configparser.ConfigParser()
    with open('config.properties', encoding='ISO-8859-1') as config_file:
        config.read_file(config_file)
    api = twscrape.API()
    user_id = 68740712
    await api.user_by_id(user_id)
    tweets = await gather(api.user_tweets(user_id, limit=20))
    client = OpenAI(api_key=config.get('openAI', 'key'))
    tweet_data_list = []

    for tweet in tweets:
        tweet_data = {
            "id": tweet.id_str,
            "url": tweet.url,
            "date": tweet.date,
            "username": tweet.user.username,
            "displayname": tweet.user.displayname,
            "rawContent": tweet.rawContent,
            "engagement": {
                "replyCount": tweet.replyCount,
                "retweetCount": tweet.retweetCount,
                "likeCount": tweet.likeCount,
                "quoteCount": tweet.quoteCount
            },
            "lang": tweet.lang,
            "mentionedUsers": [user.username for user in tweet.mentionedUsers],
            "hashtags": tweet.hashtags
        }
        tweet_data_list.append(tweet_data)
    review = ""
    for tweet in tweet_data_list:
        review += f"Tweet de {tweet['displayname']} (@{tweet['username']})el {tweet['date']}:\n{tweet['rawContent']}\n"
    review = review[:2000]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"""Basado en el siguiente resumen de tweets:\n\n{review}\nRealiza un 
            análisis que incluya: 1. Evaluación del sentimiento general hacia el tema/partido/entidad mencionada. 2. 
            Análisis de la ideología presente en las discusiones. 3. Estimación de la media de engagement de estas 
            publicaciones. 4. Probabilidad de sesgos de confirmación en las discusiones. 5. Probabilidad de sesgos de 
            bandwagon en la opinión pública."""}
        ],
        temperature=0.5,
        max_tokens=1000
    )

    path = "analisis_sentimiento.txt"
    analisis = response.choices[0].message.content.strip()
    with open(path, "w") as file:
        file.write(analisis.strip())

if __name__ == "__main__":
    asyncio.run(main())