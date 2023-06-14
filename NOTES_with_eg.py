                                          # PYTHON NOTES 


#a='ishan'
#print(type(a))

#ishan=34.4
#print(ishan)

#b=True
#print(type(b))

#a=True-False          #To show internally true=1,false=0
#print(a)


#i=2+4j         #4j is imaginary part
#print(type(i))

#t=3-8j               #To get the real part
#print(t.real)

#t=3-8j               #To get the imaginary part
#print(t.imag)
#print(t.real)

#a="heavy"          #To show indexing  
#print(a[2])        Forward indexing

#c="hi there"          
#print(c[-7])       Backward indexing (Space is also stored as a index here 2 or -6)

#user_1=[2,4,5,'hope',4+5j,True]        #Indexing in list
#print(user_1[1])
#print(user_1[-2])

#user_1=[2,4,5,'hope',4+5j,True]    #Showing mutability in list for a particular index
#user_1[4]='False'       
#print(user_1)                       #List are mutable

#a='ISHAN'   #Strings are immutable
#a[3]='s'
#print(a) -----> Error

#a=5//3            #Floor division (Rounds the result to nearest whole number)
#print(a)---->1

#a=~12                 #Tild inverts all the bits
#print(a)-----> -13

#a=33>>2                #Right shift operator(Shifts as many number from right of bin(a) as number b and gives binary equalent of left over(a>>b))
#print(a)----->8
#print(bin(33))----->0b100001
#print(bin(8))----->0b1000

#a=80<<2            #Left Shift operator(Adds as many zero on left as number of b(a<<b))
#print(a)----->320
#print(bin(80))---->0b1010000
#print(bin(320))--->0b101000000


#CONDITIONAL STATEMENTS:

#a=11
#if(a>=11):
#    print("hi")---->hi


#b=40
#if(b<30):
#    print('HI')
#elif(b>12):        -------->OK
#    print("OK")

#x=34
#y=66
#if(y<x):
#    print("HAPPY")
#elif(x==y):                   #We can use as many elif
#    print("BETTER")
#else:         ------------->Fine
#    print("Fine")
    
  #           !!!!!!!!!!!!!!! MINTAIN INDENTATIONS !!!!!!!!!!!

#a=input()
#print(a)--->45---->"45"

#a=int(input())
#print(a)---->778---->778


#a=float(input())
#b=int(input())
#if(b>a):        ---------------->33.8,77----->lion
#    print("lion")
#elif(b==a):
#    print("TIGER")
#else:
#    print('CAT')        

#LOOPING

#a=12
#b=23
#while(a<b):
#    print(a)-------> 12,19
#    a=a+7

#x=8      #else will print when while is successfully completed
#y=29
#while(x<y):---------->29
#    print(y)          20
#    y=y-9             11
#else:                 ITS DONE
#    print('ITS DONE')

#x=7                    (#When the break applies else do not print)
#y=19
#while(y>x):-------->19 GO 16 GO 13 GO 10
#    print(y)
#    y=y-3
#    if(y==7):
#        break
#    else:
#        print("GO")


#a="ishan"
#for c in a:---------->i
#    print(c)          s
#                      h
#                      a
#                      n


#x=[2,3,44.9,'YOUR',False]
#for c in x:
#    print(type(c))

##x=[2,3,44.9,False]          #(Else holds after for loop is completed successfully)
#for c in x:-------------->int,int,float,bool,HI
#    print(type(c))
#else:
##    print("HI")

#x=[2,3,44.9,89.8,'YOUR',False]
#for c in x:
 #   print(type(c))-------->int,int,float,float
#    if(c==89.8):
 #       break
#else:
 #   print("BYE")


#a=list(range(10))------->[1,2,3,4,5,6,7,8,9]
#print(a)

#a=list(range(1,6))------->[1,2,3,4,5]
#print(a)


# In a multiple line sentence we use triple double quotes(""") or triple single quotes(''')
# to convert to string

#String Methods::::


# capitalize()------>	Converts the first character to upper case
# casefold()---->	Converts string into lower case
# center()--->	Returns a centered string
# count()--->	Returns the number of times a specified value occurs in a string
# encode()---->	Returns an encoded version of the string
# endswith()---->	Returns true if the string ends with the specified value
# expandtabs()----->	Sets the tab size of the string
# find()---->	Searches the string for a specified value and returns the position of where it was found
# format()---->	Formats specified values in a string
# format_map()----->	Formats specified values in a string
# index()----->	Searches the string for a specified value and returns the position of where it was found
# isalnum()----->	Returns True if all characters in the string are alphanumeric
# isalpha()--->	Returns True if all characters in the string are in the alphabet
# isdecimal()----->	Returns True if all characters in the string are decimals
# isdigit()----->	Returns True if all characters in the string are digits
# isidentifier()------>	Returns True if the string is an identifier
# islower()----->	Returns True if all characters in the string are lower case
# isnumeric()------>	Returns True if all characters in the string are numeric
# isprintable()------>	Returns True if all characters in the string are printable
# isspace()----->	Returns True if all characters in the string are whitespaces
# istitle()------>	Returns True if the string follows the rules of a title
# isupper()------->	Returns True if all characters in the string are upper case
# join()------->	Joins the elements of an iterable to the end of the string
# ljust()------->	Returns a left justified version of the string
# lower()------>	Converts a string into lower case
# lstrip()------->	Returns a left trim version of the string
# maketrans()------->	Returns a translation table to be used in translations
# partition()-------->	Returns a tuple where the string is parted into three parts
# replace()------>	Returns a string where a specified value is replaced with a specified value
# rfind()------>	Searches the string for a specified value and returns the last position of where it was found
# rindex()------>	Searches the string for a specified value and returns the last position of where it was found
# rjust()------>	Returns a right justified version of the string
# rpartition()----->	Returns a tuple where the string is parted into three parts
# rsplit()------->	Splits the string at the specified separator, and returns a list
# rstrip()------>	Returns a right trim version of the string
# split()------>	Splits the string at the specified separator, and returns a list
# splitlines()------->	Splits the string at line breaks and returns a list
# startswith()------->	Returns true if the string starts with the specified value
# strip()------>	Returns a trimmed version of the string
# swapcase()------>	Swaps cases, lower case becomes upper case and vice versa
# title()------->	Converts the first character of each word to upper case
# translate()------>	Returns a translated string
# upper()------>	Converts a string into upper case
# zfill()------>	Fills the string with a specified number of 0 values at the beginning


#     LISTS

# Lists are used to store multiple items in a single variable.


# a=[2,3,'rise',True,336.33,False,'above',7+9j]
# print(type(a))-------->  <class list>
# print(a[2])---> 'rise'
# print(a[7])--------> 7+9j
# print(a[:3])------->[2,3,'rise']
# print(a[-2])------------>'above'
# print(a[-1: -9:-1]) or print(a[::-1])----->[(7+9j), 'above', False, 336.33, True, 'rise', 3, 2]
# This is a temporary reverse,to make it permanent we assign it i.e z=a[::-1]
# print(a[0::2])------->[2, 'rise', 336.33, 'above'] (to get even indexes)
# print(a[2][0:2])---->ri

# b=[3,4,5]
# print(a+b)---->[2, 3, 'rise', True, 336.33, False, 'above', (7+9j), 3, 4, 5]

# print(b*3)----->[3, 4, 5, 3, 4, 5, 3, 4, 5]
# print(len(a))------>8

# Method	                 Description
# append()---->	Adds an element at the end of the list
# clear()----->	Removes all the elements from the list
# copy()----->	Returns a copy of the list
# count()----->Returns the number of elements with the specified value
# extend()----->	Add the elements of a list (or any iterable), to the end of the current list
# index()------>	Returns the index of the first element with the specified value
# insert()---->	Adds an element at the specified position
# pop()-------->	Removes the element at the specified position
# remove()--------->	Removes the item with the specified value
# reverse()---------->	Reverses the order of the list
# sort()-------------->	Sorts the list

# a.append('me')
# print(a)------>[2,3,'rise',True,336.33,False,'above',7+9j,'me']

# a.append(b)
# print(a)------------>[2, 3, 'rise', True, 336.33, False, 'above', (7+9j), [3, 4, 5]]
# print(a[8][1])---------------->4


# a=[2,3,'rise',True,336.33,False,'above',7+9j]
# a.extend('ishan')
# print(a)----------->[2, 3, 'rise', True, 336.33, False, 'above', (7+9j), 'i', 's', 'h', 'a', 'n']

