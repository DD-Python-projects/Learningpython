#part 1 1-64, basic math, elements and F strings.
print('https://www.youtube.com/watch?v=mDKM-JtUhhc&t=10382s')
#an overvieuw of the first learned material:
print('hello world!')
print(6+5); print(6*5); print(6/5); print (6-5)

#you can change a variable, python works from top to bottom, 
#so the same code can lead to diferent results.
adding = (6+5)
print(adding + 6) #result = 17
adding = (50+6)
print(adding + 6) #result = 56

# print("+=,-=,/=,*="). Diferent shorthands to do math and change value:
a = 10 ; a+=5 ; print(a) # a = 15
b = 10 ; b-=5 ; print(b) # b = 5
c = 10 ; c/=5 ; print(c) # c = 2
d = 10 ; d*=5 ; print(d) # d = 50

#you can even use math logic with strings:
print('Hello ' + 'World!')
print('test ' *5)

#examples of elements:
print(len('this is a text')) #len: counts objects between '' with spaces.
print(abs(50)) 				 #abs: only 1 value: abs(50,3) leads to error.
print(max(8,4,3,2))          #max: prints the highest value.
print(min(5,3,9,7))			 #min: prints the lowest vallue.
print(max('joe','max'))	     #> works aplabeticly with strings.

#examples of methods: can be added to the print or the argument itself.

argument1 = 'hello im upper!'.upper(); print(argument1.upper())
#.upper added to make text uppercase.
argument2 = 'i hate icecream'.replace('hate', 'love'); print(argument2)
#.replace the first value to the 2nd value. 
print(type(argument2))
#type can be used to find out the type of a line of code.
print('adding an enter in a sentence is done with\nor\rusing python')

#F-strings allow variables to be added into strings:
name = 'Dirk'
age = 27
greetings = f'hello {name}, you are {age} years old!'
print(greetings)

#Combining the logic:

name, age, hobies = 'Dirk Driessen',27, 'music and coding'
age_mom, age_dad = 59, 64

introduction = f'hello, my name is {name}. i am {age} years old,\
\nand i love {hobies}. In 5 years I will be {age+5} years old.\n\
So far i have hated my time with python and i hope i can quit soon. \n\
I have two parents, my mom is {age_mom} years old, and my dad is {age_dad} years old.'\
.replace('hated','loved') \
.replace ('quit','learn more')

basic_math =f'putting this all together, my mom was {age_mom - age} years old \
and and my dad was {age_dad - age} years old when i was born.'

statment =f'^the previous introduction was exactly {len(introduction) + len(basic_math)} words long^' .upper()

print(introduction, basic_math, statment)
