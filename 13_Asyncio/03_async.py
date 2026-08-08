import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())

'''
aiohttp is an asynchronous HTTP client/server 
library for Python.

Why use ClientSession?
=>Instead of creating a new HTTP connection for 
every request, ClientSession:

Reuses TCP connections.
Improves performance.
Reduces latency.
Is the recommended way to make multiple HTTP 
requests.

Why use asyncio.gather()?

asyncio.gather() runs multiple coroutines concurrently 
and waits for all of them to finish, returning 
their results in the order they were passed.

(*tasks) = > This creates an event loop and runs 
the main() coroutine
'''
