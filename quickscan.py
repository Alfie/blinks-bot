import asyncio
from twikit import Client
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv()

USERNAME = os.getenv("USERNAME")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
THRESHOLD = 5

# Initialize client
client = Client('en-US')

async def main():
    await client.login(
        auth_info_1=USERNAME ,
        auth_info_2=EMAIL,
        password=PASSWORD
    )

    
    
    tweets = await client.search_tweet('to:gotchi_council','Latest')
    

    for tweet in tweets:
        print(
          tweet.user.name,
          tweet.text,
          tweet.created_at,
          tweet.reply_count
        )
        if tweet.reply_count > THRESHOLD:
           # TODO: Set up and post blink
           print("test")

asyncio.run(main())
