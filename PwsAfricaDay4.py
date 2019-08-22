#!/usr/bin/env python
# coding: utf-8

# In[1]:


def average(l):
    n=0
    for i in l:
        n=n+i
    avrg=n/len(l)
    return(avrg)
y=[1,2,3,4,8,7]
average(y)
v=average(y)
print(v)

       #finding the average 


# In[2]:


februarydata=[[0,2,5,1,3,4,4],[1,2,3,1,3,1,4],[0,2,1,1,3,3,3],[0,2,2,1,3,4,4]]
maxweek=[]    
for i in range(len(februarydata)):
    m=max(februarydata[i])
    maxweek.append(m)
maxall=max(maxweek)
print(maxall)

                   
#finding the maximum


# In[3]:


februarydata=[[2,2,1,4,0,2,5],[0,0,0,1,0,2,3],[0,1,1,1,0,2,2],
              [0,3,4,3,3,5,4]]
count=0
for i in februarydata:
    for n in i:
        
        if n>3:
           count=count+1
print ('number of days with rainfall>3: ',count)


# In[4]:


#dryest week
w1=[2,2,1,4,0,2,5]
w2=[0,0,0,1,0,2,3]
w3=[0,1,1,1,0,2,2]
w4=[0,3,4,3,3,5,4]
n=0
for i in w1:
    n=n+i
a=n/len(w1)
print ('week1: ',a)
for i in w2:
    n=n+i
b=n/len(w2)
print ('week2: ',b)
for i in w3:
    n=n+i
c=n/len(w3)
print ('week3: ',c)
for i in w4:
    n=n+i
d=n/len(w4)
print ('week4: ',d)
if a>b and a>c and a>d:
    print('the first week is the dryest one')
    
elif b>a and b>c and b>d:
    print('the second week is the dryest one')

elif c>a and c>b and c>d:
    print('the  week 3 is the dryest one')

else:
     print('the  week 4 is the dryest one')
    


# In[5]:


#wettest week
w1=[2,2,1,4,0,2,5]
w2=[0,0,0,1,0,2,3]
w3=[0,1,1,1,0,2,2]
w4=[0,3,4,3,3,5,4]
n=0
for i in w1:
    n=n+i
a=n/len(w1)   
print ('week1: ',a)
for i in w2:
    n=n+i
b=n/len(w2)   
print ('week2: ',b)
for i in w3:
    n=n+i
c=n/len(w3)   
print ('week3: ',c)
for i in w4:
    n=n+i
d=n/len(w4)   
print ('week4: ',d)
if a<b and a<c and a<d:
    print('the first week is the wettest one')
    
elif b<a and b<c and b<d:
    print('the second week is the wettest one')

elif c<a and c<b and c<d:
    print('the  week 3 is the wettest one')

else:
     print('the  week 4 is the wettest one')
    


# In[6]:


#water used in a month

februarydata=[[2,2,1,4,0,2,5],[0,0,0,1,0,2,3],[0,1,1,1,0,2,2],
              [0,3,4,3,3,5,4]]
count=0
for i in februarydata:
    for n in i:
        if n>3:
           count=count+1

print ('water used in a month: ',count)


# In[7]:


def average(list):
    n=0
    for o in list:
        n=n+o
    avg=n/len(list)
    return avg
februarydata=[[2,2,1,4,0,2,5],[0,0,0,1,0,2,3],[0,1,1,1,0,2,2],[0,3,4,3,3,5,4]]
newlist=[] 
for i in range(len(februarydata)):
    mavg=average(februarydata[i])
    newlist.append(mavg)
print(newlist)


# In[8]:


def average(list):
    n=0
    for o in list:
        n=n+o
    avg=n/len(list)
    return avg
februarydata=[[2,2,1,4,0,2,5],[0,0,0,1,0,2,3],[0,1,1,1,0,2,2],
              [0,3,4,3,3,5,4]] 
for i in range(len(februarydata)):
    mavg =average(februarydata[i])
    mvg= average(februarydata[0])
    if mavg> mvg:
         p= mavg
         mvg=p     
         mavg = mvg 
print('this is the dryest week: ', i)    


# In[9]:


def ceasarcipher(word):
    for i in word:
                   i=word[0]
                   n=i
                   i=word[0]
    return(word[0])
                
y=['tharcissie']
x=ceasarcipher(y)
print(x)
                   
                   
                   
                   
      


# In[16]:



#students = ["Sofiat","Fionnuala","Alex","Ify","John Paul","Ben","Tom"]
#subjects = ["Algorighms and Data Structures","Java","Web AppDevelopment","Databases", "Human Computer Interaction","Information Retrieval"]


def average(list):
    n=0
    for i in list:
        n+=1
    average=n/len(list)
         if average
    return average
marks = [[56,89,70,92,67,100],[60,70,100,45,70,76],[60,95,90,85,93,45],[55,80,56,45,51,76],[78,100,65,77,91,87],[45,78,65,50,45,87],[32,50,45,67,40,80]]
a=[]
for o in range(len(marks)):
    avg=average(marks[o])
    a.append(avg)
print (a)
#for o in range(len(marks)):
   # avg=average(marks[o])
  



# In[ ]:





# In[ ]:




