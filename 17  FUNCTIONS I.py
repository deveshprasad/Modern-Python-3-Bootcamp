# FUNCTIONS PART 1
# use of funnction DRY dont repeat yourself
# common mistakes LINE 86 AND THE OTHER IS UNNECESSARY ELSE
def sing_happy_birthday(name):
	print("Happy Birthday To You")
	print("Happy Birthday To You")
	print(f"Happy Birthday Dear {name} ")
	print("Happy Birthday To You")


sing_happy_birthday()# necesry to calling it otherwise no value
sing_happy_birthday('devesh')     # devesh is arguement  and name is parameter
sing_happy_birthday()
#########################################
def print_square_of_7(): #This function does not return anything
	print(7**2)  # return is missing

print_square_of_7()

def square_of_7(): 
	print("I AM BEFORE THE RETURN!")
	return 7**2
	print("I AM AFTER THE RETURN!")  # the thing which is written after the return 

result = square_of_7()
print(result)
#############################################
from random import random
random()     # this value is between
def flip_coin():
	if random() > 0.5:
		return "HEADS"
	else:
		return "TAILS"

print(flip_coin())
# when method is called arguement is the data you pass in the parameter

#######################################

def square(num):
	return num * num

print(square(4))
print(square(8))
##############################
def divide(num1, num2):  # for two parameters      
	return num1/num2
# whatever comes first is num1  unless specified with arguement
print(divide(2,5))
print(divide(5,2))
################################
#OLD=VERSION===OLD=VERSION===OLD=VERSION
def is_odd_number(num):
    if num % 2 != 0:
        return True
    else:  #This else is unnecessary   
    	return False
#OLD=VERSION===OLD=VERSION===OLD=VERSION


def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False # We can just return without the else

print(is_odd_number(4))
print(is_odd_number(9))
######################################
#OLD-VERSION----OLD-VERSION----OLD-VERSION-----
def sum_odd_numbers(numbers): 
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        return total #Returning too early :(
#OLD-VERSION----OLD-VERSION----OLD-VERSION-----


# NEW AND IMPROVED VERSION :)
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        # RETURN SHOULD NOT  BE WRITTEN IN THIS LINE OTHERWISE CODE WILL END WITHOUT COMPLETE EXECUTION
    return total

print(sum_odd_numbers([1,2,3,4,5,6,7]))

####################################
def add(a,b):
    return a+b

def math(a,b,fn=add): # MATH TAKES 2 NO AND FN=FUNCTION IT TAKES THE CODE TO ADD ABOVE AND EXECUTES ADDITION UNLESS SUBTTRACT IS SPECIFIED
    return fn(a,b)

def subtract(a,b):
    return a-b

print(math(4,5)) #results in add(4,5) which is 9

print(math(4,5,subtract))# ORDER DOES MATTER #results in subtract(4,5) which is -1

######################################
def exponent(num, power=2): # IF YOU DONT  PASS IN POWER DEFAULT POWER=2
	return num ** power

print(exponent(2,3)) #8
print(exponent(3)) #9
print(exponent(7)) #49
############################################
def exponent(num, power=2):
	return num ** power

# Order doesn't matter anymore, if we use key word arguments:
print(exponent(num=2,power=3)) #8
print(exponent(power=3, num=2)) #8

# Without keywords args, order still matters:
print(exponent(3,4)) #81
print(exponent(4,3)) #64

########################################### SCOPE 
# WHEN A VARIABLE IS  DESCRIBED INSIDE A FUNCION IT IIS SCOPED ONLY DEFINED INSIDE THE FUNCTION
INSTRUCTOR="devesh"
def sayhello():
    INSTRUCTOR="PRASAD"
    print(INSTRUCTOR)  # PRASAD
    return f'hello{INSTRUCTOR}'   # HELLOPRASAD IF SPECIFIED INSIDE OTHERWISE GLOBAL ONE WILL BE PRINTED

sayhello()
print(instructor)# NAME ERROR
print(INSTRUCTOR2)# NA
print(INSTRUCTOR)#DEVESH
   
total = 0  # NOT SCOPED not in a function so global
def increment():
	global total #use the global variable total
	total += 1
	return total

