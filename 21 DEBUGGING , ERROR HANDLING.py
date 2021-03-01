#  DEBUGGING AND ERROR HANDLING
# errors
# syntax errors
# name error when variable is not defined
# type error when mismatch of data types
# index error accessing using invalid index
# value error inappropriate value for an right arguement
# key error when a dict doesnot have a specific key
# attribute error when variable doesnot have a attribute
# Os error
#  we can raise the type of error we want we can decide what error we want them to see
raise ValueError("invalid value")
#ValueError: invalid value
raise NameError('blah')
#NameError: blah
print("hi")
# name error
#colorize('hi','red')
def colorize(text,color):
    if type(text) is not str:
        raise TypeError('text must be string')
    print(f'printed {text} in {color}')
colorize('hi','red')
#printed hi in red
colorize(3,'red')    
#TypeError: text must be string
def colorize(text,color):
    colors=('red','blue','green','purple','orange')
    if type(text) is not str:
       raise TypeError('text must be string')
    if color not in colors:
        raise Exception                 # you can raise value error
    print(f'printed {text} in {color}')
colorize('hello','blue')
colorize('hey','yellow')
#Exception
def colorize(text, color):
	colors = ("cyan", "yellow", "blue", "green", "magenta")
	if type(text) is not str:
		raise TypeError("text must be instance of str")
	if color not in colors:
		raise ValueError("color is invalid color")
	print(f"Printed {text} in {color}")

colorize([], 'cyan')
#TypeError: text must be instance of str
# colorize(34, "red")

###################### try and excepts error handling
foobar
# name errror
try:
    foobar
except:
    print('problem')#problem
print("after try")#after try


# you can use if there is any type of error
try:
    colt
except NameError:
    print('boom')
    #boom
#######    
d={'name':'colt'}
d['city']
get(d,'city')
def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
d={'name':'colt'}
print(get(d,'name'))
#colt
print(get(d,'city'))
#None
d['city']
# try:
# except:
# else:
# finally:


while True:
	try:
		num = int(input("please enter a number: "))
	except ValueError:
		print("That's not a number!")
	else:
		print("Good job, you entered a number!")
		break
	finally:
		print("RUNS NO MATTER WHAT!")
print("REST OF GAME LOGIC RUNS!")
#please enter a number: 4
#Good job, you entered a number!
#RUNS NO MATTER WHAT!
#REST OF GAME LOGIC RUNS!



# try:
# 	num = int(input("please enter a number: "))
# except:
# 	print("That's not a number!")
# else:
# 	print("I'M IN THE ELSE!")
# finally:
# 	print("RUNS NO MATTER WHAT!")

# def divide(a,b):
# 	try:
# 		result = a/b
# 	except ZeroDivisionError:
# 		print("don't divide by zero please!")
# 	except TypeError as err:
# 		print("a and b must be ints or floats")
# 		print(err)
# 	else:
# 		print(f"{a} divided by {b} is {result}")

def divide(a,b):
	try:
		result = a/b
	except (ZeroDivisionError, TypeError) as err:
		print("Something went wrong!")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")



# print(divide(1,2))
print(divide(1,'a'))
#Something went wrong!
#unsupported operand type(s) for /: 'int' and 'str'
#None
print(divide(1,0))
#Something went wrong!
#division by zero
#None
print(divide('a','b'))
#Something went wrong!
#unsupported operand type(s) for /: 'str' and 'str'
#None
def divide(a,b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total
divide(1,0)
#'Please do not divide by zero'
divide(1,'a')
#'Please provide two integers or floats'
######################################  DEBUGGING  #######################################
# FIRST EXAMPLE:
import pdb              #
first = "First"
second = "Second"
pdb.set_trace()       # we define first and second then stop so it wont identify third
result = first + second     # first will return 'First' same with second but not third 
third = "Third"             
result += third
print(result)


# Be careful with variable names!
def add_numbers(a, b, c, d):
    import pdb; pdb.set_trace() # to set breakpoint we use this

    return a + b + c + d
add_numbers(1,2,3,4)
#pdb a will retuen all abcd with values
#d newest frame
#b
#c quits as these are commmands so dont use keyword and use p first
#p c
#p a

# ===================
# NOTES  NOTES  NOTES
# ===================
# import pdb
# pdb.set_trace()

# Also commonly on one line:
# import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list)           like a map it will show arrow of what is next
# n (next line)
# p (print)
# c (continue - finishes debugging) we will get out of pdb same like q 





