#Monthy expences
montly_expense = [['January', 2200], ['February', 2350],	#List of Lists /nested list
				  ['March', 2600],['April', 2130],['May', 2190]]

#1. In Feb, how many dollars you spent extra compare to January?
print("Extra spent: ",(montly_expense[1][1] - montly_expense[0][1]))

#2. Find out your total expense in first quarter of the year.
print("Expences for the first three months: ",montly_expense[0][1] + montly_expense[1][1] + montly_expense[2][1])

#3. Find out if you spent exactly 2000 dollars in any month
b = [el[1] for el in montly_expense]	#[2200, 2350, 2600, 2130, 2190]
c = [el[0] for el in montly_expense] 	#to print the exact month 
#print(type(b))	#<class 'list'>

for i,e in zip(b,c):
	if i == 2000:
		print("Yes, you spent 2000$ in {}".format(e))
		break
	else: print("You didn't spent 2000$ in {}".format(e))

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

june_expense = [['June', 1980]]
montly_expense = montly_expense + june_expense
print("June was added to the list: ",montly_expense)

#5. You returned an item that you bought in a month of April and got a refund of 200$. 
	# Make a correction to your monthly expense list based on this

for n in montly_expense:
	#print(n[0])
	if n[0] == "April":
		n[1] = n[1] - 200

print("April was updated: ",montly_expense)