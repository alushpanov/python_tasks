import requests
import time


def get_json(url):
    with requests.get(url, headers={'User-agent': 'get top app'}) as response:
        return response.json()


def get_reddit_top(subreddit):
    data = get_json('https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

    for i in data['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        print('{}: {} ({})'.format(score, title, link))

    print('DONE:', subreddit + '\n')


start = time.time()
get_reddit_top('python')
get_reddit_top('programming')
get_reddit_top('compsci')
end = time.time()

print('Usual time: {:.3f}'.format(end - start))
