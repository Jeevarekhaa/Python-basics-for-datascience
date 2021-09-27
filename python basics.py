#!/usr/bin/env python
# coding: utf-8

# In[1]:


#load required library modules
import numpy as np

#Configure your output environment
#Number of digits of precision-4(by default-8)
#To avoid scientific notation printing
np.set_printoptions(precision=4,suppress=True)


# In[2]:


#My first line of code
print("Hello python")


# In[2]:


#variable creation
var1 = 23
var2 = 24


# In[4]:


#Tab completion features <Tab> for matching objects,functions,arguments,filepaths etc
var1


# In[3]:


#Tab completion features for .<Tab> for methods and attributes
v1 =[1,2,3,4]


# In[4]:


v1.clear


# In[7]:


# To seek information about the object(object introspection)
get_ipython().run_line_magic('pinfo', 'v1')


# In[8]:


# To seek information about the object(object introspection)
get_ipython().run_line_magic('pinfo', 'print')


# In[5]:


#To write a function
def pyfun(x,y,z):
    return(x*y)/z


# In[6]:


#To show the source code
get_ipython().run_line_magic('pinfo2', 'pyfun')


# In[12]:


#To search the namespace --(all names matching the wildcard expression)
get_ipython().run_line_magic('psearch', 'np.*load*')


# In[14]:


#running special commands
get_ipython().system('pip list')


# In[15]:


#magic commands
get_ipython().run_line_magic('lsmagic', '')


# In[16]:


#current working directory
get_ipython().run_line_magic('pwd', '')


# In[2]:


#list the files and folders
get_ipython().run_line_magic('ls', '')


# In[9]:


# %load pyscript.py
#load a python script
get_ipython().run_line_magic('load', 'testscript.py')
def pyfun(x,y,z):
    return(x*y)/z;
x=1
y=2
z=7
result=pyfun(x,y,z)


# In[8]:


#run a python script
get_ipython().run_line_magic('run', 'pyscript.py')


# In[27]:


z


# In[28]:


x


# In[29]:


y


# In[30]:


result


# In[10]:


# %load pyscript.py
#load a python script

def pyfun(x,y,z):
    return(x*y)/z;
x=1
y=2
z=7
result=pyfun(x,y,z)


# In[11]:


#integrate with data visualization
#matplotlib integration
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


#load required library modules
import matplotlib.pyplot as plt


# In[13]:


#EXAMPLE
plt.plot(np.random.randn(50).cumsum())


# In[36]:


np.random.randn(50)


# In[37]:


np.random.randn(50).cumsum()


# In[3]:


#Essential python programming concepts
#for loop - INDENDATION NOT BRACES AND WHITESPACES(TABS,SPACES) are used instead of braces
#colon denotes the start of an indented codeblock
array=[1,3,5,4,8,9,10,2,14,17]
pivot = 8
less = []
greater =[]
for a in array:
    if a < pivot:
        less.append(a)
    else:
        greater.append(a)
        


# In[43]:


less


# In[11]:


less.sort(key=None,reverse=True)


# In[10]:


less


# In[12]:


less.sort(key=None,reverse=False)


# In[13]:


less


# In[44]:


greater


# In[45]:


#semicolon is used to separate multiple statements on a single line instead of termination of a statement like in C
a=1; b=3; c=5


# In[46]:


print("this is an example for command line")  #example for commandline


# In[14]:


#function and object method calls
#function call without argument and return value assignment
def j():
    print("Hi this is an function with no arguments")
j()


# In[18]:


#function call with argument and return value assignment
melbin =pyfun(x,y,z)
melbin


# In[20]:


#functions attached with objects are called methods and have access to object's internal data
less.append(melbin)
less


# In[50]:


#positional and keyword arguments
def i(e,d,c,a=2,b='jeeva'):
    print(b,(x+y+z)/a)
    
i(x,y,z,a=1,b='jeevarekhaa')


# In[ ]:





# In[51]:


i(x,y,z,b='jeevarekhaa',a=1)


# In[27]:


#variable assignment and arguments passing
#Both the variables refer to the same object
#variables are names of objects within a particular namespace
v2=v1
v2


# In[33]:


v1.append(5)
v1


# In[34]:


v2


# In[14]:


a=[2,3,4]
b=a


# In[15]:


b


# In[16]:


a.append(8)