# a.extend(4)
# print(a)------->Error
# This is because extend will add only those data that has data inside data.
# a.extend([3,4,5])
# print(a)------>[2, 3, 'rise', True, 336.33, False, 'above', (7+9j), 3, 4, 5]

# a.extend([3,4,'daddy'])
# print(a)---------------->[2, 3, 'rise', True, 336.33, False, 'above', (7+9j), 3, 4, 'daddy']

# a=[2,3,'rise',True,336.33,False,'above',7+9j]
# a.insert(1,9)
# print(a)--------------->[2, 9, 3, 'rise', True, 336.33, False, 'above', (7+9j)]
# a.insert(3,'big')
# print(a)-------------->[2, 9, 3, 'big', 'rise', True, 336.33, False, 'above', (7+9j)]
# a.insert(0,[3,4])
# print(a)------------>[[3, 4],2, 9, 3, 'big', 'rise', True, 336.33, False, 'above', (7+9j)]
# a.insert(-1,55)
# print(a)----->[2, 9, 3, 'rise', True, 336.33, False, 'above', 55, (7+9j)]


# a=[2,3,'rise',True,336.33,False,'above',7+9j]
# a.pop()
# print(a)--------->[2, 3, 'rise', True, 336.33, False, 'above']
# print(a.pop())----->(7+9j)

# a=[2,3,'rise',True,336.33,False,'above',7+9j]
# a.pop(3)
# print(a.pop(5))----------->above
# print(a)------------------>[2, 3, 'rise', 336.33, False, (7+9j)]
# If we write ndex inside pop() it removes the next index


# a=[2,3,'rise',True,336.33,False,'above',7+9j]
# a.remove(336.33)
# print(a)---------->[2, 'rise', True, 336.33, False, 'above', (7+9j)]
# Remove  removes thr  specified value

# a=[2,3,'rise',True,336.33,False,'above',7+9j]
# a.insert(2,[5,6,7])
# print(a)------------->[2, 3, [5, 6, 7], 'rise', True, 336.33, False, 'above', (7+9j)]
# a[2].remove(6)
# print(a)------------------>[2, 3, [5, 7], 'rise', True, 336.33, False, 'above', (7+9j)]
# We cannot perform the above process in string
# Eg; a[2].remove('ri')
# print(a)---------->ERROR

# a=[2,3,3,'rise',True,336.33,False,'above',7+9j]
# a.remove(3)
# print(a)-------->[2,3, 'rise', True, 336.33, False, 'above', (7+9j)]
# a.remove(3)
# print(a)-------------->[2, 'rise', True, 336.33, False, 'above', (7+9j)]

# a=[2,3,'rise',True,336.33,False,'above',7+9j]
# a.reverse()
# print(a)---------------------->[(7+9j), 'above', False, 336.33, True, 'rise', 3, 2]
# This reverses the list  permanently


# a=[4,6,77,88,9,6,7,2,3,1]
# a.sort()
# print(a)--------------->[1, 2, 3, 4, 6, 6, 7, 9, 77, 88]
# It sorted in ascending order.

# a=['mm','king','ishan','go',"queen"]
# a.sort()
# print(a)---------------->['go', 'ishan', 'king', 'mm', 'queen']
# It sorted in alphabatical order.

# a=['mm','king','ishan','go',"queen"]
# a.sort(reverse=True)
# print(a)------------->['queen', 'mm', 'king', 'ishan', 'go']
# It sorted in descending alphabatical order

# a=[4,6,77,88,9,6,7,2,3,1]
# a.sort(reverse=True)
# print(a)
# It sorted in descending order.

# a=[4,6,77,88,9,6,7,2,3,1,3,33,4,3,3]
# print(a.count(3))------------------>4
# It counts the number of times the the specified value has occured in the list

# a=['above',3,3,'rise',True,336.33,False,'above',7+9j]
# print(a.count('above'))------------>2

# a=['above',3,3,'rise',True,336.33,False,'above',7+9j]
# print(a.index('above'))--------->0
# print(a.index(True))------------>4
# .index gives the index of first occurence of the specified value.

# a=[34,3,55,678,87,66]
# a[2]=97
# print(a)------>[34, 3, 97, 678, 87, 66]
# This shows lists are mutable.And the change is permanent.

# a='hi how are you'
# a[3]='r'
# print(a)----->'str' object does not support item assignment
# This shows strings are immutable.

