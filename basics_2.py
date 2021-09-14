#strings
#course = "Python's for Beginners"
#course_1 = 'Python for "Beginners"'
#print(course)
#print(course_1)
#course_2 = 'Python for Beginners'
#index      0123456789...
#                      ...-3-2-1
#print(course_1[-3])
#print(course[1:]) #python will assume index 1(in this case, y) as the start index
#print(course[:5]) #python will assume index 5(in this case, n) as the last 
#print(course[2:-2])

#Formatted Strings
#first = 'John'
#last  = 'Smith'
#message = first +' [' + last + '] is a coder'
#print(message)
#msg = f'{first} [{last}] is a coder'
#print(msg)

#first_name = 'Charming'
#last_name  = 'Princewill'
#sentence = f'My name is {first_name} {last_name}'
#print(sentence)

#String methods
course = 'Python for Beginners'
len(course) # This is to calculate the number of characters in a variable, its used
#also to caluclate the number of items in a list and etc
print(len(course))
print(course.upper()) # For converting all the characters to upper case
print(course.lower()) # For converting all the characters to lower case
print(course)

course.find('P')
print(course.find('P')) # This function will return 0 because the character 'P'in in index 0.
# You can use same function to find out the indices of each of the characters in a string
print(course.find('Beginners')) # This will return 11 because the word begins with B and B
# is index 11
course.replace('Beginners', 'Absolute Beginners')
print(course.replace('Beginners', 'Absolute Beginners')) # This function is to replace Beginners
# with Absolute Beginners. You can do same with single characters
print(course.replace('P', 'T')) # function to replace P with T. Its case sensitive
'Python' in course
print('Python' in course) # This is a funtion to check if a particular character or sequence
# of characters is in a string. It returns TRUE or FALSE
print(f"")
Running for president of the UNITED STATES BARACK MR PRESIDENT OBAMA

Hillary Clinton almost became the first president of the United States
But Trump didnt let her win the election