# In[17]:


b


# In[18]:


b.append(10)


# In[20]:


b


# In[19]:


a


# In[56]:


#Passing objects as arguments to function
def append_El(alist,el):
    alist.append(el)
    print(alist)
    print (el)
append_El(v1,9)


# In[57]:


v1


# In[58]:


alist


# ![Jeevarekhaa_20381026.jpg](attachment:Jeevarekhaa_20381026.jpg)

# In[21]:


a=5
isinstance(a,int)


# In[23]:


a='Jeeva rekhaa'
a.split()


# In[3]:


getattr(a,'split')


# In[24]:


if not isinstance(a,list):
    a=list(a)


# In[25]:


type(a)


# In[6]:


import pyscript 


# In[7]:


result=pyscript.pyfun(5,6,7)
result


# In[8]:


pyscript.x


# In[37]:


from pyscript import x,y,z,pyfun


# In[38]:


result1=pyfun(8,9,10)
result1


# In[26]:


import pyscript as pysc


# In[27]:


#or
from pyscript import x as a,y as b,z as c


# In[28]:


result3=pysc.pyfun(2,3,5)


# In[29]:


result3


# In[30]:


pysc.x


# In[39]:


pysc.result3


# In[36]:


get_ipython().run_line_magic('pinfo', 'pyscript.result')


# In[35]:


pysc.result


# In[20]:


a


# In[21]:


b


# In[22]:


a&b


# In[24]:


a|b


# In[25]:


a^b


# In[27]:


int1=123456789
int1


# In[28]:


f=2e-3


# In[29]:


f


# In[30]:


str1="hi heloo"
str1


# In[31]:


str2="""
hi all this is jeevarekhaa
this is using triple quotes
"""
str2


# In[32]:


str2.count("\n")


# In[35]:


strex="this is a string"
strex=strex.replace("string","longer")
strex


# In[40]:


str4="hi hello"
str4
str4.replace("hello","jeeva")
str4


# In[37]:


str4


# In[38]:


print(str4.replace("hello","heeva"))


# In[39]:


print(str4)


# In[40]:


str5=str4.replace("hello","jeevarekhaa")


# In[41]:


str5


# In[46]:



str6=str(int1)


# In[47]:


str6


# In[48]:


print(str6)


# In[49]:


list(str5)


# In[50]:


str5[2:]


# In[51]:


print(str5[2:])


# In[52]:


print("12\34")


# In[53]:


print("12\\34")


# In[54]:


print("12\n34")


# In[55]:


print("12\\n34")


# In[57]:


strbac="this\has\a\lot\of\backslashes"
print(strbac)
strbac1 = r"this\has\a\lot\of\backslash"
print(strbac1)


# In[60]:


temp1="US-INDIA exchange rate:{0:.4f} {1:s} are worth ${2:d}"
print(temp1.format(71.45678,'Indian rupees',1))


# In[1]:


f


# In[2]:


f=1.23456
type(f)


# In[3]:


int(f)


# In[4]:


bool(f)


# In[5]:


bool(-1.2)


# In[6]:


bool(0)


# In[8]:


def f2(a,b,c=None):
    result=a*b
    if c==None:
        result=result+1
    return result


# In[10]:


result= f2(5,6)


# In[11]:


result


# In[12]:


type(None)


# In[13]:


#dates and times
from datetime import datetime,date,time


# In[15]:


dt=datetime(2021,8,11,22,30,10)


# In[16]:


dt.day


# In[17]:


dt.month


# In[18]:


dt.year


# In[19]:


dt.hour


# In[20]:


dt.minute


# In[21]:


dt.date()


# In[22]:


dt.time()


# In[25]:


#formatting datetime as string
dt.strftime('%m/%Y')


# In[26]:


#parsing the string
datetime.strptime('20191018','%Y%m%d')


# In[27]:


dt.replace(minute=0,second=0)


# In[29]:


dt2=datetime(2019,10,10,12,12)
dt2


# In[30]:


delta=dt2-dt
delta


# In[31]:


type(delta)


# In[32]:


dt


# In[33]:


dt+delta


# In[34]:


#control flow -conditional logic--> if,elif,else
x=-1
if x<0:
    print('its negative')


# In[35]:


x=2
if x<0:
    print("its negative")
elif x==0:
    print('its zero')
elif 0<x<5:
    print('positive but less than five')
