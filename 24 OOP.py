# class and object 
# class contain methods functions and attributes (in a dict )
# instances  are constructed fron a class blue print
help(int)
help(list)
nums=[1,2,3] # you are creating instances of class
#     we can have inheritance
#_underscore_before shows private but no distinction in python
# encapsulation the grouping of private and public att and methods into a programmatic class making abstraction possiblle
# abstraction exposing only relevant data in  a class interface hiding private from users
class User: # use camel case
    pass# fuction created
user1=User()
print(user1)
#<__main__.User object at 0x000002CBBB84B808>
print(type(user1))
#<class '__main__.User'>
# A User class with 3 attributes but no methods (aside from __init__)
class User:
	def __init__(self, first, last, age):
		self.first = first# we dont write name  here so it will have same name in all 3
		self.last = last
		self.age = age

user1 = User("Joe","Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user1.first, user1.last, user1.age)# only user 1  then #<__main__.User object at 0x000002CBBB84B808>
print(user2.first, user2.last, user2.age)
# INSTANTIATING THAT IS INSTANCE OF A CLASS IS CALLED
# SELF IS CURRENT INSTANCE OF THE CLASS  IT IS FIRST PARAMETER 
# _____________   USE OF UNDERSCORE
# _name
# __name
# __name__


class Person:
	# Init is a "dunder" method
    def __init__(self):
        self.name = "Tony"
        # single underscore means "private" (sort of)
        self._secret = "hi!"   # 1 undercore
        # two leading underscores tells Python to "mangle" the name
        self.__msg = "I like turtles!"    # 2 undercore we get error
        self.__lol = "HAHAHAHAH"


p = Person()

print(p.name)
print(p._secret) #Anyone can still directly access the attribute normal with single underscore
print(p.__msg)########## 2 underscore gives error
print(dir(p)) # Notice what __msg and __lol have been "mangled" to

print(p._Person__msg)#I like turtles!
print(p._Person__lol)#HAHAHAHAH

####################################
# A User class with both instance attributes and instance methods
class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def full_name(self):
		return f"{self.first} {self.last}"  # self is required 

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(user1.likes("Ice Cream"))#########self is not required
print(user2.likes("Chips"))

print(user2.initials())
print(user1.initials())

print(user2.is_senior())#true or false
print(user1.age) #Print age before we update it
print(user1.birthday()) #updates age
print(user1.age) #Print new value of age  after birthday now age has changed


##########################
class BankAccount:

    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
user1=BankAccount('DEVESH')
print(user1.balance)
print(user1.deposit(100))
print(user1.balance)
print(user1.withdraw(50))
print(user1.getBalance())
#50

#######################3
# Another class with a class attribute, used for validation purposes
class Pet:
	allowed = ['cat', 'dog', 'fish', 'rat']

	def __init__(self, name, species):
		if species not in Pet.allowed:#cor self.allowed
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	def set_species(self,species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
print(cat.species)
#cat
tig=Pet('Shera',"tiger")
#ValueError: You can't have a tiger pet!
print(dog.species)
########## second part
ballo=set_species("bear",'fff')
#ValueError: You can't have a fff pet!






