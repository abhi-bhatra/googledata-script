# script to fetch the images from ecommerce website
#

import requests
from bs4 import BeautifulSoup

word = 'MyGlamm XOXO Valentines Range- Powder Blush Love XO09'
url = 'https://www.google.com/search?q={0}&tbm=isch&&tbs=isz:ex,iszw:1200,iszh:1200'.format(word)
content = requests.get(url).content

soup = BeautifulSoup(content,'lxml')
images = soup.findAll('img')

for image in images:
    print(image.get('src'))