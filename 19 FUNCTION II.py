# FUNCTIONS PART11
###############################     *args gather all remaining arguement as tuple
def sum_all_nums(*nums):
	total = 0
	for num in nums:
		total += num
	return total
def sum(num1,*args):  # first num1 will be printed and looping through the rest	
print(sum_all_nums(4,6,9,4,10))
print(sum_all_nums(4,6))
#####################################
def ensure_correct_info(*args):
	if "Colt" in args and "Steele" in args:
		return "Welcome back Colt!"
	return "Note sure who you are"

print(ensure_correct_info("hello", False, 78)) # Not sure who you are...

print(ensure_correct_info(1, True, "Steele", "Colt"))

########################################
def feed_me(*stuff):
	for thing in stuff:
		print(f"YUMMY I EAT {thing}")
feed_me("apple", "tire", "shoe", "salmon")
################################################  keyword args gather remaining keyword arguement and stores them in dictionary
def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"

    return "Not sure who this is..."

# print(special_greeting(David='Hello')) # Hello David!
# print(special_greeting(Bob='hello')) # Not sure who this is...
# print(special_greeting(David='special')) # You get a special greeting David!

print(special_greeting(Heather="hello", David="special"))  # you get a special greeting 
###############################################################
def fav_colors(**kwargs):
    # print(kwargs)# prints dictionary
	for person,color in kwargs.items():
		print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby="red", ethel="teal")
fav_colors(colt="purple", ruby="red", ethel="teal", ted="blue")
fav_colors(colt="royal deep amazing purple")
##################################################################
def display_info(a, b, *args, instructor="Colt", **kwargs):
  # return [a, b, args, instructor, kwargs]
  print(type(args))# tuple

print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))
# parameter orrdering
#1 parameter
#2 *args
#3 default parameters
#4 **kwargs
# a - 1
# b - 2
# args (3,)  a tuple
# instructor - "Colt"
# kwargs - {'last_name': "Steele", "job": "Instructor"}

[1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]

#################################  unpacking of tuples
def sum_all_values(*args):
	print(args)  #if nums ([1,2,3,4,5,6],)
	total = 0
	for num in args:
		total += num
	print(total)

# sum_all_values(1,30,2,5,6)

nums = [1,2,3,4,5,6]
sum_all_values(*nums) #nums will give error


#######################################################
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

display_names(names) # nope..   # single * unpacks dictionary
display_names(**names)  # yup!  unpack dict in separate keyword arguements

def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)# empty if nothing specified after abc

data = dict(a=1,b=2,c=3,d=55,name="Tony")# d and name will  be in the kwargs dictionary

add_and_multiply_numbers(**data,cat='blue') # 7# cat is also in kwargs this is dictionary unpacking
###################################EXCERCISE#####################################
def contains_purple(*args):
    if "purple" in args: return True
    return False
contains_purple(1,2,'purple') # true

#############
#I check if kwargs contains "prefix".
#If it does, I return the value of prefix + the word
#Otherwise, I check to see if "suffix" was provided as a kwarg
#If it was, I return the word followed by the value of suffix
#Otherwise, I just return the word on its own.
def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word
details=dict(word='devesh',prefix='mr',suffix='prasad')
combine_words(**details)
####################################
#Here's what you were given:

def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
#First, call count_sevens  with the numbers: 1,4, and 7  (review)

result1 = count_sevens(1,4,7)
result1  #  1 because only one 7 among the three
#Next, call count_sevens  with all the values from the nums  list, unpacked:

result2 = count_sevens(*nums)
#Adding that little *  makes a huge difference! Instead of passing in a single item (the list), we're now passing in 121 separate arguments.

######################################
#This solution uses dict.get() a lot. dict.get('first')  will return the value of 'first' if it exists, otherwise it returns None.  However, you can specify a second argument which will replace None as the default value. I use that in this solution a bunch of times.

#I defined a dictionary called operation_lookup  that maps a string like "add" to an actual mathematical operation involving the values of 'first' and 'second'
#I create a boolean variable called is_float, which is True if kwargs contains 'make_float', otherwise it's false
#Then I lookup the correct value from the operation_lookup dict using the operation that was specified in kwargs
#Basically, turning something like "subtract" into:kwargs.get('first', 0) - kwargs.get('second', 0) 
#Which in turns simplifies to a number
#I store the result in a variable called operation_value 
#I return a string containing either the specified message or the default 'The result is' string.  
#Whether operation_value  is interpolated as a float or int is determined by the is_float  variable.
#ote: this solution will divide by zero if a 2nd argument isn't provided for divide.  You may want to change the default value to 1.  We learn how to handle ZeroDivisionErrors later on in the course.  Thanks, Scott for pointing out the issue!
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final

calculate()





















