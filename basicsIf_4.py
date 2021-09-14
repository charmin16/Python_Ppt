# If Statements, How to use the "If" condition
# Write a code: If the weather is hot, it should print: Its a hot day, drink plenty of water.

#is_hot = False # First we define a boolean variable
#if is_hot:
 #   print("It's a hot day") #Its indented to show that the code is based on the if statemen
  #  print('Drink plenty of water')
#print('Enjoy your day') # press shift & tab to continue with ur code outside the if conditon
#else:
 #   print('Its an amazingly fantastic day')
  #  print('You guys make sure to enjoy yourselves')

#Exercise: Write a program that displays the following..If its hot, it should return: Its a hot
#day(on one line), next line.. Drink Plenty of water.
#Otherwise if its cold, it shud return: Its a cold day (one line), next line..Wear warm clothes
#Otherwise: it should return: Its a lovely day

#is_hot = True
#is_cold = False

#if is_hot:
    #print("It's a hot day")
   # print('Drink Plenty of water')
#elif is_cold:
    #print("Its a cold day")
    #print('Wear warm clothes')
#else:
    #print("It's a lovely day")
#print('Enjoy Your Day')

#Exercise 2: Imagine the price of a house is $1M. If the buyer has good credit they need
#to put down 10% of the price, Otherwise they need to put down 20% of the total. Write a
#program to display the downpayment

#price_of_house = 1000000
#has_good_credit = True

#if has_good_credit:
   # down_payment = 0.1 * price_of_house
#else:
    #down_payment = 0.2 * price_of_house
#print(f"Down payment : ${down_payment}")
#print(Down_payment)

# Logical operations: These are used to combine more than one condition.
# For example: Write a program for a bank, if an applicant has good credit and high income,
# It should return "Eligible"

#has_high_income = True
#has_high_credit = False

#if has_high_income and has_high_credit:
  #  print('Eligible')
#else:
    #print('iNELLIGIBLE')
#Other logical operations include OR and NOT
# For the earlier program, if an applicant has high income and doesnt have a crimial record
# It should return Eligible

#has_high_income = True
#has_no_criminal_record = False

#if has_high_income and not has_no_criminal_record:
    #print('Eligible')

 # Comparison operations. comparison operations include > < >= <= == !=
   
# Ex 3. If temperature is greater than 30, return: Its a hot day. Otherwise if its less tha
# 10, return: Its a cold day. Otherwise, return: Its neither hot or cold

#temp = 89

#if temp > 30:
 #   print("It's a hot day")
#if temp < 10:
    #print("It's a cold day")
#else:
    #print("It's neither hot or cold")

# Write a program: If name is less than 3 characters long, return: Name must be at least
# 3 characters long. Otherwise if its more than 50 characters long, return: Name can be
# a maximun of 50 characters long. Otherwise return: Name looks good

#name = 'xhbb'

#if len(name) < 3:
    #print('Name must be atleast 3 characters long')
#elif len(name) > 12:
    #print('Name can be a maximum of 12')
#else:
    #print('Name looks good')
# Ex: Take values of length and width of a rectangle from user and check if its a square or not

#length = int(input("What is the length of the rectangle: "))
#breadth = int(input('What is the width of the rectangle: '))
#if length != breadth:
    #print('It is not a square')
#else:
    #print('It is a square')

#length = 100
#width = 30
#if length != width:
    #print('It is not a square')
#else:
   # print('It is a square')

# Ex: Take two integer values from user and print the greater between them

#Number_1 = int(input('Enter the first number(integer): '))
#Number_2 = int(input('Enter the second number(integer): '))
#if Number_1 > Number_2:
    #print(f'The greater number is: {Number_1}')
#elif Number_2 > Number_1:
    #print(f'The greater number is: {Number_2}')
#else:
   # print(f'Both numbers are equal')

