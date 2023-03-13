# Python
import requests
from typing import Union, TypeAlias
import time
import asyncio
from decouple import config

# Django
from django.core.management.base import BaseCommand
from django.db import transaction

# Apps
from asyncs.models import Station


dtype: TypeAlias = list[dict[str, Union[str, int]]]


class Command(BaseCommand):
    """Class to create data."""
    
    help = 'Custom command for filling up database.'

    def generate_data(self, *args: tuple, **kwargs: dict) -> None:

        async def create_100_objects(objs: list[dict]):
            stations: list[Station] = []
            
            obj: dict
            for obj in objs:
                station = Station(**obj)
                stations.append(station)
            try:
                with transaction.atomic() as tr:
                    Station.objects.bulk_create(stations)
            except Exception as e:
                print("ERROR TASK:", e)

        def finish(future: asyncio.Future[list], *args, **kwargs) -> None:
            print('Finish')

        async def main(objs: list[dict]):
            tasks: list[asyncio.Task] = []
            i: int
            for i in range(0, len(objs) - 100, 100):
                task = asyncio.create_task(
                    create_100_objects(objs[i:i+100])
                )
                tasks.append(task)
            fut: asyncio.Future = asyncio.gather(*tasks)
            fut.add_done_callback()

        url: str = (
            "https://radio-world-75-000-worldw"
            "ide-fm-radio-stations.p.rapidapi.com/api.php"
        )
        headers = {
	        "X-RapidAPI-Key": config('X-RapidAPI-Key', cast=str),
	        "X-RapidAPI-Host": config('X-RapidAPI-Host', cast=str)
        }
        querystring: requests.sessions._Params = {
            "count": "5000",
            "page": "1",
            "radios": ""
        }
        response: requests.Response = \
            requests.request(
                "GET", 
                url, 
                headers=headers, 
                params=querystring
            )
        
        data = response.json()
        asyncio.run(main(
            data.get('stations')
            )
        )

    def handle(self, *args: tuple, **options: dict) -> None:
        """Handles data filling."""

        start = time.perf_counter()
        self.generate_data()
        print(
            f"Finished by {(time.perf_counter() - start):.2f}sec"
        )
