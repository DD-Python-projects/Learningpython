
myList = 1,1,1

def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result
 
float(multiplyList(myList)) 

def dividelist(myList):

	#divide all elements with eachother:
	result = 1
	for x in myList:
		result = result / x
	return result

float(dividelist(myList))


def math(operator, *second, first_number):
	sum_second  		= sum(second)
	multiplied_list 	= multiplyList(second)
	divided_list		= dividelist(second)

	if operator == 'add':
		adding_result = first_number + sum_second
		print(int(adding_result))
	
	elif operator == 'minus':
		subtract_result = first_number - sum_second
		print(int(subtract_result))

	elif operator == 'multiply':				
		multiply_result = multiplied_list * first_number
		print(int(multiply_result))

	elif operator == 'divide':		
		divide_result = first_number * divided_list
		print((divide_result)) 

	else:print('plz pick a viable operator for math')

#'operator' 'sum = first_number /-*+ middle numbers (can insert at manny as you want)' 
math('add',4,5,6,7,first_number = 1000)			#= 1000 + 4 + 5 + 6 + 7 = 1022
math('minus',4,5,6,7,first_number = 1000)		#= 1000 - 4 - 5 - 6 - 7 = 978
math('multiply',4,5,6,7,first_number = 1000)	#= 1000 * 4 * 5 * 6 * 7 = 840000
math('divide',4,5,6,7,first_number = 1000)		#= 1000 / 4 / 5 / 6 / 7 = 1.19


#had some trouble with the 'divide calculation' 
#reason --> 400 / (7/6/5/4) != 400/7/6/5/4
#in order to make 400/7/6/5/4 using this method:
#400/7/6/5/4 == (400 * (7/6/5/4)



