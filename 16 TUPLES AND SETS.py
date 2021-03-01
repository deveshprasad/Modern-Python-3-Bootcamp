# TUPLES HAVE OPEN BRACKET IMMMUTABLE CANT BE CHANGED
#ORDERED COLLECTION OF GROUPS OR ITEM
n=(1,2,3,4,5)
3 in n
#3 true
n[1]# value can be seen but not changed
 # tuple object doesnot support item assignment
# tuples are faster than lists 
# .items in dictionary returns tuples
second_tuple=tuple((2,3,5,7))
print(second_tuple)
#class(second_tuple)
#tuples can be used as keys in dictionary
########location={(121,232):"delhi",...}

months=("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec")
for month in months:
    print(month)
i=len(months)-1
while i>=0:
    print(months[i])
    i-=1
    # functions
# count return no of times a value appears
# index at which value is found
    #  TUPLES ARE FASTER THAN LISTS
    
    
    
    
# SETS  DONOT HAVE DUPLICATES AND NOT ORDERED
    # ITEM CANNOT BE ASSIGNED USING INDEX
s=set({1,2,3,4})
4 in s
print(s)
for i in s:
    print(i)
print(list(set(months)))
print(len(set(months)))
s.add(55)
s
s.remove(4)
# coying s 
another_s=s.copy()
another_s
another_s in s # false as it is a copy
s.clear()  # to clear the  set


# intersection
# symmetric_difference
# union


#maths|biology
#gives us union of the sets with no duplicacy
 # & operator gives intersection
# s.symmetric_difference(months)
 
 #
{x*x for x in range (10)}
{char.upper() for char in "devesh"} # unordered it will appear
string="hellohahahahaha"
{char for char in string if char in 'aeiou'}
# hives a,e,o in sets
# sequoia tree has all alphabets
string="sequoia"
{char for char in string if char in 'aeiou'}