else:
    print('positive and larger than five')
    


# In[7]:


#and or conditions
a=15;b=17;
c=10;d=18


# In[37]:


if a<b or c>d:
    print("reached")


# In[38]:


#chain comparisons because 2 is less than 3
1<2>3<4


# In[40]:


#LOOPS
for x in [1,2,3]:
    print (x)


# In[41]:


#continue
seq=[0,1,2,None,4,None,5]
i=0
for x in seq:
    if x==None:
        continue
    i+=x
print (i)


# In[43]:


#break
seq=[0,1,2,3,4,5,5]
i=0
for x in seq:
    if x > 4:
        break
    i+=x
print (i)


# In[45]:


for i in range(5):
    for j in range(5):
        if j>i:
            break
        print((i,j))
        


# In[47]:


#while
x=112
i=0
while x>0:
    if i>200:
        break
    i+=x
    x=x//2


# In[48]:


i


# In[49]:


x


# In[51]:


#pass
if x<0:
    print("hi")
elif x==0:
    pass
else:
    print("helo")


# In[52]:


#range function
list(range(5))


# In[54]:


#(start,end,step)
list(range(0,10,2))


# In[55]:


range(5)


# In[56]:


list(range(0,10,1))


# In[58]:


list(range(4,-4,-1))


# In[41]:


seq=[1,2,3,4,5,6,7,9]
for x in range(len(seq)):
    v5=seq[x]
v5


# In[62]:


sum=0
for x in range(100000):
    if x%2==0 or x%3==0:
        sum+=x
    


# In[63]:


x


# In[64]:


sum


# In[65]:


#ternary expression
if x<0:
    'negative'
else:
    'positive'


# In[67]:


c='negative' if x<0 else 'positive'


# In[68]:


c


# In[69]:


#TUPLE=Fixed length,immutable
tup=(1,5,9)
tup


# In[70]:


tup1=2,6,10
tup1


# In[72]:


#nested tuple
nestup =(1,5,9),(2,6,10)
nestup


# In[27]:


#typecasting to tuple
tup2=tuple([1,0,2])
tup2


# In[31]:


tup3=tuple("jeeva rekhaa")
tup3


# In[76]:


tup3[3]


# In[23]:


tup4=tuple(['jee',[0,1],False])
tup4


# In[24]:


tup4[2]=True


# In[25]:


#modification of tuple for inplace elements - because list (intuple)can be modified
tup4[1].append(2)
tup4


# In[80]:


tup4+tup3


# In[28]:


tup2*3


# In[82]:


#unpacking tuple
a,b,c=tup1
c


# In[83]:


(x,y,z),(p,q,r)= nestup
q


# In[84]:


#swapping variable name
a,b,c=c,b,a
c


# In[2]:


#Iterating over sequences of tuples or lists
seq=[(1,2,3),(4,5,6),(7,8,9)]
for x,y,z in seq:
    print('x={0},y={1},z={2}'.format(x,y,z))


# In[42]:


seq=[(1,2,3),(4,5,6),(7,8,9)]
for x in seq:
    print('x={0}'.format(x))


# In[11]:


#returning multiple values from a function
def f(x,y,z):
    x=x*y
    y=y*z
    z=z*x
    return(x,y,z)
d,e,f = f(a, b, c)


# In[12]:


d,e,f


# In[10]:


b


# In[13]:


tup6=1,2,3,4,5,6,7
a,b,*rest=tup6
a,b


# In[14]:


rest


# In[15]:


*rest1,c,d=tup6


# In[16]:


c,d


# In[17]:


rest1


# In[18]:


a,b,*rest2,c=tup6
rest2


# In[19]:


c


# In[32]:


#tuple method --> count
tup4.count('e')
tup3.count('e')


# In[33]:


#LIST --mutable
v1=[1,3,None,5,True]
v1


# In[35]:


v2=list(tup6)
v2


# In[36]:


v2[3]


# In[37]:


v2[3]='Jeeva'
v2


# In[38]:


list(range(6))


# In[40]:


#appending 
v2.append('JEE')
v2


# In[41]:


v2.insert(1,'rekhs')


# In[42]:


v2


# In[43]:


#removing an element
element=v2.pop()
element


# In[44]:


v2


# In[46]:


v2.remove(7)


# In[47]:


v2


# In[48]:


#in,notin
2 in v2


# In[49]:


7 in v2


# In[50]:


'rekhs' in v2


# In[51]:


#concatenation
v1+v2


# In[53]:


#adding multiple elements by extend
v1.extend(['melbin','sai','sasi'])
v1


# In[54]:


#sorting the elements
v3=[10,56,19,85,32]
v3.sort()
v3


# In[55]:


#sort using key
v4=['hiIII','all','tr','JG']
v4.sort(key=len)
v4


# In[56]:


#inserting new element in sorted list
#using bisect module
import bisect
#to find the index of location
bisect.bisect(v3,12)


# In[57]:


#to insert at an appropriate index into sorted list
bisect.insort(v3,24)
v3


# In[58]:


v3[1:5]


# In[59]:


#partial modification
v3[0:2]=[1,2,3]
v3


# In[60]:


v3[:5]


# In[61]:


v3[6:]


# In[62]:


#negative index
v3[-3:]


# In[63]:


v3[-5:-2]


# In[64]:


v3


# In[65]:


#every second element after start
v3[::2]


# In[66]:


v3[::3]


# In[67]:


v3


# In[68]:


#reversing a list
v3[::-1]


# In[69]:


#reversing a tuple using slicing index
tup6


# In[70]:


tup6[::-1]


# In[43]:


seq=[7,2,5,4,9]
i=0
for x in seq:
    x=x+i
    i+=1
print(i,x)


# In[75]:


#using enumerate function
for i,x in enumerate(seq):
    x=x+i


# In[76]:


i


# In[77]:


x


# In[78]:


enumerate(seq)


# In[79]:


list(enumerate(seq))


# In[80]:


v4


# In[81]:


#dict
mapping={}
for i,x in enumerate(v4):
    mapping[x]=i
mapping


# In[82]:


#sorted
sorted([7,56,14,23,14])


# In[83]:


sorted(['tr', 'JG', 'all', 'hiIII'])


# In[1]:


#zip function
seq1=['hi','all']
seq2=('jeeva','rekhaa')
list(zip(seq1,seq2))


# In[2]:


seq3=[True,False]
list(zip(seq1,seq2,seq3))


# In[3]:


for i,(a,b) in enumerate(zip(seq1,seq2)):
    print('{0}:{1},{2}'.format(i,a,b))


# In[88]:


#unzipping the sequence
zseq=[('hi','rekhaa'),('hol','hola')]
useq1,useq2=zip(*zseq)


# In[89]:


useq1


# In[90]:


useq2


# In[91]:


reversed(range(10))


# In[92]:


list(reversed(range(10)))


# In[4]:


#DICTIONARY - mutable, key value pairs
#also called hash map or associative array
#key value pairs are separated using (:)
d={}
d


# In[45]:


d1={'s':'jeeva','i':[1,2,3]}
d1


# In[8]:


#accessing dict elements using [] operator using keys in dictionaries because they are unordered so we cant go for indices
d1['i']


# In[9]:


d1['s']


# In[46]:


#adding elements in a dict
d1['f']=[1,2,3,4,5]
d1


# In[47]:


d1['dummy']='xyz'
d1[9]='a value'
d1


# In[48]:


#modifying elements of a dict
d1[9]='value dey'
d1


# In[13]:


#to check whether a key is present in a dict
'f' in d1


# In[49]:


'xyz' in d1


# In[15]:


'i' in d1


# In[16]:


'i' not in d1


# In[17]:


#Removing elements in a dict
#by using del keyword or pop method
del d1[9]
d1


# In[18]:


poped=d1.pop('dummy')
d1
poped


# In[19]:


d1


# In[20]:


#keys and values method
d1.keys()


# In[21]:


list(d1.keys())


# In[22]:


d1.values()


# In[23]:


list(d1.values())


# In[24]:


#merging two dicts by update method
d2={'A':'a','B':'b'}
d2


# In[25]:


d1.update(d2)


# In[26]:


d1


# In[27]:


d1.update({'C':'c'})
d1


# In[31]:


d1.update({'f':[1.2,2.3,4.5]})
d1


# In[33]:


#pairing up 2 sequences element-wise to create a dict
mapping2={}
for k,v in zip(d1.keys(),d1.values()):
    mapping2[k]=v
mapping2


# In[36]:


dict(zip(d1.keys(),d1.values()))


