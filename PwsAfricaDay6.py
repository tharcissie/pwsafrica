#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # !!! you have first to define np always!!!

x=np.array([1,2,3])
z=x
x[0]=0
print(x)
print(z)


# In[2]:



x=np.array([1,2,3])
y=np.array(x)
z=x.copy()
x[0]=0
print(x)
print(y)
print(z)


# In[3]:


nums=[3,7,9,232]
print(nums[-1])
print(nums[2])
x=np.arange(20)
print(x)
print(x[-1:])
print(x[0])


# In[4]:




x=np.zeros([2,5])
print(x)

#matrix of all zeros


# In[5]:


x=np.ones([3,4,5])
print(x)

#1D array from 0 to 50 stepping by 2


# In[6]:


x=np.arange(0,51,2)
print(x)

#or

x=np.arange(0,51)
print(x[::2])

#1D array from 0 to 50 stepping by 2


# In[7]:


x=np.random.normal(200)
print(x)


# In[8]:


x=np.empty((2,3))
print(x)
x.fill(8)
print(x)

#priting an empty matrix and fill it with a number


# In[9]:


x=np.full((2,3),2)
print(x)

# Create a constant array


# In[10]:


x=np.full((2),np.pi)
print(x)


#a 2 element vector, with all elements equal to np.pi


# In[11]:


a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 = a[1, :]  
print(row_r1)
row_r2 = a[1:2, :]
print(row_r2)
print(a.shape)

#we can also access column

col_r1=a[:,1]
print(col_r1)
col_r1=a[:,2]
print(col_r1)


# In[12]:


x=np.random.normal(0,1,200)
print(x)

#an 200 element array, random numbers normally distributed with
#mean 0 and standard deviation 1


# In[13]:


z=np.linspace(-1,1,3)
print(z)

#an array of evenly spaced numbers between -1 and 1 
#number btn -1 and 1 and we want only 3 numbers 


# In[14]:


array1=np.arange(2,6)
array2=np.arange(2,6)
print(array1)
f=np.vstack((array1,array2))
g=np.hstack((array1,array2))
print(f)
print(g)

#create two 1D arrays of the same length and stack them (vertically
#and then horizontally)


# In[15]:


#Problem 2. Snails dataset Inside the zip file, you’ve downloaded,
#you can find the snail data. Groups of 20 snails were held for periods
#of 1, 2, 3 or 4 weeks in carefully controlled conditions of temperature
#and relative humidity. The two species of snails are labelled as 0
#and 1. At the end of the exposure time the snails were tested to see if
#they had survived.
#Data format: a 2D array with six columns: species(0 or 1), exposure(
#weeks), humidity, temperature, ndeaths, nsnails (initial number
#of snails in the experiment).
#Your tasks for this problem:


# In[16]:



#Read the data. Note: don’t parse the file yourself, use numpy

file=np.loadtxt('snails.txt')
file


# In[17]:



print(file[-1][3])

#temperature of the last entry


# In[18]:


print(file[5][2])

#humidity of the 5th entry


# In[19]:


print(file[:,1:3])                                                           

#get the 2nd and the 3 column


# In[20]:


print(file[0:5])

#retrieve the first 5 rows


# In[21]:


x=np.sum(file[:,4])
print(x)

#total number of deaths


# In[22]:


x=np.sum(file[:,5])
print(x)

#total number of snails that survived the experiment


# In[23]:


x=np.max(file[:,3])
print(x)

#max temperature


# In[24]:


x=np.mean(file[:,2])
print(x)

#mean humidity


# In[25]:


x=np.average(file[:,4])
print(x)

#average death rate


# In[32]:


# import matplotlib as mpl
import math as m
get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt
x=np.array([1,2,8,4])
y=np.array([1,2,3,4])
plt.plot(x,y,'.',c='green')


# In[55]:


import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot([0,1,2,3,4,5],[0,2,4,6,7,9],'*',x,y,'.')
x=np.arange(1,5)
y=x**2
plt.xlabel('height')
plt.ylabel('width')
plt.title('My First MatPlot')
plt.show()


# In[70]:




ones = (file[file[:,0]==1])
zeros = (file[file[:,0]==0])
print(ones)
print()
print(zeros)

#Split the snails in 2 arrays based on their species (hint: use Boolean
#indexing)


# In[78]:



y=ones[:,4]
z=np.mean(zeros[:,4])
x=np.mean(y)
print(x)
print(z)

#Which group of snails has the highest average death rate?


# In[82]:


x=np.sum(file[:,5])
print(x)
z=np.sum(file[:,4])
print(z)
surved=x-z
print(surved)

#What are the optimum living conditions (temperature and humidity)
#for snails? Consider only snails kept for the full duration of
#the experiment.


# In[ ]:




