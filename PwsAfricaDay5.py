#!/usr/bin/env python
# coding: utf-8

# In[1]:


marks = [[56,89,70,92,67,100],[60,70,100,45,70,76],[60,95,90,85,93,45],[55,80,56,45,51,76],[78,100,65,77,91,87],
        [45,78,65,50,45,87],[32,50,45,67,40,80]]
students = ["Sofiat","Fionnuala","Alex","Ify","John Paul","Ben","Tom"]
subjects = ["Algorighms and Data Structures","Java","Web AppDevelopment","Databases", "Human Computer Interaction","
            Information Retrieval"]
            
            


# In[7]:


dictresults={'avg':52,'java':78,'hci':24,'db':39,'ir':66}
total=0
for subject in dictresults:
    print(dictresults[subject])
    total=total+dictresults[subject]
print (total)
average=total/len(dictresults)
print(average)


# In[16]:


chemicalElements = {'H':'Hydrogen','He':'Helium','Li':'Lithium','Be':'Beryllium','B':'Boron','C':'Carbon','N':'Nitrogen','O':'Oxygen','F':'Fluorine','Ne':'Neon'}

print(chemicalElements['C'] )
print(chemicalElements['H'] )
print(chemicalElements['B'] )
print(chemicalElements['N'] )
print(chemicalElements['F'] )
print(chemicalElements['Ne'] )

chemicalElements['Na']='sodium'
print(chemicalElements)


   # Problem 1. Without using a loop, print what element is represented
#by C,H, B, N, F, Ne. Add Sodium (Na) and Magnesium (Mg) to the
#dictionary.


# In[32]:


temperatureCountries = {'Rwanda': 29, 'Nigeria':28 , 'Kenya':23, 'Egypt':37 ,'Morocco': 41 ,'South Africa': 25, 'Mali': 33, 'Ghana':28,}

print(temperatureCountries)
temperatureCountries['congo']=1
temperatureCountries['burundi']=5
print(temperatureCountries)
temperatureCountries['Morocco']=38
temperatureCountries['Kenya']=29
temperatureCountries['South Africa']=31
print(temperatureCountries)

for degree in temperatureCountries:
    if temperatureCountries[degree]>30:
        print( degree,'is too hot, ')
    elif temperatureCountries[degree]<25:
        print( degree,'is too cold, ')
        



#Problem 2. Don’t use for loops in this question! Print the current
#recorded temperature for Nigeria, South Africa and Egypt. Add
#two countries of your choice. Change the recorded temperature for
#Morocco to 38 degrees, Kenya goes to 29 degrees, and South Africa
#increses to 31 degrees.

#Problem 3. Which countries have temperature over 30 degrees. For
#those countries print, it’s too hot. If the temperature is below 25, print
#it’s too cold.


# In[35]:


courseStudents = {'Java Programming':120, 'Django': 60, 
'Algorithms and Data structures': 58, 'Software Engineering': 70}

number=0
for student in courseStudents:
    number=number+courseStudents[student]
print('number of student doing computing: ', number)

#Problem 5. Given the course name and number of students, what’s
#the total number of students doing computing.


# In[101]:


students = {'Sofiat': [56,89,70,92,67,100], 'Fionnuala'
:[60,70,100,45,70,76],'Alex':[60,95,90,85,93,45],
'Ify': [55,80,56,45,51,76],'John Paul':[78,100,65,77,91,87],
'Ben': [45,78,65,50,45,87],'Tom':[32,50,45,67,40,80]}

def Total(dict):
    total=0
    for marks in dict:
            total=total+marks
    return(total)

def average(st):
    for a in st:
        a=Total
x=Total(students['Sofiat'])
print('Marks of Sofiat: ',x)
average=x/len(students['Sofiat'])
print('Average of Sofiat: ',average)
y=Total(students['Tom'])
print('Marks of Tom: ',y)
average=y/len(students['Tom'])

for n in student


# In[112]:


sonnet1 = ['from', 'fairest', 'creatures', 'we', 'desire', 
    'increase','that', 'thereby', 'beauty','rose', 'might',
    'never', 'die','but','as', 'the', 'riper', 'should', 
     'by','time', 'decease','his', 'tender', 'heir','cruel' 
     'might', 'bear', 'his', 'memory','but','thou', 
     'contracted', 'to','thine', 'own', 'bright','eyes',
     'feed','thy','light','flame', 'with','self-substantial',
   'fuel','making','a','famine','where', 'abundance','lies',
     'thyself','thy','foe', 'thy', 'sweet', 'self', ]
dict={}
for a in sonnet1:
    count=1
    if a in sonnet1:
        count+=1
    dict.update({a:count})
print(dict)

#Problem 7. Count the word frequencies in this sentence and store it
#in a dictionary


# In[116]:


countriesDict = {'Zimbabwe': {'capital': 'Harare', 'population': 16,'neighbours': ['South Africa', 'Botswana', 'Zambia', 'Mozambique'], 'GDP': 41},                                                                   
                 'Rwanda':{'capital':'Kigali','population': 11, 'neighbours':['DRC','Uganda', 'Tanzania', 'Burundi'],'GDP': 30}, 
                 'Nigeria': {'capital':'Abuja', 'population': 200, 'neighbours': ['Cameroon','Benin', 'Chad', 'Niger'], 'GDP':1221},
                 'Uganda': {'capital': 'Kampala', 'population':41, 'neighbours':['Rwanda', 'Kenya','Tanzania','Sudan','DRC'],'GDP': 102}, 
                 'Kenya':{'capital': 'Nairobi', 'population': 49,'neighbours': ['Tanzania', 'Uganda', 'Sudan', 'Somalia', 'Ethiopia'], 'GDP':190 } }

def find(my_dict,my_key,my_val):
     for country in countriesDict:
        if country == my_key:
               for mk,val in countriesDict[country].items():
                    if mk == my_val:
                        return(country,mk,val)
def change(my_dict,my_key,my_val,new):
        for country in countriesDict:
            if country == my_key:
                for mk,val in countriesDict[country].items():
                    if mk == my_val:
                        val==new
                        return(country,mk,val)
        print(find(countriesDict,'Rwanda','GDP'))
        print(find(countriesDict,'Zimbabwe','capital'))
        print(find(countriesDict,'Uganda','neighbours'))
        print(find(countriesDict,'Rwanda','population'))
        new=int(input("Updating Rwanda's population:")
        print(change(countriesDict,'Rwanda','population',100))
  


# In[ ]:




