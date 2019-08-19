#!/usr/bin/env python
# coding: utf-8

# # FUNCTION

# In[23]:


# function is away to achieve the modularity and reusablity of the code.
def c(): # def is a keyword. # fasih is a variable # () braces 
    c = "shahbaz"    # parameter less function
    print(c)        
c()


# In[28]:


a = "shahbaz"  # variable can be assighned before def
def c(a):     # this is the another way of definition assighnemnt 
    print(a)  
c(a)


# In[36]:


def c(a): 
    print(a)      # this is called passing information
c("shahbaz")       # variable can be assighned after def


# In[38]:


def c(a,b):                 
    print(a + " and" + b)      
c(b = " shahbaz" , a= " tehseen")        # this is the keyword arguments method


# In[39]:


def c(a,b):                 
    print(a + " and" + b)      
c(" shahbaz" , " tehseen", "fasih")  


# In[48]:


def pizza(size, offers, time, *cat):
    print(f"Your pizza size is {size},  the offer is {offers} time is {time} and the category is {cat}")
    
pizza(12 ,"ramoffers", "30mins","chkfaj", "olive")


# In[51]:


def couple(husband_name, wife_name):
    print(f"The name of the couple are {husband_name} and {wife_name}.")

couple("Muhammad Shahbaz","Mrs. Shahbaz")


# In[52]:


def cake(size, type,*toppings):
    print(f"The size of your cake is {size} inches, the type is {type} cake and toppings are {toppings}. Thanks for using our service.")
    
cake(16, "strawberry", "cherries", "chocos", "crunches", "pineapples crushes")


# In[ ]:




