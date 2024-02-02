#dictonaries: use a 'key' + 'list' that contain variables
test_dict = {'A':123, 'B':[4,5,6]}
print(test_dict.items())
print(len(test_dict))

#converting a dictionary:
print(tuple(test_dict))
print(list(test_dict))

#indexing using dictonaries:
print(test_dict['A'])		#mistake leads to an error
print(test_dict.get('A'))	#mistake leads to 'none'

#exersise: update the dictonary: add another key + data point to 'test_dict'
test_dict = {'A':123, 'B':[4,5,6]}
extra_test_dict = {'C':[7,8,9]}			#method 1: {'key':[data]}
test_dict.update(D = [10,11,12])		#method 2: .update(key = [data])
extra_test_dict['E'] = 130,131			#method 3: ['key'] = data
test_dict.update(extra_test_dict)
print(test_dict)

#sets: every single datapoint in the set has to be unique. Used to compare 2 datasets.
my_set ={1,2,3,4,4,3,2,1}
print(my_set)		#prints = {1,2,3,4}, doesnt print repeated elements.

#using methods: (python set methods)
# my_set.add(5)
# my_set.remove(3)
# print(my_set)		#prints {1,2,4,5}

# intexing and slicing does NOT work on sets. 
print(my_set.pop())
print(my_set)
# what you can do is remove a datapoint with .pop
#exersise: use type conversion to take a specific point from a set:
print(type(my_set))		#print: my_set
my_list = list(my_set)	#turns data type into a list
print(my_list[2])		#takes index 2 (so the number 4) from the list
#^can also be typed as: print(list(my_set))^

#comparison of datasets
set1 = {34,24,67,43,21}
set2 = {34,67,23,79,41,37,21}
set3 = {32,460}

print(set1.union(set2))			#combines all of the values.

print(set1.intersection(set2))	#gives us all the values in both datasets
								#set1 & set2
print(set1.difference(set2))	#gives datapoints in set1 that are not in set 2
								#set1 - set2

#exersise: find out if this list has duplicates:
test_list_exersise = [48, 52, 38, 85, 19, 38, 10, 9, 79, 9, 70, 28, 53, 44, 68, 24, 45, 7, 92, 79, 42, 99, 29, 60, 62, 95, 70, 88, 85, 10, 71, 10, 55, 75, 86, 70, 73, 86, 84, 77, 74, 14, 28, 17, 69, 56, 20, 65, 8 ,62 ,62 ,16 ,52 ,19 ,43 ,82 ,7 ,67, 33, 32, 98, 71, 91, 98, 89, 68, 82, 18, 5, 12, 85, 5, 55, 88, 43, 97, 25, 89, 63, 49, 41, 81, 74, 60, 48, 92, 45, 76, 21, 34, 66, 100, 5, 3, 59, 73, 55, 13, 51, 63]
print(len(test_list_exersise))  			#list contains 100 numbers.
set_list_exersise = set(test_list_exersise)  
print(len(set_list_exersise))				#set contains 66 values so 33 duplicates.


#Booleans: compare 2 values: results either in 'false' or 'true'
list_of_oparators = ['== means equals to', '!= means is not equal to' , '<, <= means smaller then/equal than']
print(list_of_oparators)
print(1 == 1) #true if equal
print(1 != 1) #true if not equal
print(10 > 1) #true if 10 is larger then 1

#booleans in lists: 'not' reverses the result of booleans
print(48 in (test_list_exersise))
print(4 not in (test_list_exersise))

#exersise: check if key 1 exists in the dict. and if value 'four' does':
e_dict = {1:'one',2:'two',3:'three'}
print(1 in (list(e_dict)))				# 1 is present in the dicto x = [1,2,3,5,3,2]
print('four'in e_dict.values())			#.values targets values instead of keys.

#the bool() function: truthy and falsy.
print(bool(1)) # any kind of value gives = true. No vallue = False.




