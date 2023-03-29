import requests
from bs4 import BeautifulSoup

word = 'dog'
url = 'https://www.google.com/search?tbm=isch&q={0}&tbs=isz:lt,islt:2mp'.format(word)
content = requests.get(url).content
soup = BeautifulSoup(content,'lxml')
images = soup.findAll('img')

for image in images:
    print(image.get('src'))