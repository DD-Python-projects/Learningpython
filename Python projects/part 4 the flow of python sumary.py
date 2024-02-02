#the flow of python is controled by using boliouns that give true or false:
#boulions: check how a variable compares to another variable.
#opirators: If, Else, Elif, case, while, for, and.

#variables used:
x = 16
y = 24
z = 16

#basic If statment, using a variable:
if 	  x > z: print ('x is larger then z!')
elif x == z: print ('x and z have the same value!')
else	   : print ('z is larger then x!')  

#you can use math to make the statments more complicated:
if (x/16) + 5 < (z+y)/x+4 : print ('i guess thats right?')
else			          : print ('thats a big ass x value')

#you can even put if statments into if statments:
if x > 10:
	if y > 10:
		if z > 10:
			print ('all your values are higher then 10')

#Use multiple variables with an AND statment:
if x > 10 and y > 10 and z>10:	
	print ('either all your numbers are over 10 or they are over 50 combined')

#if you add in an 'or' statmentn one of the factors on the left or right have to be true:
if x + y >= 40 or y + z >= 40:
	print('math is fun isnt it?')

#methods sort data on diferent elements:
w = '4'
if w in ['a','b','4','5','s','%',' ']:
	print('the variable is in the list')
	if   w.isalpha():
		print(f'and it is the letter {w}')
	elif w.isdigit():
		print(f'its the number {w}')
	elif w == ' ':
		print(f'please put something in there not a space, its not funny....')
	else:
		print(f'its the symbol {w}')

