from bs4 import BeautifulSoup as bs
import requests as r

def coinSoup(coin):
  Coin = coin.lower()

  if ' ' in Coin:
    finalCoin = Coin.replace(' ', '-')
  else:
    finalCoin = Coin

  url = f'https://coinmarketcap.com/currencies/{finalCoin}'
  response = r.get(url)
  page = response.text
  soup = bs(page, 'html.parser')

  return soup
                         
def getStats(coin):
  statsDict = {}
  soup = coinSoup(coin)

  price = soup.find('div', class_="priceValue___11gHJ").text


  # class_="sc-16r8icm-0 fIhwvd"
  change = soup.find(class_="sc-16r8icm-0 dxttqv").table.tbody
  usdChange = change.find_all('span')[2].text
  # this makes sure that if the usd change is negative, so is the percentage. I could also change this to just be a percent with an up or down arrown to represent in which direction
  if usdChange[1] == '-':
    perChange = '-' + change.find_all('span')[3].text
  else: 
    perChange = change.find_all('span')[3].text
  
  circulatingSply = soup.find_all(class_="statsValue___2iaoZ")[-1].text

  splyList = circulatingSply.split()
  abrv = splyList[1]

  maxSply = soup.find(class_="maxSupplyValue___1nBaS").text
  maxSply = maxSply + ' ' + abrv
  marketCap = soup.find(class_="statsValue___2iaoZ").text
  volume = soup.find_all(class_="statsValue___2iaoZ")[2].text
  
  statsDict['price'], statsDict['usdChange'], statsDict['perChange'], statsDict['circulatingSply'], statsDict['maxSply'], statsDict['marketCap'], statsDict['volume'] = price, usdChange, perChange, circulatingSply, maxSply, marketCap, volume

  return statsDict, abrv

def getInfo(coin):
  soup = coinSoup(coin)
  info = soup.find(class_="sc-1lt0cju-0 srvSa").div
  fullInfo = []
  finalInfo = []
  for item in info:
    fullInfo.append(item.text)
  
  for item in fullInfo:
    if item[0:13] == 'Related Pages':
      break
    else: 
      finalInfo.append(item)
  
  return finalInfo

