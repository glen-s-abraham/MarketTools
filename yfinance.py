#statistics url:https://in.finance.yahoo.com/quote/ASHOKLEY.NS/key-statistics?p=ASHOKLEY.NS
#summary url:https://in.finance.yahoo.com/quote/TATAMOTORS.NS?p=TATAMOTORS.NS

import pandas as pd
import pandas_datareader as pdr

company=input("Enter Ticker:")


company=company.upper()+".NS"

summary=pd.read_html(f'https://finance.yahoo.com/quote/{company}')
historical=pd.read_html(f'https://finance.yahoo.com/quote/{company}/history')
analytics=pd.read_html(f'https://finance.yahoo.com/quote/{company}/analysis')

current=float(historical[0]['Adj Close**'][0])
eps=float(summary[1][1][3])
growth=float(analytics[5][company][4].replace('%',''))
bond=float(input("Enter Yield on a AAA bond:"))
value=(eps*(8.5+(2*growth))*8.5)/bond

print("\n","Current :",current)
print("\n",summary[1][0][3],": ",eps)

print("\n",analytics[5]['Growth Estimates'][4],": ",growth)
print("\n","AAA secure Corporate bond intrest:",bond)

print("\n","Intrinsic Value:",value)




