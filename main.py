import tkinter as tk
import getInfo as gi
##### for sample text on info page #####
import lorem as l

def showPage(page):
  page.tkraise()

bg1 = 'black'
bg2 = 'light slate blue'
up = 'green3'
down = 'red3'
textColor = 'white'
infoText = l.text()
statsFont = ('Arial', 11, 'normal')

def submit():
  coin = coinEntry.get()
  coinParts = coin.split()

  if len(coinParts) > 1:
    newCoinList = []
    for part in coinParts:
      newCoinList.append(part.capitalize())
      Coin = ' '.join(newCoinList)
  else: 
    Coin = coin.capitalize()

  statsDict, abrv = gi.getStats(coin)
  infoDict = gi.getInfo(coin)

  infoTitle.config(text=f'{Coin} ({abrv})')
  title.config(text=f'{Coin} ({abrv})')

  fillStats(statsDict)
  fillInfo(infoDict)

  coinEntry.delete(0,50)

def fillInfo(dictionary):
  infoString = ''
  for string in dictionary:
    infoString += (string + '\n\n')
  
  info.configure(state='normal')
  info.delete(1.0, 'end')
  info.insert(1.0, infoString)
  info.configure(state='disabled')

def fillStats(dictionary):
  price, usdChange, perChange, circulatingSply, maxSply, marketCap, volume = dictionary['price'], dictionary['usdChange'], dictionary['perChange'], dictionary['circulatingSply'], dictionary['maxSply'], dictionary['marketCap'], dictionary['volume']

  if perChange[0] == '-':
    usdChnge.config(fg=down)
    pChange.config(fg=down)
  else: 
    usdChnge.config(fg=up)
    pChange.config(fg=up)

  coinPrice.config(text=price)
  usdChnge.config(text=usdChange)
  pChange.config(text=perChange)
  circulating.config(text=circulatingSply)
  maxS.config(text=maxSply)
  marCap.config(text=marketCap)
  vol.config(text=volume)
  nextBtn.place(relx=.84, rely=.885, relwidth=.15, relheight=.1)

  
root = tk.Tk()
root.geometry("600x400")
root.title('Crypto')

# STATS PAGE
statsFrame = tk.Frame(root, width=600, height=400, bg=bg1)
statsFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

# INFO PAGE
infoFrame = tk.Frame(root, width=600, height=400, bg=bg1)
infoFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

# STATS LAYOUT
# this is only if I can figure out how to webscrape an image, if not I will reformat the page with the same information just not the image
icon = tk.Label(statsFrame, text='icon here')
icon.place(relx=0.025, rely=0.05, relwidth=0.2, relheight=0.3)

title = tk.Label(statsFrame, text='Coin Name', font=('Arial', 19, 'bold'), bg=bg1, fg=textColor)
title.place(relx=0.25, rely=0.05)

coinPrice = tk.Label(statsFrame, text='Price', font=('Arial', 16, 'normal'), bg=bg1, fg=textColor)
coinPrice.place(relx=0.25, rely=0.175)

usdChnge = tk.Label(statsFrame, text='24hr Chng (USD)', bg=bg1, fg=down)
usdChnge.place(relx=0.25, rely=0.296)

pChange = tk.Label(statsFrame, text='24hr Change (%)', font=('Arial', 14, 'normal'), bg=bg1, fg=up)
pChange.place(relx=0.7, rely=0.18)

volumeLabel = tk.Label(statsFrame, text='24 Hour Volume: ', font=statsFont, bg=bg1, fg=textColor)
volumeLabel.place(relx = 0.025, rely=0.5)
vol = tk.Label(statsFrame, text='volume', font=statsFont, bg=bg1, fg=textColor)
vol.place(relx=0.25, rely=0.5)

mcLabel = tk.Label(statsFrame, text='Market Cap:', font=statsFont, bg=bg1, fg=textColor)
mcLabel.place(relx=0.025, rely=0.7)
marCap = tk.Label(statsFrame, text='marketcap', font=statsFont, bg=bg1, fg=textColor)
marCap.place(relx=0.19, rely=0.7)

circLabel = tk.Label(statsFrame, text='Circulating Supply: ', font=statsFont, bg=bg1, fg=textColor)
circLabel.place(relx=0.485, rely=0.5)
circulating = tk.Label(statsFrame, text='circulatingsupply', font=statsFont, bg=bg1, fg=textColor)
circulating.place(relx=0.72, rely=0.5)

maxLabel = tk.Label(statsFrame, text='Maximum Supply: ', font=statsFont, bg=bg1, fg=textColor)
maxLabel.place(relx=0.485, rely=0.7)
maxS = tk.Label(statsFrame, text='maxsupply', font=statsFont, bg=bg1, fg=textColor)
maxS.place(relx=0.715, rely=0.7)

prevBtn = tk.Button(statsFrame, text="< Previous", command=lambda:showPage(infoFrame))
prevBtn.place(relx=.01, rely=.885, relwidth=.15, relheight=.1)

# INFO LAYOUT
infoTitle = tk.Label(infoFrame, text='--', bg=bg1, fg=textColor,  font=('Arial', 15, 'bold'))
infoTitle.place(relx=0, rely=0.01, relwidth=1, relheight=0.08)

info = tk.Text(infoFrame, bg=bg2)
info.insert(1.0, infoText)
# this makes it so you cant edit the text
info.configure(state='disabled')
info.place(relx=0, rely=0.1, relwidth=1, relheight=0.77)

coinLabel = tk.Label(infoFrame, text='Enter A Coin: ', bg=bg1, fg=textColor, anchor=tk.W)
coinLabel.place(relx=0.02, rely=0.885, relwidth=0.3, relheight=0.1)

coinEntry = tk.Entry(infoFrame, width=13)
coinEntry.place(relx=0.18, rely=0.903)

infoBtn = tk.Button(infoFrame, text='Show Info', bg='white', command=submit)
infoBtn.place(relx=.4, rely=.9, relwidth=.15, relheight=.06)

nextBtn = tk.Button(infoFrame, text="Next >", command=lambda:showPage(statsFrame), bg='white')

root.mainloop()