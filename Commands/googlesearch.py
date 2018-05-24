from googleapiclient.discovery import build
from main import client
import discord.ext


def google_search(search_term, api_key, cse_id, **kwargs): 
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']
    
@client.command()
async def gsearch(*args):
    from discord_token import my_api_key
    from discord_token import my_cse_id
    wut = ''
    for words in args:
        wut += words
        wut += ' '
        results= google_search(wut,my_api_key,my_cse_id,num=1) 
    for result in results:
        await client.say(str(result['link']))
        