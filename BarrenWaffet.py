import pandas as pd
import pandas_datareader as pdr
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import math

company=input("Enter Ticker:")

c=company.upper()
data=pd.read_html(f'https://www.screener.in/company/{c}/')
cflow=data[7]
pnl=data[1]
col=pnl.columns.values.tolist()
revenue=[]
income=[]
eps=[]
div=[]
for i in range(1,len(col)):
	revenue.append(float(pnl[col[i]][0]))
	income.append(float(pnl[col[i]][9]))
	eps.append(float(pnl[col[i]][10]))
	div.append(pnl[col[i]][11])
for i in range(0,len(div)-1):
	div[i]=float(div[i].replace('%',''))


plot1=plt.figure("P&L data Visualization")	
plt.subplot(2,3,1)
plt.title("Revenue vs income")
plt.plot(col[1:],revenue,'r',label="Revenue")
plt.legend()
plt.plot(col[1:],income,'b',label="Income")
plt.legend()
plt.xticks(rotation = 90)		
plt.subplot(2,3,2)
plt.title("EPS")
plt.bar(col[1:],eps)
plt.xticks(rotation = 90)
plt.subplot(2,3,3)
plt.bar(col[1:],div)
plt.title("Divident")	
plt.xticks(rotation = 90)

#cashflow
oa=[]
ia=[]
fa=[]
col=cflow.columns.values.tolist()
for i in range(1,len(col)):
	oa.append(float(cflow[col[i]][0]))
	ia.append(float(cflow[col[i]][1]))
	fa.append(float(cflow[col[i]][2]))
plot2=plt.figure("Cash flow distribution")
plt.title("Cash flow distribution")
plt.plot(col[1:],oa,'r',label='OA')
plt.legend()
plt.plot(col[1:],ia,'g',label='IA')
plt.legend()
plt.plot(col[1:],fa,'b',label='FA')
plt.legend()
plt.axhline(y=0, color='black')
plt.show()
