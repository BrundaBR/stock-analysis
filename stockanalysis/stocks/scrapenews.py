#https://economictimes.indiatimes.com/markets/stocks
# imports 
from bs4 import BeautifulSoup
import requests
#get by url request
req=requests.get('https://economictimes.indiatimes.com/markets/stocks')
#convert to bs
soup=BeautifulSoup(req.content)
# find content
alinks=soup.find("a").text()
print(alinks)