# In[39]:


#using dict function to create a dict
#DICT is a essentially a collection of two tuples where combined elements are separated by : instead of ','
mapping3=dict(zip(range(5),reversed(range(4))))


# In[40]:


mapping3


# In[42]:


#list of tuples
list(zip(range(5),reversed(range(4))))


# In[43]:


#useful dict methods
#get and pop
d1.get('s')


# In[44]:


d1.get('t')# nothing will be returned because t key doesnt exist in d1


# In[45]:


#change the default returned value
d1.get('t','key not found ra')


# In[46]:


d1.pop('t')


# In[47]:


d1.get('t','key not found')


# In[1]:


#set default
#useful to set values while generating a dict like categorizing a list of terms by their first letters as a dict of lists
terms=['alpha','beta','gamma','alpha2','beta2','gamma2']
d3={}
for x in terms:
    d3.setdefault(x[1],[]).append(x)
d3


# In[49]:


#default dict from collections module
from collections import defaultdict
first_letter=defaultdict(list)
for  x in terms:
    first_letter[x[0]].append(x)
first_letter


# In[50]:


#dict keys generally have to be immutable objects
#dict values can be any python object
{0:3,1:2,[3]:0}


# In[51]:


{0:3,1:2,(3):0}


# In[52]:


#element of tuple is list so error
{0:3,1:2,([3]):0}


# In[53]:


#to check whether an object can be used as a dict key
#hash function
hash('a')


# In[54]:


hash(0)


# In[55]:


hash((1,2,3))


# In[56]:


hash((1,[2,3]))


# In[57]:


#set
#similar to dictionary with keys and without values
#unordered collection of unique elements
#created with a comma separated collection of unique elements using {} operator or set function
set1={1,2,3}
set1


# In[59]:


#allows only unique elements
{2,2,2,3,3}


# In[61]:


set2=set([4,5,5,6])
set2


# In[62]:


#set operation: union of sets
#using union method or | operator
set3=set1.union(set2)
set3


# In[63]:


set1|set2


# In[64]:


set1|set2|set3


# In[65]:


#set operation: intersection of sets
#using intersection method or & operator
set4=set1.intersection(set3)
set4


# In[66]:


set2&set3


# In[67]:


#no common elements
set1&set2&set3


# In[68]:


#set update method using |= operator(inplace counterparts no need of saving it)
set4.update(set2)
set4


# In[71]:


set4 |={7,8,9}
set4


# In[72]:


set4.add(10)
set4


# In[73]:


#remove or pop method
set4.remove(10)
set4


# In[75]:


#pop removes some arbitrary element
set4.pop()


# In[76]:


set4.pop()


# In[77]:


#using clear method
set4.clear()
set4


# In[78]:


set4.pop()


# In[79]:


#set operations:subset,superset and disjoiint
#using issubset,issuperset and isdisjoint
set1.issubset(set2)


# In[80]:


set1.issubset(set3)


# In[81]:


set2.issuperset(set3)


# In[83]:


#no common elements
set1.isdisjoint(set2)


# In[84]:


#check two sets has same elements irrespective of the container
#using == operator
{1,2,3}=={4,5,6}


# In[85]:


{1,2,3}=={2,1,3}


# In[86]:


{1,2,3}=={(3,2),1}


# In[87]:


{1,2,3}=={(3),2,1}


# In[1]:


#set elements has to be immutable objects like int,float,strings,tuples(immutable)
{1,2,3,[4,5,6]}


# In[2]:


{1,2,3,(4,5,6)}


# In[3]:


{1,2,3,(4,5,[6])}


# In[4]:


#LIST,SET ,DICT comprehensions
#to filter and transform the elements
#basic form:[exp for val in collection if condition]
seq4=['sri','rama','jayam','chants']
[x.upper() for x in seq4]


# In[5]:


#comprehension with filtering expression
[x.upper() for x in seq4 if len(x)>3]


# In[6]:


#Dict comprehension
#basic form: {key-exp: value-exp for value in collection if condition}
{v:i for i,v in enumerate(seq4)}


# In[7]:


#Set comprehensions
{len(x) for x in seq4}


# In[10]:


#nested list comprehensions
#EXAMPLE: Extract the list of strings with two or more a's from a list of strings
seq5=[['sri','rama','jayam'],['om','ganapathy']]
[x for f in seq5 for x in f if x.count('a')>=2]


# In[11]:


#example: to convert the list of tuples of integers to list of integers
seq6=[(1,2,3),(4,5,6),(7,8,9)]
[x for f in seq6 for x in f]


# In[12]:


#list comprehension inside a list comprehension
#convert list of tuples of integers into a list of lists of integers
[[x for x in t] for t in seq6]


# In[2]:


#FUNCTIONS are another type of python objects
#might have positional arguments and keyword arguments
#keyword arguments might follow the positional arguments
def f(x,y,z=0.5):
    if z>1:
        return z*(x+y)
    else:
        return z/(x+y)


# In[3]:


f(1,2,z=1)


# In[4]:


f(1,2,1.3)


# In[5]:


#keyword arguments
f(4.3,6)


# In[20]:


#namespace --> variable scope = local , global
v5=[]
def f1():
    for i in range(5):
        v5.append(i)
f1()


# In[21]:


v5


# In[22]:


del v5


# In[23]:


def f2():
    v5=[]
    for i in range(5):
        v5.append(i)
f2()


# In[24]:


v5


# In[26]:


#using global keyword
def f3():
    global v5
    v5=[]
    for i in range(5):
        v5.append(i)
f3()


# In[27]:


v5


# In[7]:


#Returning multiple values
def f4():
    a=5
    b=6
    c=7
    return a,b,c
a,b,c = f4()
#f4()


# In[29]:


a


# In[30]:


b


# In[31]:


c


# In[32]:


v6=f4()
v6


# In[33]:


#returning a dict
def f4():
    a=5
    b=6
    c=7
    return {'a':a,'b':b,'c':c}
v7=f4()
v7


# In[1]:


#writing more reusable and generic functions
#example: data cleaning on a list of strings like stripping whitespace, removing punctuation symbols on proper capitalization
#first approach
messy_strings = ['Alabama','Georgia!','Georgia','georgia','FlOrida','south carolina##']
import re
def clean_strings(strings):
    result=[]
    for x in strings:
        x=x.strip()
        x=re.sub('[!#?]','',x)
        x=x.title()
        result.append(x)
    return result


# In[35]:


messy_strings


# In[2]:


clean_strings(messy_strings)


# In[3]:


#second approach
#applying list of operations on a list of strings
def remove_punctuation(value):
    return re.sub('[!#?]','',value)
clean_ops = [str.strip,remove_punctuation,str.title]

def clean_strings(strings,ops):
    result=[]
    for x in strings:
        for f in ops:
            x=f(x)
        result.append(x)
    return result


# In[39]:


messy_strings


# In[40]:


clean_strings(messy_strings,clean_ops)


# In[43]:


Dict = {1:2, 3:4, 4:11, 5:6, 7:8} 
print(Dict[Dict[3]])


# In[44]:


set1={1,2,3} 
set2={4,5,6} 
set3 = set1.union(set2)  
set3


# In[46]:


def func(i):
    print("Hello world",i)
func(5,5)


# In[4]:


#map function applies a function to a sequence
for x in map(remove_punctuation,messy_strings):
    print(x)


# In[5]:


#anonymous or lambda function
#passing a function as argument that has 2 or 3 lines of code
#we wont call this lambda function that is why is anonymous
def short_f(x):
    return x*10


# In[6]:


ret2=lambda x:x*10


# In[7]:


def apply_short_f(alist,short_f):
    return [short_f(x) for x in alist]


# In[8]:


apply_short_f([0.1,0.2],lambda x:x*10)


# In[10]:


seq7=['sri','ramaaa','jayam']
seq7.sort(key=lambda x:len(x))
seq7


# In[12]:


#currying:defining a new function that calls an existing fun which has fewer arguments
def add_nos(x,y):
    return x+y
#using lambda
add_5=lambda x: add_nos(5,x)


# In[13]:


add_nos(5,2)


# In[14]:


add_5(4)


# In[15]:


def add_nos(x,y):
    return x+y
#using lambda
add_5=lambda x: add_nos(5,x)

#using partial function from builtin functions tools
from functools import partial
new_add5=partial(add_nos,8)


# In[16]:


new_add5(5)


# In[17]:


##generators are functions used to construct iterable objects
#an iterator is any obj that will yield objects so that iterations can be performed() to ther python interpreter)
d4={'a':1,'b':2,'c':3}
for i in d4:
    print(i)


