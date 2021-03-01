#lambda 
def square(num):
    return num*num    # normal 
square2=lambda num:num*num   #lambda
add=lambda a,b:a+b
print(add(3,10))
print(square(6))
print(square2(6))

print(square.__name__)  # square
print(square2.__name__) # lambda
print(add.__name__)     # lambda
# map
# a std func with 2 arguement a function to call and is iterable
nums=[2,4,6,8,10]
doubles=map(lambda x:x*2,nums)

doubles
list(doubles)
# not  a list but  a mapped object
for num in doubles :
    print(num)
#
list(doubles)# empty 
# 

people=['darcy','chris','dev','josie']
peeps=map(lambda name:name.upper(),people)
print(list(peeps))


# from a dictionaey with first and last name to  get the first name
# names  is the list which contains the dictionary
firstname=list(map(lambda x:x['first'],names))


def double(x):
    return x*2
double(3)
doubles=map(double,nums)
list(doubles)
list(doubles)  # empty 

################################# filter
# allows to take a list tuple and acc to condition filters

l=[1,2,3,4]
evens=list(filter(lambda x:x%2==0,l))
print(evens)

names=['austin','arthur','billy','aisha','angel']

anames=filter(lambda n:n[0]=='a',names)
print(list(anames))

# we can use list comprehensions
#############
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))  # utweets return who is truthy that is active  so not 

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))
print(usernames)
# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]


names=['colt','dev','prasad']
filter=list(map(lambda name: f'your instructor is {name}',
         filter(lambda value: len(value)<5,names)))
print(filter)

############### any and all
all([0,''])#false if all are truthy or if empty
all([0,1])# false
all([1,2,3])# truth

all([char for char in 'eio' if char in 'aeiou'])
# true

all([names[0]=="C" for name in names])
# false
[names[0]=="C" for name in names]
# false , false , false
nums=[2,60,26,18]
all([num%2==0 for num in nums])
# true


# any  if any one is truthy tru
any([0,'',[],1])# true for 3 false and 1 true

############################ GENERATOR FUNCTION
import sys
# A simple comparison of size (in Bytes)
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")  # 9024
print(f"Generator Expression: {gen_exp} bytes")  # 120


# SORTED WORKS WITH TUPLE AND LIST
sorted(nums)
# return a copy
nums=[4,6,1,5,23]
nums.sort()
nums
sorted(nums)

#revers
sorted(nums,reverse=True)
# descending order
################## .sort is list specific
# sorted is for both tople

sorted((2,1,3,7,6,5))

###############################################
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#sorted(users,key=len)# ascending order of dictionary  here lambda is usable
# To sort users by their username
sorted(users,key=lambda user: user['username'])

# Finding our most active users...
# Sort users by number of tweets, descending
sorted(users,key=lambda user: len(user["tweets"]), reverse=True)

# ANOTHER EXAMPLE DATA SET==================================
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
sorted(songs, key=lambda s: s['playcount'])
  

###########  sort is a list method it doesnot return copy iterates itself
################ max 
max(3,67,99)
max('c','d','a','A')
# we can pass tuple list dictiomnary

max("hello world")
#w min #e
#####################
names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]
min(names)# gives alphabetical 
# finds the minimum length of a name in names
min(len(name) for name in names) # 3
[len(name) for name in names]
# find the longest name itself
max(names, key=lambda n:len(n)) #Ollivander

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
min(songs, key=lambda s: s['playcount']) #{"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title'] #YMCA



max=0
for song in songs:
    if song['playcount']>max:
        max=song['playcount']
print(max)  


############## reversed  return a reverse iterator

nums.reverse()
nums

reversed(nums)
# gives mapped can be converted to list 
reversed("hello")
for char in reversed("hello"):
    print(char)
'hello'[::-1]
list(reversed('hello'))
''.join(list(reversed('hello')))

for x in reversed(range(10)):
    print(x)
#9,8,7,6,5,4,3,2,1,0

#########################len
    
# len of dict on basis of key value pairs
'hello'. __len__()   # this happeming behind len function
#5
# list can be done like this too 

class SpecialList:
 
    def __init__(self, data):
        self.__data = data
    def __len__(self):  # JUST LOOK AT THIS LINE
        return 50 # no matter what is  the length of data it will return 50 
 
#   def __len__(self):
#        return self.__data.__len__()//2

l1 = SpecialList([1,40,30,100,30,1,2,3,4])
l2 = SpecialList([1,3,4,5]) 

print(len(l1)) #50
print(len(l2)) #50


########### abs
abs(-23)# also float
abs('20')
abs(float('20'))
import math
math.fabs(-4)# converts to float
####################sum
sum([1,2,3])
sum([1,2,3],10)# start at 1,2,3 then add 10 we can do tuples floats set
sum(['hi','there']) # sum cant  sum strings use join
 
###############
round(3.576,1)
# if no value tha round to integers
############################zip
num1=[1,2,3]
num2=[4,5,6]
z=zip(num1,num2)
list(z)
dict(z)# 1:4
# order matters if no equal amount as soon as we reach limited num it will stop 

words=['ji','ki']
list(zip(words,num1,num2))
# we get tuples
list(zip(*z))# * takes tuples oout of list run them individually

fivebytwo=[(0,1),(1,2),(2,3),(3,4)]
list(zip(*fivebytwo))
#[(0,1,2,3),(1,2,3,4)]
##########################
midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']


# returns dict with {student:highest score} USING DICT COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# returns dict with {student:highest score} (same thing as above) USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)
print(final_grades)
# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0]+pair[1])/2),
			zip(midterms, finals)
		)
	)
)
print(avg_grades)





