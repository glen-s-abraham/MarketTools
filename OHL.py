import pandas as pd
from os import system

system('cls')

nifty50=pd.read_csv('sm.csv')
ohlBuy=[]
ohlSell=[]
size=len(nifty50)
for i in range(1,size):
	if nifty50['OPEN \n'][i]==nifty50['HIGH \n'][i]:
		ohlSell.append(nifty50['SYMBOL \n'][i])
		
	if nifty50['OPEN \n'][i]==nifty50['LOW \n'][i]:
		ohlBuy.append(nifty50['SYMBOL \n'][i])
		

	#print(nifty50['OPEN \n'][i]==nifty50['HIGH \n'][i])	

#print(nifty50['SYMBOL \n'],nifty50['OPEN \n'],nifty50['HIGH \n'],nifty50['LOW \n'])
print("_________OHL_________")
print("BUY:",ohlBuy)
print("SELL:",ohlSell)
print("_____________________")