#!/usr/bin/env python
# coding: utf-8

# In[55]:


with open("SS2_counts.csv", 'r') as f:
    data = f.readline()

text=data.strip()
text2=text.split(',')

text2
len(text2)


# In[ ]:





# In[72]:


from io import StringIO
import numpy as np
data = np.loadtxt("SS2_counts.csv", delimiter=',', 
                  usecols= np.arange(1,len(text2)),skiprows=1)


# In[69]:


data.shape


# In[74]:


data


# In[76]:


# number of zeros
num=(data==0).sum()
num


# In[77]:


np.count_nonzero(data)


# In[79]:


data[:,0]


# In[81]:


data.shape[1]


# In[ ]:


# lst=[]
# for i in data.shape[1]:
#     np.count_nonzero(data.shape[i])


# In[90]:


#total count per cells
count_cells=np.sum(data,axis=0)
count_cells


# In[91]:


#number of non zeros per cells
count_nonzero_cells=np.count_nonzero(data,axis=0)
count_nonzero_cells


# In[ ]:





# In[92]:


len(count_cells)


# In[93]:


len(count_nonzero_cells)


# In[106]:


#scatter plot
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
x=count_cells

y=count_nonzero_cells




plt.scatter(x,y,cmap='viridis',alpha=0.2)
plt.title('total count vs number of expressed genes')
plt.xlabel('total count')
plt.ylabel('number of expressed genes')


# In[ ]:




