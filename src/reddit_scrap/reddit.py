import requests
import time
user_agent = "#hacksurreymk2 @baahorn i'm scraping spongebob memes to train something to replace them with others"

base = 'https://reddit.com/r/BikiniBottomTwitter/new.json'

def req(url, params):
    r = requests.get(
        url,
        params=params,
        headers={
            'User-Agent': user_agent,
        }
    )
    return r.json()

def reddit_batch(latest=None):
    urls = []
    last = ''
    raw = req(base, {'limit': 100, 'after': latest })
    for child in raw['data']['children']:
        url = child['data']['url']
        last = child['data']['name']
        if 'https://i.redd.it/' in url:
            urls.append(url)

    return last, urls

def main():
    urls = []
    last = None
    for i in range(0, 2):
        last, l_urls = reddit_batch(last)

        print('\n'.join(l_urls))
        urls += l_urls
        time.sleep(0.5)

    #print('\n'.join(urls))

if __name__ == "__main__":
    main()
