#!/usr/bin/env python
# coding: utf-8

# ### Visualising Data with Matplotlib
# 
# The following notebook will guide you through creating plots with matplotlib. 
# 
# There are 2 types of problems in this notebook: the first type is choosing the most appropriate visualisation for data, and the second type is criticising visualisations. 
# 
# If you are stuck at any point, please ask a tutor!

# In[1]:


#Don't forget to run this cell

import numpy as np
# make the plots look good inline
# Set up Matplotlib
import matplotlib as mpl   
import matplotlib.pyplot as plt


# #### Recap
# Refer to the following section, if you need reminded of writing matplotlib code. Step of creating plots: 
# 
# * To begin plotting, you need to create figure: 
# 
#     fig = plt.figure()  #creates a blank figure
#   
# 
# * The following code can handle changing the default figure size: 
#     fig = plt.figure(figsize=(5,5))
# 
# * To draw anything, we must define axes. Each axes is a facet of a plot. It has a coordinate system which can be used to draw data.The call to create a new axis is formatted fig.add_subplot(rows, columns, index) which will create a subplot in a matrix of axes indexed by the index. The index increases column-wise, then row-wise, and starts from 1 (not 0!)
# 
#     ax = fig.add_subplot(1, 1, 1) 
#     
# * The defined axes come with a range of useful methods such as set_title, set_xlabel, etc
# 
# 
# 

# In[2]:


# a simple function, returns pulses with a shape determined by k
def pulse(x, k):
    return np.cos(x) * np.exp(np.cos(x) * k - k)

## generate some data
x = np.linspace(-np.pi, 5 * np.pi, 500)


# In[3]:


fig = plt.figure()  # create a new figure

ax = fig.add_subplot(1, 1, 1)  # create a new subplot, returning a set of axes
# note: the call is formatted fig.add_subplot(rows, columns, index)
# which will create a subplot in a matrix of plots (of the given size)
# indexed by the index. The index increases column-wise, then row-wise, and starts from *1*
# for example, we could create a 3x2 array of plots, and select the middle-left plot
# using
# plt.add_subplot(3, 2, 3)
#    --------
#   | 1 | 2 |
#   | 3 | 4 |
#   | 5 | 6 |
#   ---------


# line plot of x against f(x, k) for fixed values of k
# each subsequent plot will be a new color
# all of the plots will be overlaid on the axis
# plot(x,y) is the basic line plotting command
ax.plot(x, pulse(x, 1), label='k=1')
ax.plot(x, pulse(x, 5), label='k=5')
ax.plot(x, pulse(x, 100), label='k=100')

# label the plot 
ax.set_xlabel("Phase (radians)")  # x-axis label
ax.set_ylabel("Amplitude")  # y-axis label
ax.set_title("Pulse wave function for various $k$")  # title of plot (appears above plot)

## set the limits of the plot
# (if this is omitted, sensible autoscaling will be applied)
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(-0.25, 1.2)

# draw a dotted, semi-transparent horizontal line at the maximum possible value of the function
ax.axhline(1.0, color='k', linestyle=':', label="Maximum", alpha=0.25)

# draw an annotation directly on the plot
ax.annotate(
    "First peak",
    xy=(0, 1),
    xytext=(20, 10),
    textcoords='offset points',
    arrowprops={"arrowstyle": '->'})

# create a legend (key) for the plot, using the labels specified
# in the ax.plot() calls
ax.legend()


# ### Part A: Visualising Data
# 
# To complete those tasks successfully: 
# 
# * choose the right kind of plot (line, scatter, bar, histogram). There may be more than one right choice.
# * plot the data correctly
# * Add the necessary axes labels,etc
# * write a short caption for the data in the cell provided.

# #### Problem 1:
# * Data file: `data/cherry_trees.txt`
# * Description: Height and volume of black cherry trees  measured in an orchard.
# * Columns:
#   
#        Height (ft)  Volume (ft^3)
# 
# Note: plot your graph in **metric units**. 1 ft = 0.3048m
#        
#     

