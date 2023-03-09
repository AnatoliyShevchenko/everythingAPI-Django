import asyncio
import requests
import time


async def check_region(home: str, day: int = 13) -> bool:
    response: requests.Response = \
        requests.get(
            f'https://raw.githubusercontent.com/jokecamp/FootballData/master/EPL%202016%20-%202017/2016-08-{day}.all-epl-games.json'
        )
    
    data: list[dict] = response.json()
    for item in data:
        if item['home'] == home:
            return True
        
    return False

