import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

chapters = ['01','02','03','04','05','06','07','08','09','10']

random_chapter = random.choice(chapters)

url = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

verses = soup.findAll("div", attrs={"class":"p"})

verses = verses.findAll('span')

my_verses = []


for verse in verses:
   # print(verse.text.split('  '))
    for v in (verse.text.split("  ")):
        my_verses.append(v)

my_choice = random.choice(my_verses)

print('Chapter:',random_chapter, 'Verse:', my_choice)


