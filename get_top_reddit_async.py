import aiohttp
import asyncio
import json
import time


async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()


async def get_reddit_top(subreddit, client):
    data = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

    j = json.loads(data.decode('utf-8'))
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        print(str(score) + ': ' + title + ' (' + link + ')')

    print('DONE:', subreddit + '\n')


loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)

group1 = asyncio.gather(get_reddit_top('python', client))
group2 = asyncio.gather(get_reddit_top('programming', client))
group3 = asyncio.gather(get_reddit_top('compsci', client))
all_groups = asyncio.gather(group1, group2, group3)

start = time.time()
results = loop.run_until_complete(all_groups)
end = time.time()
print('async time: ', end - start)

loop.close()
