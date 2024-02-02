#python uses lists and tuples (tuples = lists that can not be edited)
test_list  = [1,2,3,4,5,6,7,8,9,10]
test_tuple = ['one','two','three','four','five']

#obtaining data from lists: Slicing.
print(test_list [3]) 	  #take index 3 from 'test list': 4.
print(test_list [0:3]) 	  #print index 0,1,2 -> python takes UP TO index 3.
print(test_list [7:0:-1]) #print index 7 to 0 in reverse order (-).
print(test_list [0:7:2])  #print index 0 to 7: every 2nd number.
print(test_list [9:0:-3]) #you can combine reverse + every x-number.

#Exersise: list in a list: print 'test_list'
test_list2 = [1,2,[4,2,[test_list]]]
target = test_list2[2][2][0]
print(target) #prints the nubers of the test_list.

#multiple variables in one:
points, deck_size, graveyard = 8000, 40, 0
print(points, deck_size) #result= 8000 40
#you can then change multiple variables with one command:
deck_size, graveyard = 36, 4
print(points, deck_size) #result= 8000 36

#data types: turning lists/tuples into strings (and the other way around).
test_string = 'sometimes i feel like i dont have a partner'
test_list3	= [1,4,5,7,3,2,6,5]
print((test_string.split('i'))) 			#removes the letter 'i' from the text. 
print(list(test_string))					#prints the test string as a list.
print((test_string).replace('i','u'))		#replace: replaces the letter i in the string with the letter u.
weird_string = test_string.strip('some')	#strips a string from a specific vallue (only works on the outside).
print(weird_string)

#combined exersise:
test_string2, test_string3 = 'green is my favorite colour','blue is my least favorite colour'
string_list = list(test_string2)			#turns string 2 into a list
string_list_part = string_list[3:20:2]		#takes data from the new list.
print(string_list_part[2])					#prints data from the new list.



# and turning the list back into a string:
def ilikepizza(string_list):	     #define ilikepizza		
	str1 = ""						 #vallue between outputs
	return (str1.join(string_list))  #explains what ilikepizza does (.join a list)
print(ilikepizza(string_list))