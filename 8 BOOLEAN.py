#  TRUTHINESS OR FALSINESS 
# 0 IS TAKEN AS FALSY
# 1 AS TRUTHY
# ANT STRING IS TAKEN AS TRUTHY
if 0:
    print("falsiy")
if 1:
    print("truthy")
# truthy   
    # string
animal=input(" enter fav animal :")
if animal:
    print("string are truthy")
 #enter fav animal :fdd
#string are truthy   
 #   
name = "Arya Stark"
if name == "Arya Stark":
    print("Valar Morghulis")
elif name == "Jon Snow":
    print("You know nothing")
else:
    print("Carry on")
    
 #   
data = input("What's your favorite color?")
print("You said " + data)

print("What's your favorite color?")
data = input()
print("You said " + data)


#
color = input("What's your favorite color?")
if color == 'purple':
	print("excellent choice!")
elif color == 'teal':
    print("not bad!")
elif color == 'seafoam':
    print("mediocre")
elif color == 'pure darkness':
    print("I like how you think")
else: 
	print("YOU MONSTER!") 
 
    
    
   #   
animal = input("enter your favorite animal")

if animal:
    print(animal + " is my favorite too!")
else:
	print("YOU DIDNT SAY ANYTHING!")



#
age = input("How old are you: ")
if age:
	age = int(age)
	if age >= 18 and age < 21: 
		print("You can enter, but need a wristband!")
	elif age >= 21:
	    print("You are good to enter and can drink!")
	else: 
		print("You can't come in, little one! :(")
else:
	print("Please enter an age!")



# VERSION 2 with slightly refactored conditional logic
age = input("How old are you: ")
if age:
	age = int(age)
	if age >= 21:
	    print("You are good to enter and can drink!")
	elif age >= 18:
	    print("You can enter, but need a wristband!")
	else: 
		print("You can't come in, little one! :(")
else:
	print("Please enter an age!")