print(increment()) # 1
print(increment()) # 2
print(increment(4)) #TypeError: increment() takes 0 positional arguments but 1 was given
#####################################
# EXAMPLE OF A SCOPING PROBLEM:
total = 0

def increment():
	total += 1
	return total

print(increment()) # Error! 
# "I can't find a variable named total in this function"
# NON LOCAL  THIS VARIABLE IS NOT DEFINED IN INNER OR GLOBAL SCOPE BUT IN A PARENT FUNCTION
# FOR EXAMPLE
# DEF OUTER():
#    COUNT=0
#    DEF INNER():
#        NON LOCAL COUNT
#        COUNT+=1
#        RETURN COUNT
#    RETURN INNER
def exponent(num, power=2):
	"""exponent(num, power)raises num to specified power. Power defaults to 2."""
	return num ** power

print(exponent(2,3)) #8
print(exponent(3)) #9 
print(exponent(7)) #49

print(exponent.__doc__)#exponent(num, power)raises num to specified power. Power defaults to 2.
#none if nothing specified in three brackets
print.__doc__
l=[1,2,3,4]
l.pop.__doc__ 

############################################################################
#################SOLUTIONS#################################################
def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None
return_day(5)# THURSDAY
# SAME
def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None
return_day(5)# THURSDAY

##############################
def last_element(l):
    if l:
        return l[-1]
    return None
last_element('abc')# c from abc
#First check to see if the list exists (if it has data in it).  If it does, return the -1 item (last item).  Otherwise, return None.
#########
def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"
number_compare(9,6)
############
def single_letter_count(string,letter):
    return string.lower().count(letter.lower())
single_letter_count('mississipppi','p')# 3
 ###########################
def multiple_letter_count(string):
   return {letter: string.count(letter) for letter in string}
multiple_letter_count('missisiiispi')
#{'m': 1, 'i': 6, 's': 4, 'p': 1}
##################################################
def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection
#list_manipulation(,'remove','end')

#################################
def is_palindrome(string):
    return string == string[::-1]
is_palindrome('devesh') # false
#For the more advanced version that ignores whitespace, I first remove all whitespace from the input string using a string method called replace() . What I'm actually doing is replacing all spaces(" ") with empty strings ("").  I save the result to a new variable I call stripped .  Then, I simply check if stripped is a palindrome, using the same logic I did in the previous solution.

def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]
is_palindrome('devesh prasad') # false
is_palindrome('naman naman')#true
####################
def frequency(collection, searchTerm):
    return collection.count(searchTerm)
frequency([1,2,3,4,4,5],4)#2
#####################################
def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total
multiply_even_numbers([1,2,3,4])#8

#########################
#Slicing the first character (up to index 1) and capitalizing it
#Adding that to the rest of the string (from index 1 onward)
def capitalize(string):
    return string[:1].upper() + string[1:]
capitalize(' dick') # only works for first character it shouldnot be empty space and doesnot work on sentences
capitalize('dickless')
#'Dickless'
##################
#I make a list to store all truthy values
#I iterate over each value in the list
#I check if the value is truthy (using a simple if val ) 
#If the value is truthy, add it to the truthy_vals  list
#return truthy_vals  at the end
def compact(l):
    truthy_vals = []
    for val in l:
        if val: truthy_vals.append(val)
    return truthy_vals
compact([1,2,3])# [1,2,3]
compact(['',(),0])#[]  as these are falsies
####################################
def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common
intersection([1,2,3],[3,4,5])#3
intersection('abcde','bcdew')#bcde
#['b', 'c', 'd', 'e']
# same
def intersection(l1, l2):
    return [val for val in l1 if val in l2]
intersection('abcde','bcdew')#bcde
# sets method
def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]
intersection([1,2,3],[3,4,5])#3

######################################
#I have two lists, to hold the true and false values
#I loop through the list, calling fn  with each value in the list
#If the result is True, I append the value to the trues  list
#Otherwise, I append the value to the falses  list
#At the end I return a list that contains both the trues  and falses  lists
def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]
partition([0,1,2,''],sum)

def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

def partition(l, callback):
    return [[l.pop(l.index(i)) for i in l if callback(i)],l]










