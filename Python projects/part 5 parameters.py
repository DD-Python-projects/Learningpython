#function: a block of code that can be re-used.
def test_function():
	print(5+4)

#calling a function: runs the function defined as: test_function.
test_function()


def calculator(num1, num2): #parameters are viarables that only work in the function.
	result = num1 + num2
	print(result)

calculator(7,9) 	#num1 = 7 and num2 = 9: prints = 16
calculator(15,19) 	#num1 = 15 and num2 = 19: prints = 34

#exersise: make a calculator that can subtract AND add. (my attempt)
def better_calculator(num1, num2, operation):
	if 	operation == 'plus':
		result = num1 + num2
	elif operation == 'minus':
		 result = num1 - num2	
	print(result)

better_calculator(9,6,'plus')	

#result lesson:
def lesson_calculator(num1, num2, operation):
	if 	operation == 'plus':
		result = num1 + num2
		print(f'{num1} + {num2} = {result}')
	elif operation == 'minus':
		 result = num1 - num2
		 print(f'{num1} - {num2} = {result}')	
	
lesson_calculator(4,5,'minus')

#keyword arguments:
def test_test (arg1 = 1, arg2 = 1, arg3 = 1, arg4 = 1): 
	#default arguments: if you dont give a value to one of the arguments it defaults to 1
	print((arg1 + arg2)/(arg3+arg4)) 
test_test(arg1 = 1,arg2 = 2,arg3 =3) #no value given for arg4, so its set to 1.

#exersise:
def greet_function(person = 'insert name of person', greet = 'general kind greeting', weekday = 'sadly not sunday'):
		print(f'{greet} {person}, have a nice {weekday}')

greet_function(greet ='hello',weekday = 'sunday')	#I printed a function giving a new variable to greet and weekday while using the default argument for person.
		#'hello insert name of person, have a nice sunday'

#what if you dont know the number of arguments?: #list unpacking
def print_all(first,*arguments,extra): 
		print(first)
		print(arguments)
		print(extra)

def print_dict(*tuple1, **dict1):
	print(tuple1)
	print(dict1)
		
print_all(9,1,2,3,4,5,6,7,8,extra = 12) #python = prints 9 and 12 as keyword arguments while keeping the rest in a list.

print_dict(1,2,3)


#exersise: create a calc function that prints the sum of an unlimited string of numbers
def print_powerfull_calc(*arguments):
	result = sum(arguments)
	print(result)

print_powerfull_calc(4,3,2,1,4,5,6,87,9,6,5,4,3,3,23,5324,453,6,3)

#function to multiply values in a list: stolen straight from the internet:
myList = 1,2,3

def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result
 
multiplyList(myList) #seems to work fine, printed 1,2,3.

#combination exersise: self made exersise: make a working calculator that can do single math operations:
def the_most_powerfull_calc(first,*arguments,last):
	sum_arguments  		= sum(arguments)
	list_arguments 		= print(list(arguments))
	multiplied_list 	= multiplyList(arguments)


	if first == '+':
		result_sum = sum_arguments + last
		print(f' the calculator did the folowing math for you: {arguments} + {last} = {result_sum}') #works with basic stuff from course.

	elif first == '-':
		result_minus = last - sum_arguments
		print(f'the calculator did the folowing math for you: {last} - {sum_arguments} = {result_minus}') #works with basic stuff from course.

	elif first == '/':
		result_div = last / divided_list
		print(f'the calculator did the folowing math for you: {last} / {divided_list} = {result_div}') #this part doenst work yet.

	elif first == '*':
		result_multi = last * multiplied_list
		print(f'the calculator did the folowing math for you: {last} * {multiplied_list} = {result_multi}') #works thanks to dif: multiply list i found online.


the_most_powerfull_calc('*',5,6,7,8, last = 80)

#calc can only multiply single numbers, it cant do: 80 * 4 * 5 yet, for example. Right now it does: 80*(4+5).
#it needs some function that multiplies/divides all data in a tuple (or most likely a list if you convert its type)

#on the internet i found:
	#def multiplyList(myList):
 
    # Multiply elements one by one
    #result = 1
    #for x in myList:
        #result = result * x
    #return result

#final result before moving on: i managed to make a calculator that can add, subtract and multiply. It cant divide yet.
#i tried changing the multiply function to divide instead, but that resulted in incorect calculations.
#i found methods to divide all data in a list by the same number. For list data with eachother (the thing i need) it recomended a 'numpy' function. Maybe this shows up later.  
#Ill probably come back to this one after learning more information from the course.