# a='hi how are you'
# print(a.replace('h','y'))------>yi yow are you
# print(a)----------------------->hi how are you
# This does not proves mutability as the change is not permanent, to make it permanent
# assign a variable eg :
# f=a.replace('h','y')
# print(f)-------------->yi yow are you
# print(a)----------------------->hi how are you

# TUPLES

# A tuple is a collection which is ordered and unchangeable.

# w=(2,4,5.5,66,7,'ishan',5+8j,True,[2,3,4])
# print(len(w))------->9
# print(type(w))---------><class 'tuple'>
# print(w[4])---------->7
# print(w[-1])---------->[2, 3, 4]

# w[1]=9
# print(w)-------->'tuple' object does not support item assignment
# This shows tuples are also immutable like strings

# print(w[::-1])-------->([2, 3, 4], True, (5+8j), 'ishan', 7, 66, 5.5, 4, 2)
# print(w)--------------->(2, 4, 5.5, 66, 7, 'ishan', (5+8j), True, [2, 3, 4])


# Method	                       Description
# count()-->	Returns the number of times a specified value occurs in a tuple
# index()--->	Searches the tuple for a specified value and 
#             returns the position of where it was found


# w=(2,4,5.5,66,7,'ishan',5+8j,True,[2,3,4])
# print(w.count(5.5))------->1
# print(w.index([2,3,4]))----->8


# SETS

# A set is a collection which is unordered, unchangeable*, and unindexed.

# s={3,6,7.8,0.9,'visen',9-3j,False}
# print(type(s))---><class 'set'>

# s={3,6,7.8,0.9,'visen',9-3j,False,[4,5,6]}
# print(type(s))----->unhashable type: 'list'

# s={3,6,7.8,0.9,'visen',9-3j,False,(4,5,6)}
# print(type(s))-----><class 'set'>
# Sets only accepts immutable objects.

# s={3,6,7.8,0.9,3,2,4,3,1,5,5,6,7,7,3,4,5,9,8,5,6,8,9}
# print(s)----->{0.9, 1, 2, 3, 4, 5, 6, 7.8, 7, 9, 8}
# Set only keeps unique data but not  in arranged order(it just seems like it does).
# Example:q={33,44,55,67,888,998,76,43,23,554,332}
#         print(q)-------------------->{33, 67, 998, 554, 43, 44, 76, 332, 55, 23, 888}

# s=[3,6,7.8,0.9,3,2,4,3,1,5,5,6,7,7,3,4,5,9,8,5,6,8,9]
# e=set(s)
# print(e)----------->{0.9, 1, 2, 3, 4, 5, 6, 7.8, 7, 9, 8}
# s1=list(e)
# print(s1)------------>[0.9, 1, 2, 3, 4, 5, 6, 7.8, 7, 9, 8]

# q={33,44,55,67,888,998,76,43,23,554,332}
# print(q[2])-------->'set' object is not subscriptable
# print(q[1::3])--------->'set' object is not subscriptable


# Method	                        Description
# add()	----------->Adds an element to the set
# clear()--------->	Removes all the elements from the set
# copy()------------->	Returns a copy of the set
# difference()----------->	Returns a set containing the difference between two or more sets
# difference_update()----->	Removes the items in this set that are also included in another, 
#                            specified set
# discard()-------->	Remove the specified item
# intersection()--------->	Returns a set, that is the intersection of two other sets
# intersection_update()--------->	Removes the items in this set that are not present in other,
#                                 specified set(s)
# isdisjoint()----------->	Returns whether two sets have a intersection or not
# issubset()------------->	Returns whether another set contains this set or not
# issuperset()-------------->	Returns whether this set contains another set or not
# pop()------------->	Removes an element from the set
# remove()------------>	Removes the specified element
# symmetric_difference()--------->	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()------------>	inserts the symmetric differences from 
#                                             this set and another
# union()----------------------->	Return a set containing the union of sets
# update()----------------------->	Update the set with the union of this set and others

# q={33,44,55,67,888,998,76,43,23,554,332}
# q.add(88)
# print(q)--------->{33, 67, 998, 554, 43, 44, 76, 332, 55, 23, 888, 88}
# q.remove(55)
# print(q)----->{33, 67, 998, 554, 43, 44, 76, 332, 23, 888}


# Dictionaries

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.

# d={}
# print(type(d))----------><class 'dict'>
# When a curly bracket is having  linear elements i.e without key value pair is a set

