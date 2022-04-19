from unicodedata import name
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from twilio.rest import Client



##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## 
# 
'''
Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies and display as a formatted output one currency at a time. The output should display the name of the currency, the symbol (if applicable), the current price and % change in the last 24 hrs and corresponding price (based on % change)

Furthermore, for Bitcoin and Ethereum, the program should alert you via text if the value falls below $40,000 for BTC and $3,000 for ETH.

Submit your GitHub URL which should contain all the files worked in class as well as the above.

'''


url = 'https://cryptoslate.com/coins/'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)
print('Ranked by Market Capitalization')
print()

coin_row = soup.findAll('tr')

accountSID = 'AC31a443f768547cfb55cc1feb94765730'

authToken = 'efcc63285753824d85db1e3a9b161acf'

Client = Client(accountSID, authToken)

TwilioNumber = "+17622486473"

mycellphone = "+19703906757"

for row in coin_row[1:6]:
    td = row.findAll('td')

    name = td[2].text
    print('Name and Symbol:',name)

    price = td[4].text
    print('Current Price:',price)
    price = float(td[4].text.replace(',','').replace('$',''))
    
    change = td[5].text
    print('Percent Change in Price over the last 24 hours:',change)
    change = float(td[5].text.replace('','').replace('+','').replace('%',''))
    change = 1 + (change/100)
    #print(change)

    dchange = price/change
    #print(dchange)
    
    mon = float(price - dchange)

    poneg = 'increase'
    if mon > 0:
        poneg = 'increase'
    else:
        poneg = 'decrease'
    
    print('The Price 24 hours ago was:',"${:,.4f}". format(dchange))

    mon = "${:,.4f}". format(mon)

    print('Price Amount Change in last 24 hours:',mon, poneg)

    print('')
    
    if str(td[2].text) == 'Bitcoin BTC ':
        if price <  40000:
            textmessage = Client.messages.create(to=mycellphone, from_=TwilioNumber, body="BTC price is below $40,000!")

            #print(textmessage.status)

    if str(td[2].text) == 'Ethereum ETH ':
        if price < 3000:
            textmessage = Client.messages.create(to=mycellphone, from_=TwilioNumber, body="ETH price is below $3,000!")
            #print(textmessage.status)


#Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope process .\.venv\Scripts\activate








