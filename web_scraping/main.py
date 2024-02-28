import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github user: ')

url = f'https://github.com/{github_user}'

r = requests.get(url)


if r.status_code == 200:
    soup = bs(r.content, 'html.parser')
    profile_image = soup.find('img',{'class': 'avatar'})['src']
    print(profile_image)