#Ex: A company decided to give bonus of 5% to employees if their yr of service is more than
# 5yrs. Ask user for their salary and yrs of service and print the net bonus

#no_of_yrs = int(input('Enter the number of years you have put in: '))
#salary = int(input('Salary: '))
#if no_of_yrs > 5:
    #bonus = 0.05 * salary
    #total = bonus + salary
    #print(f'Your net salary including your bous is: {total}')
#else:
    #print(f'Your salary is: {salary}')

# Ex: A school has the following rules for grading system: below 25 - F, 25-45 -E, 45-50-D
# 50-60 - C, 60-80 -B, above 80 -A. Ask  user to enter marks and print the corresponding grade

#mark = int(input('Enter marks: '))
#if mark < 25:
    #print('F')
    #print('Please put in more effort for next semester')
#elif mark <= 45:
   # print('E')
   # print('You need to step up your performance')
#elif mark <= 50:
   # print('D')
   # print('Pls study harder next time so you can score better')
#elif mark <= 60:
   # print('C')
    #print('Average performance')
#elif mark <= 80:
    #print('B')
   # print('Good one')
#elif mark <= 100:
    #print('A')
    #print('Excellent')
#else: 
    #print('Error')

# Ex: Take input of age of 3 ppl by user and determine oldest and youngest among them
#john = int(input("Enter John's age: "))
#mike = int(input("Enter Mike's age: "))
#pete = int(input("Enter Pete's age:"))
#if john > mike and john > pete:
 #   print('John is the oldest')
#elif mike > john and mike > pete:
 #   print('Mike is the oldest')
#elif pete > mike and pete > john:
 #   print('Pete is the oldest')

# Write a program to print the absolute value of a number entered by the user

#num = int(input('Enter the number: '))
#print(f'The absolute value of the number entered is: {abs(num)}')

# Ex: A student will not be allowed to sit in exam if his/her attendance is less than 75%.
# Take the following inputs from user: Number of classes held, Number of classes attended.
# Print percentage of class attended and determine if student is eligible to sit in the 
# exam or not

#classes_held = int(input('Number of classes held: '))
#classes_attended = int(input('Number of classes attended: '))
#percent_class_attended = (classes_attended/classes_held) * 100
#if percent_class_attended < 75:
    #print('Not allowed to sit in this exam because of poor attendance')
#else:
    #print('Eligible to sit in the exams, your attendance is good')

# Write a program to check if a year is a leap yr or not

#year = int(input('Enter Year: '))
#leap = year/4
#if leap == int:
 #   print('Its a leap year')
#else:
  #  print("It's not a leap year")

## Ex: Write a program to ask a use to enter their age, gender(M or F), marital status( Y or N)
# and then using the following rules print their place of service
# If employee is female, then she will work only in urban areas. If employee is a male btw
# 20 and 40 then he may work anywhere. If employee is male and age btw 40 to 60 then he may
# work in urban area only. And any other input of age should print ERROR

#age = int(input('Enter your age: '))
#gender =(input('Gender: '))
#marital_status = input('Marital status: ')
#if gender == F:
#    print('You will work only in urban areas')
#elif gender == M and age => 20
 #   print('You may work anywhere')

## Ex: A 4 digit number is entered thru keyboard. Write a program to print a new number
# with digits reversed as of original number.

#numb = (input('Input: '))
#print(f'Output: {numb(1:)}')

# Given the 3 sides of a triangle - x,y,z determine whether the triangle is
# equilateral(all three sides are equal), isosceles(any two sides are equal),
# obtuse (all three sides are different)

side_one = int(input('Enter the first side: '))
side_two = int(input('Enter the second side: '))
side_three = int(input('Enter the third side: '))
if side_one == side_two == side_three:
    print('The triangle is an Equilateral Triangle')
elif side_one == side_two or side_one == side_three or side_two == side_three:
    print('The triangle is an Isosceles Triangle')
else:
    print('The triangle is an Obtuse Triangle')








