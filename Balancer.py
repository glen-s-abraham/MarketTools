eq=[]
cur_invst=0

n=int(input("Enter the number of stock"))

for i in range(1,n+1):
	print("\nStock ",i,"Details")
	ticker=input("Symbol name:")
	price=float(input("Enter Current value:"))
	qty=float(input("Enter Quantity in hold:"))
	prcnt=float(input("Enter % to allocate:"))
	eq.append([ticker,price,qty,prcnt,(price*qty)])
	cur_invst+=eq[i-1][4]
	print("\n_________________________________________")


print("\nCurrent Investment: ",cur_invst)

extra=int(input("How Much more would you like to invest?(0 if none):"))

finl_invst=cur_invst+extra
print("New Investment: ",finl_invst)
print("\n_________________________________________")

print("\nQTY to add")

for e in eq:
	prtn=((e[3]/100)*finl_invst)
	to_add=((prtn-e[4])/e[1])
	print("How Much to add ",e[0]," :",to_add)