# d1={'key':'value','name':'ishan','number':87263,'email':'ishan@mail.com'}
# d2={37126:'mynum','#%^&*':'specialcase',True:22490}
# print(d1['number'])---------->87263
# print(d2[True])-------->22490 

# d4={'name':'ishan','surname':'visen','name':'ISHAN'}
# print(d4['name'])------------------>ISHAN
# Key should be unique else the interpreter will give the last value as the output

# d4={'name':'ishan','surname':'visen','games':['cr',4,5,6,True]}
# print(d4)------->{'name': 'ishan', 'surname': 'visen', 'games': ['cr', 4, 5, 6, True]}
# print(d4['games'][3])----------->6
# Can also store list as a value

# d4={'numbers':[2,3,4,5],'date':(2,3,5,7,8),'month':{3,4,5,12,33}}
# print(d4)------->{'numbers': [2, 3, 4, 5], 'date': (2, 3, 5, 7, 8), 'month': {33, 3, 4, 5, 12}}
# We can also keep list,tuple,set,dictionary as a value

# d4={'numbers':[2,3,4,5],'date':(2,3,5,7,8),'month':{3,4,5,12,33}}
# d4['name']=['me','you','him']
# print(d4)->{'numbers': [2, 3, 4, 5], 'date': (2, 3, 5, 7, 8), 'month': {33, 3, 4, 5, 12}, 'name': ['me', 'you', 'him']}
 
# If we add a key that already exist then python will update the value of old ke

# Method	                      Description
# clear()------------->	Removes all the elements from the dictionary
# copy()------------->	Returns a copy of the dictionary
# fromkeys()------------>	Returns a dictionary with the specified keys and value
# get()---------------->	Returns the value of the specified key
# items()-------------------->Returns a list containing a tuple for each key value pair
# keys()---------------------->	Returns a list containing the dictionary's keys
# pop()------------------>	Removes the element with the specified key
# popitem()---------------------->	Removes the last inserted key-value pair
# setdefault()------->	Returns the value of the specified key. 
#                        If the key does not exist: insert the key, with the specified value
# update()----------->	Updates the dictionary with the specified key-value pairs
# values()---------------->	Returns a list of all the values in the dictionary




# d4={'numbers':[2,3,4,5],'date':(2,3,5,7,8),'month':{3,4,5,12,33}}
# del d4['date']
# print(d4)---->{'numbers': [2, 3, 4, 5], 'month': {33, 3, 4, 5, 12}}


# d4={'numbers':[2,3,4,5],'date':(2,3,5,7,8),'month':{3,4,5,12,33}}
# print(d4.keys())-------------->dict_keys(['numbers', 'date', 'month'])

# d4={'numbers':[2,3,4,5],'date':(2,3,5,7,8),'month':{3,4,5,12,33}}
# print(d4.values())------>dict_values([[2, 3, 4, 5], (2, 3, 5, 7, 8), {33, 3, 4, 5, 12}])

# d4={'numbers':[2,3,4,5],'date':(2,3,5,7,8),'month':{3,4,5,12,33}}
# print(d4.items())-->dict_items([('numbers', [2, 3, 4, 5]), ('date', (2, 3, 5, 7, 8)), ('month', {33, 3, 4, 5, 12})])

# d4={'numbers':[2,3,4,5],'date':(2,3,5,7,8),'month':{3,4,5,12,33}}
# d4.pop('date')
# print(d4)----------------->{'numbers': [2, 3, 4, 5], 'month': {33, 3, 4, 5, 12}}
# print(d4.pop('date'))---------->(2, 3, 5, 7, 8)

# FOR LOOP

# marks=[1,9,8,7]
# n=[]
# for c in marks:
#     n.append(c+1)
# print(n)---------------->[2, 10, 9, 8]


# user_1=["ishan","biet","college"]
# user_2=[]
# for i in user_1:
#     user_2.append(i.upper())
# print(user_2)------------------>['ISHAN', 'BIET', 'COLLEGE']    

# user_1=["ishan",1,22,345,66,'mr','94',4,'visen']
# user_2=[]
# user_3=[]
# for i in user_1:
#     if (type(i)==str):
#         user_2.append(i)
#     else:
#         user_3.append(i)
# print(user_2)---------------->['ishan', 'mr', '94', 'visen']
# print(user_3)---------------->[1, 22, 345, 66, 4]















































































