###A -> Monthy expences
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

##B -> Heros
heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heros))
# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange
#    Do that with one line of code.
heros = [i for i in heros if i not in ('thor', 'hulk')]
heros.insert(1,'doctor strange')
#heros[1:3] = ["doctor strange"]
print(heros)
# 5. Sort the heros list in alphabetical order 
# (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)

###C -> Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

m = input()
print("You enter this max number: ",m)
print("The list of odd numbers is: ",[m for m in range(1, int(m)+1) if m%2 != 0 ])
