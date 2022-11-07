from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(service):
    async with aiohttp.ClientSession() as session:
        async with session.get(service.url) as resp:
            json = await resp.json()
            return json[service.ip_attr]


async def asynchronous():
    done, _ = await asyncio.wait(
            [fetch_ip(service) for service in SERVICES],
            return_when=FIRST_COMPLETED
    )
    for future in done:
        print(future.result())

asyncio.run(asynchronous())
