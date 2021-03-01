#  LIST ANDD APPLCATIONS
demo_list=[1,"devesh",True,3.5]
print(demo_list)
r=range(10)
k=list(r)
print(k)
str(3)
print(1 in k)  # TRUE
#if 1 in k
for i in k:
    print(i)
# while 
col=["a","b","c","d","e"]
i=0
while i<len(col):
    print(f"{i}:{col[i]}")
    i=i+1
    
# append( item added to end of the list) , insert ,extend
    # append is used only to add 1 item list cannot be added for that insert is used
k.append([11,12])
print(k)    
k.extend([11,12])
print(k)
# insert to insert an item at a given position
k.insert(0,"suc")
print(k)
k.insert(-1,"hey")
print(k)
# not added in last place because the list has a last elemnt alredy it will add in the last index of the prfix list but the new list will have it as second last element
# to solve this use len 
k.insert(len(k),"last")
print(k)

# clear pop and remove
# clear will remove all item 
 # pop will remove last by default guided using index
 # remove  dirctly remove value no index specified
 # index
print(k.index('hey'))
# we can specify start annd end

k.index(5,1)
k.index(5,2)
k.index(8,6,8)# will check from 6-8 if any 8 after this it will give that one

# count
k.count("value")

k.reverse()
print(k)

k.sort()
print(k)

words=['coding','is','fun']
print(','.join(words))

# jon combines copy of original list
# slicing
# x=[1,2,3,4]
#x[-1]=[1,2,3]
#x[1:-1]=[2,3]


# x=[1,2,3,4,5,6]
#x[::2]=[1,3,5]
#x[1::2]=[2,4,6]
#x[1::-1]=[2,1]
#x[:1:-1]=[6,5,4,3]
#x[2::-1]=[3,2,1]


# revers of a string of a list
print(words[0][::-1])

# helllllooo[::3]
#hllo

# swapping
word=["deves",'prsasd']
word[0],word[1]=word[1],word[0]
print(word)

# list comprehension
n=[1,2,3,4,5]
doubled_no=[]
for i in n:
    doubled=i*2
    doubled_no.append(doubled)
print(doubled_no)
# it can be done as 
print([i*2 for i in n])
name="devesh"
[char.upper() for char in name]

# 
friends=["abc","def","pqr"]
print([friend[0].upper() for friend in friends])

[num*10 for num in range(10)]



# to get truthy or falsy all three below aree falsy
[bool(val) for val in [0,[],""]]

# number tto str
p=range(10)
[str(num) for num in p]
[str(num)+"suckit" for num in p]

# adding conditional logic
even=[num for num in p if num%2==0]
print(even)

#
[num*2 if num%2==0 else num/2 for num in p]


#
"......".join(['cool','dude'])

# nested list
l=[[1,2,3],[4,5,6],[7,8,9]]
# accessing
l[0][-1]

# how to use for loop to get every value in a line
for i in l:
    for j in i:
        print(j)
# how print or make a nested listed
L=[[num for num in range(1,4)] for val in range(1,4)]     
print(L)      
        
D=[['X' if num%2!=0 else"O" for num in range(1,4)] for val in range(1,4)]     
print(D)        
       
print([['*'] for i in range(1,4)]) 
        
        
        
        