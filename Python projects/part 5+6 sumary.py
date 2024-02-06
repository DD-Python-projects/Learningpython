#sumary of part 5 & 6: going over functions in python:

#step 1: whats a function? A function is a block of individual code you can call back to.
#example:
def test_function():
	print(9+9)

#usually these are placed at the top of a document.
#these can then be called back to using function() comand:
test_function() #this prints the result of test_function = 18

#you can introduce parameters between the brackets: ().
#these parameters are unique to a function, so they dont affect anything outside of it.

''''#######################################################################'''
#example: create a function for a calculator that can add and subtract:
def calculator (num1, num2, operation):
	if operation == '+':
		result = num1 + num2
	elif operation == '-':
		result = num1 - num2
	print(result)		
#at this point the function has been made, 
#but it has to be called to do something:
calculator(4,5,'+')
calculator(6,4,'-')
calculator(4,9,'-')

''''#########################################################################'''

#keyword arguments: #default values: the code picks this data if none is given.
def test_function_2 (arg1 = 2, arg2 = 1, arg3 = 4, arg4 = 6): 
	print(f'arg1 = {arg1}, arg2 = {arg2}, arg3 = {arg3} arg4 = {arg4}')
	Sum_arguments = arg1 + arg2 + arg3 + arg4
	print(f'the sum of all the arguments totals to {Sum_arguments}')

test_function_2() 			#only keyword arguments given.
test_function_2(2,7,6) 		#arg1/2/3 all get another value, arg4 defaults to keyword.

'''############################################################################'''

#above method only allows exactly 4 datapoints, 
#what about big lists with a ton of numbers?
#you can include a tuple with the * marker: targets data thats not asigned to keyword.

def function_3(first,*arguments,big_number): 
	argument_sum = sum(arguments)
	result = big_number / argument_sum
	if result > first:
		print ('its bigger then 1')

function_3(1,2,5,2,3,4,5,8,8,9,3,4,8,4,65,8,6,8,5,654,6,5,56,1,35,big_number = 1563)

'''############################################################################'''
multiplier 	   = 5
has_calculated = False

def multiply_calculator(number): #() = the variable you can enter into the function.		
	global has_calculated
	has_calculated = True
	result = number * multiplier
	return result

print(multiply_calculator(10))
print(has_calculated)

'''############################################################################'''
#Lambda: a small anonymous function with only one expression:
test = lambda test: 'i like blue' if test > 6 else 'i like red'
print(test(9))