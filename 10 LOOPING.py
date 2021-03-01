# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:41:39 2020

@author: Devesh Prasad
"""

nums=range(1,10,2)
nums
print(nums)# you will get range so use lis
list(nums)
print(list(nums))
#[1, 3, 5, 7, 9]

times = input("How many times do I have to tell you? ")
times = int(times)

# Simplest Version
for time in range(times):
	print("CLEAN UP YOUR ROOM")

# Version 2
for time in range(times):
	print(f"time {time+1}:CLEAN UP YOUR ROOM")
    #5
#time 1:CLEAN UP YOUR ROOM
#time 2:CLEAN UP YOUR ROOM
#time 3:CLEAN UP YOUR ROOM
#time 4:CLEAN UP YOUR ROOM
#time 5:CLEAN UP YOUR ROOM   
    
    
# Main Solution
for num in range(1,21):
	if num == 4 or num == 13:
		print(f"{num} is unlucky")
	elif num % 2 == 0:
		print(f"{num} is even")
	else:
		print(f"{num} is odd")

	
# Slight Refactor
for num in range(1,21):
	if num == 4 or num == 13:
		state = "unlucky"
	elif num % 2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{num} is {state}")

#1 is odd
#2 is even
#3 is odd
#4 is unlucky
#5 is odd
#6 is even
#7 is odd
#8 is even
#9 is odd
#10 is even
#11 is odd
#12 is even
#13 is unlucky
#14 is even
#15 is odd
#16 is even
#17 is odd
#18 is even
#19 is odd
#20 is even
    
# Continues to ask for user input until the user types 'bananas'
msg = input("whats the secret password?")
while msg != "bananas":
	print("WRONG!")
	msg = input("whats the secret password?")
print("CORRECT!")
#whats the secret password? gululu
#WRONG!
#
#whats the secret password?ffffd
#WRONG!
#
#whats the secret password?fdf
#WRONG!
#
#whats the secret password?gd
#WRONG!
#
#whats the secret password?

# for num in range(1,11):
# 	print(num)

# equivalent of above for loop
num = 1
while num < 11:
	print(num)
	num += 1


# With a for loop
for x in range(3):  # to write it 3 times
	for num in range(1,11): 
		print("\U0001f600" * num)

# With a while loop
times = 1
while times < 11:
	print("\U0001f600" * times)
	times += 1
#😀
#😀😀
#😀😀😀
#😀😀😀😀
#😀😀😀😀😀
#😀😀😀😀😀😀
#😀😀😀😀😀😀😀
#😀😀😀😀😀😀😀😀
#😀😀😀😀😀😀😀😀😀
#😀😀😀😀😀😀😀😀😀😀



# Without string multiplication - ugly solution
# for num in range(1,11): 
# 	count = 1
# 	smileys = ""
# 	while count <= num:
# 		smileys += "\U0001f600"
# 		count += 1
# 	print(smileys)


msg = input("Say Something: ")


while msg != "stop copying me":
	print(msg)
	msg = input()
print("UGH FINE YOU WIN, BROTHER!")

# while msg != "stop copying me":
# 	msg = input(f"{msg}\n")
# print("UGH FINE YOU WIN, BROTHER!")


# while True:
#     command = input("Type 'exit' to exit: ")
#     if (command == "exit"):
#         break

# for x in range(1, 101):
#     print(x)
#     if x == 3:
#         break

times = int(input("How many times do I have to tell you? "))

for time in range(times):
	print("CLEAN UP YOUR ROOM!")
	if time >= 3: 
		print("do you even listen anymore?")
		break
		