# In[18]:


it=iter(d4)


# In[19]:


it


# In[20]:


list(it)


# In[21]:


type(it)


# In[35]:


#generators return a sequence of multiple elements in an orderly fashiion as and when requested
#it use 'yield' keyword instead of 'return'
def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n**2))
    for i in range(n+1):
        yield i**2


# In[23]:


g=squares()


# In[24]:


g


# In[25]:


type(g)


# In[26]:


list(g)


# In[27]:


list(g)


# In[33]:


for x in g:
    print (x,end='')


# In[38]:


g1=squares()
for x in g1:
    print (x,end=' ')


# In[39]:


list(g1)


# In[45]:


#generator expression ---similar to list comprehension wiht parathenses instead of brackets
g2=(x**2 for x in range(10))


# In[43]:


g2


# In[46]:


list(g2)


# In[48]:


#can be used as function argumensts as well
sum(x**2 for x in range(10))


# In[49]:


dict((i,i**2) for i in range(5))


# In[57]:


#other way to create generators
#using itertools library by groupby function which takes a sequence and a function as its arguments
#it groups the consecutive elements in the sequence of return value of the function
import itertools
terms=['Ram','Ramesh','seetha','sathya','jake','jeeva']
firstletter= lambda x:x[0]
for letter,terms in itertools.groupby(terms,firstletter):
    print(letter,list(terms))


# In[1]:


#EXCEPTION HANDLING
#improper input values:value error exception
float('1.2')


# In[2]:


float('abc')


# In[4]:


def attempt_float1(x):
    try:
        return float(x)
    except:
        return 'error erumaaa'


# In[5]:


attempt_float1('1.2')


# In[10]:


attempt_float1('abc')


# In[7]:


#improper input types:value error exception
float((1,2))


# In[9]:


def attempt_float2(x):
    try:
        return float(x)
    except ValueError:
        return 'error erumaaa-Improper input value'
    except TypeError:
        return 'improper input type'


# In[11]:


attempt_float2('1.23')


# In[12]:


attempt_float2('abc')


# In[13]:


attempt_float2((1,2))


# In[16]:


#Catching multiple exceptions types using one statement
def attempt_float3(x):
    try:
        return float(x)
    except (ValueError,TypeError):
        return 'Improper input value or type'


# In[17]:


attempt_float3('abc')


# In[18]:


attempt_float3((1,2))


# In[30]:


#this block gets executed even try block succeeds or not
#finally: block
#for ex: generating logs or cleaning up the python objects
#in such situation wwe might also prefer to not suppress exceptions

f1=open('tempt.txt','w')
try:
    f1.write("done\n")
except:
    f1.write("done\n")
finally:
    f1.write("log1\n")
    f1.write("log2\n")
    f1.close()


# In[31]:


f1.read()


# In[23]:


fl1=open('tempt.txt')
fl1.read()


# In[24]:


fl1.close()


# In[41]:


#EXECUTE a code block only if 'try: block' succeeds
#by using 'else:block'
fl2=open('tempt.txt','a')
try:
    fl2.write("done\n")
except:
    print("Failed")
else:
    print("Succeeded")
finally:
    fl2.close()


# In[42]:


#file manangement aspects
#python very popular for text and file munging
#by default file is opened in read-only mode
#file path:relative or absolute
path='tempt.txt'
fl3=open(path)


# In[43]:


path='tempt.txt'
fl3=open(path)


# In[44]:


#read method returns data from file as a string
fl3.read()


# In[45]:


#end of the file reached :an empty bytes object is returned
fl3.read()


# In[46]:


#closing the file objects created with open function
#resources go back to the os
fl3.close()


# In[47]:


#iterating over the lines of the file
#by treating file handle as a list
fl3=open(path)
for line in fl3:
    pass


# In[48]:


#because we iterated over the eof
fl3.read()


# In[49]:


#by default \n is the eol marker
fl3=open(path)
for line in fl3:
    print(line)


# In[50]:


#closed method returns True if the file is close
fl3.closed


# In[51]:


fl3.read()


# In[55]:


#EOL free list of lines
[line.rstrip() for line in open(path)]
#[line for line in open(path)]


# In[53]:


fl3.close()


# In[56]:


#cleaning up open files
#using 'with' keyword
with open(path) as fl4:
    [line.rstrip() for line in fl4]


# In[57]:


fl4.closed


# In[58]:


fl4.read()


# In[76]:


#python file modes for writing:should be used carefully
#'w' - write only mode: creates a new file (Erasing a data with the existing same file name)
#'x' - write only mode: creates a new file if the file path doesnt already exist
#'a' - append to existing file(creating the file if it does not already exist)
fl5=open("tempt.txt",'a')
fl5.write("appended\n")


# In[66]:


fl5.close()


# In[69]:


with open('tempt.txt') as fl6:
    lines = fl6.readlines()


# In[70]:


lines


# In[71]:


fl6=open('tempt.txt','w')


# In[72]:


fl6.read()


# In[73]:


fl6.close()


# In[74]:


fl6=open(path)
fl6.read()


# In[77]:


fl6=open('tempt.txt','x')


# In[78]:


fl6=open('tempt1.txt','x')


# In[79]:


fl6.write("sri rama jayam\n")


# In[80]:


fl6.write("sri rama jayam\n")


# In[81]:


fl6.write("\n")


# In[82]:


fl6.close()


# In[83]:


fl6=open('tempt1.txt')


# In[84]:


#commonly used methods in read modes:read,seek and tell
fl6.read(9)


# In[86]:


#to read raw bytes, binary mode(b) is used
#read method exactly return the number of bytes in this file mode
fl7=open('tempt1.txt','rb')
fl7.read(9)


# In[87]:


#tell method gives you the current position of the file handle(an integer value)
fl6.tell()


# In[88]:


fl7.tell()


# In[89]:


#check the default encoding
#by using 'sys' module
import sys
sys.getdefaultencoding()


# In[90]:


#seek method changes the file position to the indicated byte in the file
fl6.seek(5)


# In[91]:


fl6.read(3)


# In[92]:


fl7.read()


# In[93]:


fl6.close()
fl7.close()


# In[101]:


#writelines and readlines methods
#writelines method writes the passed sequence of strings of the file
#readlines method returns list of lines in the file
path1='tempt1.txt'
with open('tempt2.txt','w') as fl8:
    fl8.writelines(x for x in open(path1) if len(x)>1)


# In[102]:


with open('tempt2.txt') as fl8:
    lines = fl8.readlines()


# In[103]:


lines


# In[104]:


#bytes and unicode with files
#UTF-8 is a variable-length unicode encoding
#when requested some number of char from the file(done in the default text mode),Python reads the exact bytes from the file
with open(path1,'rb') as fl8:
    raw=fl8.read(9)


# In[105]:


raw


# In[106]:


#decoding bytes to a str object
#possible if each of the encoded unicde char is full formed given a particular text encoding
raw.decode('utf8')


# In[107]:


raw[:5].decode('utf8')


# In[108]:


raw[:4].decode('utf8')


# In[109]:


raw[:3].decode('utf8')


# In[113]:


path2='temp4.txt'
with open(path2,'w') as fl8:
    fl8.write("Naïve Baye\n")
    


# In[114]:


with open(path2,'rb') as fl8:
    raw2=fl8.read()


# In[115]:


raw2


# In[116]:


raw2[:2].decode('utf8')


# In[117]:


raw2[:3].decode('utf8')


# In[118]:


raw2.decode('utf8')


# In[120]:


raw2.decode('windows-1250')


# In[121]:


raw2.decode('windows-1252')


# In[122]:


raw2[:3].decode('windows-1252')


# In[124]:


#convert from one text encoding to another
tmp_p='tmp.txt'
with open(path2)  as fl8:
    with open(tmp_p,'xt',encoding='windows-1252') as fl9:
        fl9.write(fl8.read())


# In[125]:


with open(tmp_p,encoding='windows-1252') as fl8:
    print(fl8.read(7))


# In[126]:


#caution note:seek method applicatble to the non binary file modes
#if the file position falls in the middle of the bytes defining a cahr as per a particular text encoding
#then subsequent reads might result in an error
with open('temp5.txt','w') as fl8:
    fl8.write('JIIïvee\n')


# In[127]:


fl8=open('temp5.txt')
fl8.read()


# In[128]:


fl8.seek(4)


# In[129]:


fl8.read(1)


# In[ ]:


############end of python built in capabilities 24-aug-2021

