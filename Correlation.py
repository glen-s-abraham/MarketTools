from nsepy import get_history
import datetime
import matplotlib.pyplot as plt


def get_data(symbol): 
	from datetime import date 
	sdate=datetime.datetime.now().date()
	edate=datetime.datetime.now().date() - datetime.timedelta(days=2*365)
	data = get_history(symbol=symbol, start=edate, end=sdate)
	return data['Close']

try:
	symb1=input("Enter Symbol 1:")
	s1data=get_data(symb1.upper())

	symb2=input("Enter Symbol 2:")
	s2data=get_data(symb2.upper())

	print(s1data.corr(s2data))
	s1data.plot()
	s2data.plot()
	plt.show()
except:	
	print("Exception occured")
		

