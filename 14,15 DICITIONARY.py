# DICITIONARY COMPREHENSION WITH SPOTIFY AS EXAMPLE
playlist = {
	'title': 'patagonia bus', 
	'author': 'colt steele', 
	'songs': [
		{'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
		{'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
		{'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
	]
}
for song in playlist['songs']:
    print(song['title'])


total_length = 0
for song in playlist['songs']:
	total_length += song['duration']

print(total_length,"mins")

# DICT HAS KEY VALUE PAIRS 
CART={1:'A',2:'B',3:'C',4:'D',5:'E'}
CART
# ANOTHER WAY
D=dict(key="value")
D
# accessing data 
D['key']
# output is value
d=4
d in CART
# true because d has a vlaue 4 and this value is in the dictionary
# if out of the box then we will get keyerror 
#iteration using loops
for value in CART.values():
    print(value)
for value in CART.keys():
    print(value)
for value in CART.items():
    print(value)
D.values
D.keys
D.items  

for k,v in  CART.items():
    print(f'key is {k} and value is {v}')
    
    
    # METHODS
D.clear()
D2=D.copy()  
D2
D2==D  # true 
D2 is D # false

# from keys
{}.fromkeys('a',[1,2,3,4,5])
# best example
new_user={}.fromkeys(['name','score','email','profile'],'unkknown')
new_user
# if you use existing dict it will create new but not overwrite

newuser={}.fromkeys('string',"devesh")
newuser
# if key is without list symbol than that word will taken and splited

CART.get('nokey')
# none is assigned


D2.pop('key')
#.pop() # error atleast 1 arguement is required
# if something that doesnot exist key error   


# popitem()
 # removes something randomly
 # doesnot takes arguement

# update
 
person={'city':'delhi'}
person.update(CART)

person
#person.update({}) doesnot removes thing but adds

n=dict(a=1,b=2,c=3)
squares={key:value**2 for key,value in n.items()}
squares
{num:num**2 for num in[1,2,3,4,5]}

# looping through two strings
str1="ABC"
str2="123"
combo={str1[i]:str2[i] for i in range(0,len(str1))}
print(combo)

# to make  capital of two dictionaries
dictsample={k.upper():v.upper() for k,v in CART.items()}
dictsample

n=[1,2,3,44,5]
{num:("even" if num%2==0 else "odd") for num in range(100)}
#  to change one key named color to upper case
###############{k.upper() if k is "color" else k for v,k in dict.items}


##########################################################################          EXCERCISE SOLUIONS

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f"{artist['first']} {artist['last']}"
print(full_name)


donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0

for donation in donations.values():
 total_donations += donation
print(total_donations)

# built in function
total_donations = sum(donation for donation in donations.values())

# advanced function
total_donations = sum(donations.values())





# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}
if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")


#
quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")


game_properties = [
    "current_score",
    "high_score",
    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements"
]
initial_game_state = dict.fromkeys(game_properties, 0)
print(initial_game_state )


inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
# Make a copy of inventory and save it to a variable called stock_list
stock_list = inventory.copy()
# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18
stock_list
# remove 'cake' from stock_list
stock_list.pop('cake')


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(0,3)}
print(answer)


#zip
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

dict(zip(list1,list2))  
#  3 methods to do same thing 
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}
print(answer)
answer1 = {k:v for k,v in person}
print(answer1)
answer3 = dict(person)
print(answer3)


answer = {char:0 for char in 'aeiou'} 
answer = dict.fromkeys("aeiou", 0) 
print(answer)
answer = {count: chr(count) for count in range(65,91)} 
print(answer)