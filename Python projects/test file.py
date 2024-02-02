# print("Control B runs the program >:)")
# print('selecting all code and pressing Control + / turns everything into a comment')

# print("+=,-=,/=,*=")

# print("roses are red, violets are blue, some people can eat poo")
# print (123)

# result = 15 + 3
# print(result)

# result2 = result / 3
# print(result2)

# test_69 = result2 * 10 + 9 
# print(test_69)

# result2 *= 2  #python reads top to bottom. 
# #Line 16 changes the vallue of result 2 from this point on, 
# #so it doesnt affect the math on line 13 :o.

# test_69 = result2 * 10 + 9 
# print(test_69)

# sum1 = (10+5)
# sum1 += 20
# print (sum1)

# #len element: (counts the amount of symbols in the box)

# longass = (len('len also counts the spaces!'))
# print(longass)  #  ^    ^      ^   ^

# #abs element only takes 1 argument

# print	(abs(-50))
# #doesnt take ^ or another argunent added with comma


# #max element: takes the highest vallue (highest number or name)
# print (max(70, 54, 46,29))
# print (max('max', "john", "chad", "yoe"))

# #Methods (Upper, turns all text into uppercase):
# Method1 = 'this is a method'.upper()
# print(Method1)
# #or:
# Method2 = 'so is this one'
# print(Method2.upper())

# exercise_string = 'I Like puppies puppies puppies'.replace('puppies','kittens',2)
# print(exercise_string)

# print(abs(len('a word')*-10))
# #      ^   ^			

# # how to place logical lines in a row or one big one in multiples: 
# print (5+5); print(4+6)
# print (1+2+3+4\
# 		+5+6)

# #int (1, 2, 3,) and float (1.2,1.6,4.7) 
# print(type(1)); print(type(1.1)); print(type('hello'))
# print(int(5.2));print(float(5)); print(1.1 * 3)

# #strings
# variable1 = 'icecream? \n "i love it!"' ;print(variable1)
# print('Hello ' + 'World')
# print('Repeat me ' *10)

# #place values into strings:
# name = 'john'
# age = 26
# greeting_string = 'hi {one}, you are {two} years old'\
# .format(one = name,two = age)
# print(greeting_string)

# #F-string (allows variables to be added into a string):
# greeting_string_better = f'hi {name}, you are {age + 5} years old'
# print(greeting_string_better)

# #exersise:
# exname = 'Dirk'
# exhobby = 'Making Music'
# greeting_string_exersise = f'Hello, my name is {exname}\n and my hobby is {exhobby}'
# print (greeting_string_exersise)

# #tuples and lists: (cant eddit tuples, but you can edit lists)
# my_list = [1,2,3,4,'five','six']
# print (len(my_list))
# print(my_list)
# #editing the list:
# my_list.reverse()
# my_list.append(6)
# print(my_list)

# #tuple
# my_tuple = (1,2,3,4,5,6,7,8,9,10)   #indexing = take the 2nd index from the string
# print(my_tuple[-2]);print(my_tuple[0])

# #exersise list in a list in a list.
# exersise_list = ['first entry',[123,456,[0,'hello :)']], 'bye']
# solution_var = exersise_list[1][2][1]
# print(solution_var)

#picking multiple elements: Slicing
# test_list = [1,2,3,4,5,6,7,8,9,10]
# data_points = test_list[0:4]
# in_line	= test_list[4:10:2]
# reverse_order = test_list[10:4:-1]
# default_slicing = test_list [::2]

# #obtaining specific data:
# print(default_slicing)

# #exersise (list from 8 to 2 only picking every 2nd element)
# exersise_test_list = test_list [7:0:-2]
# print(exersise_test_list)

# a,b,c = 1,2,3
# print(a)

# #exersise:
# value_1 = 10
# value_2 = 'test'
# value_1, Value_2 = value_2, value_1
# print(value_1)

# #turn string into list/tuple
# test_string = 'i like beer'
# test_list2 = [1,2,3,4]
# print(test_string.split('r'))
# print(list(test_string))

# #turn list/tuple into a string: (join)
# print(' and '.join(['one','two','three'])) #this works! cuz its reading a string.
# print(str(test_list)) #join only works in strings not on an int.

# #indexing on strings works the same as on int.
# print(test_string[0:5])

#exersise: #goal:print: 1 2 3 4
test_list = [1,2,3,4]
print(str(test_list).strip('[').strip(']').replace(',',''))

