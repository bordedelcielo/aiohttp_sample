# confirmed to be working on unix
# todo - Make a Windows module

from aiohttp import ClientSession
from asyncio import gather, new_event_loop, set_event_loop

def process_data(input, output=[]):

    # First code block
    async def get_url(url):
        async with ClientSession(trust_env=True) as session: # trust_env=True helps avoid "too many files" error
            async with session.get(url) as res:
                data = await res.json()
                output.append(data)

    # Second code block: get data for items in iterable
    async def get_urls(an_iterable):
        await gather(*[get_url(i) for i in an_iterable])

    # Third code block: create loop
    loop = new_event_loop()
    set_event_loop(loop)
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop.run_until_complete(get_urls(input))
    loop.close()

    return output

base_url = 'https://pokeapi.co/api/v2/pokemon/'

pokemon = [
    'pikachu',
    'raichu',
    'pichu',
    'jigglypuff',
    'mewtwo',
    'snorlax',
    'lucario',
]

urls = [base_url + i for i in pokemon]

for i in range(100):
    urls.append(base_url + 'pikachu')

for i in urls:
    # print(i)
    pass

data = process_data(urls)

print(len(data))