# In[4]:


#your solution goes here


# #### Problem 2:
# * Data file: `data/air_passengers.txt`
# * Description: The number of international air passengers, each month, 1949 to 1960.
# * Columns:
# 
#       year   passenger_count
# 

# In[5]:


#your solution goes here


# #### Problem 3: 
# 
# * Data file: `data/rivers.txt`
# * Description: Length of major rivers in the United States (miles)
# * Columns:
#    
#        river_length
# 
# 

# In[6]:


# your solution goes here


# #### Problem 4: Layered and Faceted Plots
# 
# * Data file `data/cake.txt`
# * Description: 
# >Data on the breakage angle of chocolate cakes made with three different
# recipes and baked at six different temperatures. The angle of breakage is affected by the recipe and temperature. The experiment was repeated 15 times (replicates).
# 
# * Columns:
# 
#         replicate(1-15)    recipe(0-2)    temp(deg F)    angle(deg)
# 
# Use this model:
# * Facet `recipes`
# * Layer `replicates`
# 
# * Colour each replicate identically, and use lowered opacity.
# 
# * As well as the layered replicates, clearly show the mean and standard deviation of the breakage angle in each facet as a line geom and a ribbon geom. Use np.mean and np.std. 
# 
# * Convert Fahrenheit to Celsius before plotting. 
# 
# * `plt.tight_layout()` will fix layout of facets. Set a super-title across all facets using `fig.suptitle()`. 
# 
# * You will need one or more `for` loops (probably) to solve this problem.
# * Use Boolean arrays to perform `group by` like operations.
# 
# The plot below illustrates how your final plot should look like. 
# 
# ![image.png](attachment:image.png)

# In[7]:


#your code goes here


# #### Problem 5: Plotting uncertainty
# 
# * Data file: `data/insects.txt`
# * Description: The counts of insects on each leaf of a plant in agricultural experimental units treated with
# different insecticides.
# * Columns:
# 
#             insect_count spray_id (0-5)
# 
# 
# * Plot the data, on three separate figures, using:
#     * A simple bar chart of the mean insect counts (grouped by spray).
#     * A barchart showing the mean counts (grouped), and half a standard deviation above and below the mean. Find a way to show this interval (hint: look at the [`plt.bar` documentation](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.bar.html)). The standard deviation of an array can be computed by `np.std(x, axis)`, just like `np.mean()`.
#     * A Box plot of the insect counts.
# 
# * Mark the ticks on the x axis using the names of the sprays.
# 
#         0 = Insecticator
#         1 = Placebo
#         2 = BuzzNoMore
#         3 = Aprotex
#         4 = DieOff
# 

# In[8]:


#your code goes here


# ### Part B: Criticising visualisations
# 
# For the plot below, identify areas that could be improved. Discuss with your tutor before proceeding to improving the plot.

# #### Problem 6: Reaction times and sleep
# Dataset: The average reaction time per day for subjects in a sleep deprivation study. On day 0 the subjects had their normal amount of sleep. Starting that night they were restricted to 3 hours of sleep per night. The observations represent the average reaction time on a series of tests given each day to each subject.
# 
# File data/sleep_study.txt
# 
# Columns
# 
#    reaction time (ms)    sleep_deprivation (days)  subject_id (id)

# In[9]:


sleep_study = np.loadtxt("data/sleep_study.txt")
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
reaction, sleep, subject = 0,1,2

# group each day
grouped =np.array([sleep_study[sleep_study[:,sleep]==i] for i in range(10)])
# take mean for each day and plot it
mean_reactions = np.mean(grouped, axis=1)[:,0] 
ax.plot(mean_reactions, np.arange(10))

# adjust axes
ax.set_xlim(0,1000)
ax.set_ylim(-2, 15)

ax.set_ylabel("Sleep deprivation")
ax.set_xlabel("Reaction time")


# In[ ]:





# In[ ]:




