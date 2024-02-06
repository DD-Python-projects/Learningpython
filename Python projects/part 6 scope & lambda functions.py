#goal of scope/return: making use of an existing variable without editing it for the rest of the code.

#the rules of scope: 
#every function has its own scope:
x = 60
y = 30

def test():
	#x += 4     	#this doesnt work, you cant edit a variable thats outside of the scope
	x = 5			#this does work! The x varable is now 5 in the scope of test().	
	x_sum = x + 5	#Creates x + 5, cuz x is defined in def test, it gives 10, if it was not it would give 65.
	print(x_sum)	

def test2(y):
	y += 15
	#print(y)
	return y

print(test2(y))	#returns 45 after 15 was added to variable 'y'. 
print(y)		#returns 30 cuz 15 was only added in the scope of def: test2
test()			#when outside of the def test, it doesnt see the variable anymore

#exersise: 
multiplier 	   = 5
has_calculated = False
#my attempt:
def multiply_calculator(multiplier,has_calculated):
	x = 15
	result = x * multiplier
	has_calculated = True
	return result

print(multiply_calculator(multiplier,has_calculated))

#solution course:
def multiply_calculator(number):		
	global has_calculated
	has_calculated = True
	result = number * multiplier
	return result

print(multiply_calculator(10))

#both solutions give the same result but the course one is better.
#reason: the variable you can edit in your print statment.
#using the method from the course: you can edit the variable specific to the function.
#you want to create a function in a way where its made towards ease of access with the data you have.

#lambda functions:
Q = lambda x: x + 1
print(Q(10))

basic_calc = lambda a,b: a + b 
print(basic_calc(2,3))

#exersise: - takes 1 int argument, if int > 5 say 'hello' else? say bye.

q = lambda q: 'hello' if q > 5 else 'bye'
print(q(3))


#explain all your functions to keep your sanity in tact :)
''''simple text'''
test(62,63)
print(test.__doc__)