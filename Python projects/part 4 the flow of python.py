#the basic if statment: the code is only run if the boulion value gives: true.
x = int(50/6)
if x > 10:
	print('the number is higher then 10')
	if x > 15:
		print ('higher then 10?? Its higher then 15!')

elif x == 5:
	print('the number is 5')
elif x == 6:
	print('the number is 6')
elif x == 7:
	print('the number is 7')
elif x == 8:
	print('the number is 8')
elif x == 9:
	print('the number is 9')
elif x == 10:
	print('the number is 10')

else:
	print('the number is lower then 5 :(')

if x >= 5:
	print(f'the result of your equation was {x}, it was a nice number')

else:
	print('numbers lower then 5 suck')

#exersise:
money_available = 140

if money_available >=80:
	print('eat something fancy!')

elif money_available > 45:
	print('eat something nice')

elif money_available > 15:
	print('eat something okay')

else:
	print('eat something cheap')


#complex if statments: And/or
#example: if: (true) and (true) and (false) = False
#		  if: ((true) and (true) and (false)) or true) = true
x = 1
y = 1

if x > 6 or y > 4:
	print('one of them is true :)')
	if x > 6 and y > 4:
		print ('seems like both of them are!')

else:
	print('seems like you picked some low ass numbers')

#Exersise: check if money >80 and if hungry > 40 and bored < 40
	ex_money_available = 70
	hungry	= 10
	bored   = 10

if ex_money_available >80 and hungry >=40 and bored <= 40:
	print('we going to eat')

else:
	if ex_money_available <80: 
		print ('guess i dont have the money')
	if hungry <=40:
		print ('im just not that hungry')
	if bored <= 40:
		print ('dont think im bored enough')


#nested if statments:
x = ' '

if x in ['a','b','4','5','s','%',' ']:
	print('the variable is in the list')
	if  x.isalpha():
		print(f'and it is the letter {x}')
	elif x.isdigit():
		print(f'its the number {x}')
	elif x == ' ':
		print(f'please put something in there not a space, its not funny....')
	else:
		print(f'its the symbol {x}')
	
import random
items = ['1','2','3','4','5','6']
x = int(random.choice(items))
if (x <= 2):			 print('you rolled 1 or 2')
elif (3 >= x <= 4):	 	 print('you rolled 3 or 4')
elif (5 >= x <=6):		 print('you rolled 5 or 6')
print(x)


#match case: pick 1 result out of multiple options.
mood = 'horney'

match mood:
	case 'hungry':
		print('im hungry!')
	case 'tired':
		print ('go to sleep')
	case 'thirsty':
		print ('go drink something')
	case _:
		print('case is not in the database')

#the while loop: repeats code as long as a condition is true:

x = 1
y = 4

while (y < 10):
	y += 1
	print(y)

	if y == 7:
		print('at this point y = 7')
		#break			#end the entire while loop
		#continue		#ends the 'if' statment its placed in
		print('i like pudding') 
	if y == 9:
		print ('pudding is nice!') #continue prints this + 8 9 10
								   #break stops the while loop so print stops at 7.

#exersise: use a while loop to create a list with even vallues from 0-100.
#my idea:
list_of_numbers = []
q = -2

while q < 100:
	q += 2
	list_of_numbers.append(q)

list_of_numbers.remove(58)

print(list_of_numbers)

#exersise result:

my_list = []
counter = 0

while counter <= 100:
	if counter %2 == 0 and counter != 58:	#easy tool to print only even or odd values.
		if counter != 58:					#remove 58 using the != 'is not' command.
			my_list.append(counter)
	counter += 1

print(my_list)

#for loop: run code for every item in a container:
basic_list 		= [4,5,6]
basic_tuple 	= (1,2,3)
basic_dict		= {1:'one', 2: 'two', 3: 'three'}
basic_set		= {1,2,3}
basic_string	= 'One two three'
basic_num		= 3

for x in basic_dict.items():      #stands for every item in the list.
	print(x)				  	  #print


#you can print ranges: ranges by default count from 0 to the specified number:
print(range(6)) 			#prints (0, 6)
print(range(10,20,2))		#starts at 10 moves to 20 (not including 20) by steps of 2

for x in range(10,20,2):	#prints 10/12/14/16/18
	print(x)

#exersise: my attempt:
practice_list = [[10,40,20,50],[2,42,10],[101,10,4]]
new_list= []
#only print numbers below 50, dont print numbers under 10, break if <100.
for x in list(practice_list[0]):
	if x >= 100:
		break

	if x < 50 and x >= 10:
		new_list.append(x)

for x in list(practice_list[1]):
	if x >= 100:
		continue

	if x < 50 and x >=10:
		new_list.append(x)

for x in list(practice_list[2]):
	if x >= 100:
		continue

	if x < 50 and x >=10:
		new_list.append(x)

print(new_list) #new_list contains every number between 10 and 50 and doesnt include numbers over 100.

#exersise result:
for nested_list in practice_list:		#targets the nested_lists in the practice_list.
	for value in nested_list:			#takes every datapoint from the nested list.
		if value > 100:
			break
		if value < 50:
			if value < 10:
				continue
			print(value)

#compact syntax:
x,y = 7,5
if x<5: color='blue'
else:	color='red'
print(color)

#or:
x = 10
color = 'red'if x < 5 else 'blue'
print(color)

#ternary operator:
print(f"the color is {'red'if x < 5 else 'blue'}")
a = ['red'if x < 5 else 'blue']
print(a)







