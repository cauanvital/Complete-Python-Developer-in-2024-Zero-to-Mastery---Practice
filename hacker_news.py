import requests
from bs4 import BeautifulSoup
from pprint import pprint

res1 = requests.get('https://news.ycombinator.com/news')
soup_obj1 = BeautifulSoup(res1.text, 'html.parser')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup_obj2 = BeautifulSoup(res2.text, 'html.parser')

links = soup_obj1.select('.titleline') + soup_obj2.select('.titleline')
subtexts = soup_obj1.select('.subtext') + soup_obj2.select('.subtext')

def sort_stories_by_vote(hnlist:list):
    return sorted(hnlist, key=lambda x:x['points'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    
    for idx, link in enumerate(links):
        title = link.getText()
        href = link.select('a')[0].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title':title, 'link':href, 'points':points})
    
    return sort_stories_by_vote(hn)

pprint(create_custom_hn(links, subtexts))
