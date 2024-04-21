# The asyncio module is essential for building high-performance, scalable, and responsive applications, 
# especially those that involve I/O-bound operations. By leveraging asynchronous programming, 
# asyncio allows you to efficiently utilize system resources, handle a large number of concurrent 
# connections, and build responsive user interfaces. It's a powerful tool for building web servers, 
# network clients, web scrapers, and other applications that require high concurrency and responsiveness.

import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['https://www.example.com', 'https://www.google.com', 'https://www.python.org']
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for url, result in zip(urls, results):
        print(f"Response from {url}: {result[:100]}...")

if __name__ == "__main__":
    asyncio.run(main())







# aiohttp is a third-party library used for making HTTP requests asynchronously 
# in Python asyncio applications.

# Explanation:

# We define a coroutine fetch_url that asynchronously fetches the contents of a URL using the aiohttp library.
# In the main coroutine, we create a list of URLs to fetch asynchronously.
# We create a list of coroutine objects (tasks) by calling the fetch_url coroutine for each URL.
# We use asyncio.gather to concurrently execute all the coroutine tasks and wait for their results.
# Finally, we print the first 100 characters of each response.