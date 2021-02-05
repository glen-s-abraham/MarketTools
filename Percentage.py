import matplotlib.pyplot as plt

eqts=[]
lbls=[]
prcnts=[]
n=int(input("Enter number of stocks"))

for i in range(1,n+1):
	print("Stock",i)
	p=float(input("Unit Price:"))
	qty=float(input("Quantity:"))
	eqts.append([p,qty,(p*qty)])

tot=0

#total investment
for eqt in eqts:
	tot+=eqt[2]

#calculate percentages	
i=1
for eqt in eqts:
	lbls.append(("Stock"+str(i)))
	prcnts.append((eqt[2]/tot)*100)
	print("Stock ",i,": Percentage",(eqt[2]/tot)*100)
	i+=1

#print and plot

fig1, ax1 = plt.subplots()
ax1.pie(prcnts, labels=lbls, autopct='%1.1f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

