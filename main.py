import asyncio
import twscrape
from twscrape import gather

async def main():
    api = twscrape.API()

    user_id = 360887604
    await api.user_by_id(user_id)
    resultado = await gather(api.user_tweets(user_id, limit=20))

    with open('tweets.txt', 'w', encoding='utf-8') as file:
        for tweet in resultado:
            file.write(f'{tweet}\n')

if __name__ == "__main__":
    asyncio.run(main())