from unicodedata import name
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## 
# 
'''
Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies and display as a formatted output one currency at a time. The output should display the name of the currency, the symbol (if applicable), the current price and % change in the last 24 hrs and corresponding price (based on % change)

Furthermore, for Bitcoin and Ethereum, the program should alert you via text if the value falls below $40,000 for BTC and $3,000 for ETH.

Submit your GitHub URL which should contain all the files worked in class as well as the above.

'''


url = 'https://cryptoslate.com/coins/'
#url = 'https://coinmarketcap.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title)

coin_row = soup.findAll('tr')

for row in coin_row[1:6]:
    td = row.findAll('td')


    name = td[2].text
    print(name)
    
    price = td[4].text
    print(price)
    
    change = td[5].text
    print(change)
    

