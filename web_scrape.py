import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User: ')
url = f'https://github.com/{github_user}'
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'width' : '260'})['src']
print(profile_image)



