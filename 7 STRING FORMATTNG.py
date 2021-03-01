#  NEWEST FORMATTING METHOD IS THE NEWEST python 3.6  suitable only
guess=8
print(f"your {guess} is right")
# f is necessary
#your 8 is right
guess="DEVESH"
print(f"your {guess} is right")
#your DEVESH is right
# .FORMATMETHOD  OLDER WAY
formatted="this is {} nice".format(10)
print(formatted)
#this is 10 nice
# oldest way
x=10
format2="my name is %d"%(x)
print(format2)
#my name is 10

print("How many kilometers did you cycle today?")
kms = input() #get user input
miles = float(kms)/1.60934 #convert from string to float and divide
miles = round(miles, 2) #round the result
print(f"Your {kms}km ride was {miles}mi ")  
#Your 234km ride was 145.4mi 
# ROUND SYNTAX:
# round(thing to round, how many decimal points)


