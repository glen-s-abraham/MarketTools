import pandas as pd
import pandas_datareader as pdr
from matplotlib import pyplot as plt


evaluations={}

#company=input("Enter Ticker:")


#company=company.upper()+".NS"

summary=pd.read_html(f'https://finance.yahoo.com/quote/{company}')


evaluations['pe']=float(summary[1][1][2])

if evaluations['pe']>25:
	evaluations['pe_remarks']="Compare with sectorial peers"
elif evaluations['pe']<25 and evaluations['pe']>15:
	evaluations['pe_remarks']="Security Worth Consideration"
elif evaluations['pe']<10 and evaluations['pe']>0:
	evaluations['pe_remarks']="Good P/E ratio"	

evaluations['eps']=float(summary[1][1][3])

#statistics
statistics=pd.read_html(f'https://finance.yahoo.com/quote/{company}/key-statistics')
evaluations['peg']=statistics[0][1][4]
if evaluations['pe']>1:
	evaluations['peg_remarks']="Over Valued compare with sectorial peers"
elif evaluations['peg']>0 and evaluations['peg']>1:
	evaluations['peg_remarks']="Security Worth Consideration"

evaluations['ps']=statistics[0][1][5]
evaluations['pb']=statistics[0][1][6]	
evaluations['profit_margin']=statistics[5][1][0]
evaluations['roa']=statistics[6][1][0]
evaluations['roe']=statistics[6][1][1]
evaluations['bps']=statistics[8][1][5]