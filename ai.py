# 1. Variables

#print("Hello World")  #used quotes hence "hello world" is printed

# (a)Declaring and Using a Variable

#age = 20 #first value of the variable
#age = 30 # second value of the variable
#print(age)  # Value of the age variable(no quotes used, this prevents age from being printed on the terminal but instead the value(20/30) is printed)
#"print(age)" prints the second value of the variable

# (b)Declairing variables and assigning a string value
#price = 19.95 #(can use decimals/whole numbers("int"))
#first_name = "Mosh" #(use an underscore to seperate words/when using multiple words, moreover, makes code be more readable)
#is_online = True #(boolean value, true or false)

# 2. Input
# name = input("What is your name? ")
# print("Hello " + name) # string concatenation

# 3. Type Conversion(Data Types)
#(a) Numbers
#(b)String
#(c)Booleans
#(d)Dictionary(object in js)
#(e)Lists(Array in js)

#birth_year = input("Enter your birth year: ")


# Calculate age 
#age = 2024 - int(2006) #use int() function to convert string to int
#age = 2024 - '2006' #cannot convert string to int, so use int() function
#print(age)

# Functions to convert variables
# float(): converts a value to a floating point number
# int(): converts a value to an integer
# bool(): converts a value to a boolean value
# str(): converts a value to a string

# 10 = interger
# 10.1 = float
#True/False = boolean
# '19.1. = string

# (a)Strings
# ( print() and Input() Functions) are general purpose functions

#course = "Python for Beginners"
#course.upper() #converts string to uppercase/returns new string
#print(course.upper()) #prints uppercase string
#print(course.lower()) #prints lowercase string
#print(course.find("P")) #prints index of the first occurrence of the substring
#print(course.replace("for","4")) #replaces substring with another string
#print('Python' in course) #checks if substring is present in the string
#print(course) #prints original string

# Arthimetic Operators
#print(10 + 3) #addition
#print(10 - 3) #subtraction
#print(10 * 3) #multiplication
#print(10 / 3) #division : floating point number
#print(10 // 3) #integer division : whole num...(integer)
#print(10 % 3) #modulus : remainder of division
#print(10 ** 3) #exponentiation : power of...


# used more lines of code
#x = 10
#x = x + 3
#print (x)

#Augmented assignment operator

 # used fewer lines of code
#x +=3
#print(x)

#Operator Precedence(order of operator application)

#x = 10 + 3 * 2 #('BODMAS' rule applied)
#print(x) #prints 16

#x = (10 + 3) * 2 #parentheses applied first
#print(x) #prints 26

#Comparisson Operators
 # compares values at some point

#x = 3 > 2 #greater than(boolean value gives boolean results/expressions)
#print(x)

#Logical Operators
  # Builds complex rules and conditions

#price = 50
#print(price > 25 and price < 25)

# and(both)
# or (at least one)
# not (opposite)

# if statements (make decisions in programming)

#temperature = 37
#if temperature > 30:
    #print("It's a hot day") #prints if the condition is true
    #print("Drink plenty of water") #prints regardless of the condition

##else:
   # print("It's not a hot day") #prints if the condition is false

#elif temperature > 20: #else if [20, 30]
   # print("It's a nice day")
#print("Okr") #prints regardless of the condition (not part of the "if statement" due to the lack of indentation)

# While Loops 
 # bad approach
  #print(1)
  #print(2)
  #print(3)

#(repeat a block of code multiple of times)
 # less tiresome approach
#i = 1
#while i <= 1_000: # used an underscore to make my code more readable but it is not important
   # print(i) #block of code to be repeated
    #i = i + 1 #incrementing the value of i by 1

# Lists
#names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
#print (names) #prints the entire list
#print(names[0]) #prints the first element of the list(index starts from 0)
#print(names[-1]) #prints the last element of the list
#names[0] = "Jon" #updates the first element of the list
#print(names) #prints the updated list
#print(names[0:3]) #prints the elements from index 0 to 2 (exclusive)

# List Methods

#numbers = [1, 2, 3, 4, 5]
#numbers.append(6) #adds an element to the end of the list
#numbers.insert(0, -1) #inserts an element at a specific index(pass any type of objects)
#numbers.remove(3) #removes an element from the list
#numbers.clear() #removes all elements from the list
#print(1 in numbers) #checks if an element is present in the list(print operator)
#print(len(numbers)) #prints the length of the list
#print(numbers) #prints the original list

#For Loops (iterate over a sequence of elements)
 #shorter implementation
#numbers = [1, 2, 3, 4, 5]
#for item in numbers: #for each item in the list
    #print(item) #prints each item in the list

    #more implementation is required
#i = 0
#while i < len(numbers): #while loop
   # print(numbers[i]) #prints each element in the list
    #i = i + 1 #incrementing the value of i by 1

# Range Functions
#numbers = range(5,10,2) #range function generates a sequence of numbers
#print(numbers) #prints the range object (not a list)
#for number in range(5): #for each number in the range
    #print(number) #prints each number in the range

#Tuples(like lists that store objects but are immutable)
#numbers = (1, 2, 3) #tuples are immutable, [] defines lists while () define tuples
    #numbers [0] = 10 #cannot modify a tuple
#numbers.count(1) #counts the number of occurrences of an element
#print(numbers) # prints the original tuple
#print(numbers.index(1)) #prints the index of the first occurrence of the element






























