#!/usr/bin/env python
# coding: utf-8

# In[4]:


d = {}


# In[5]:


type(d)


# In[6]:


d1 = {'key':"vipin"}


# In[7]:


d1


# In[8]:


d2 = {'name':"vipin","email":"ss@gmail.com","number":334455}


# In[1]:


d3 = {234 : "sudh", '-wer': "kumar",True :24234}


# In[2]:


d3


# In[5]:


d3[234]


# In[4]:


d3


# In[6]:


d3[True]


# In[7]:


d3[1]


# In[8]:


d4 = {'name':"sudh", 'mail_id' :"ss@gmail.com" ,"name":"sudhanshu"}


# In[9]:


d4['name']


# In[12]:


d4["name"]


# In[13]:


d5 = {"company" : "peskills" , "course" :["web dev" , "data science","java with dsa system design"]}


# In[14]:


d5


# In[16]:


d5['course'][2]


# In[21]:


d6 = {"number" : [2,34,3,34,34] , "assignment" :(1,2,3,4,5,6) , "lunch_date":{28,12,14} ,"class_time":{"web_dev": 8 , "data science masters" : 8 ,"java with dsa and system design":7}}


# In[22]:


d6


# In[23]:


d6['class_time']['java with dsa and system design']


# In[24]:


d6['mentor'] = ["sudhanshu","krish","anurag" , "hayder"]


# In[25]:


d6


# In[26]:


del d6['number']


# In[27]:


d6


# In[29]:


list(d6.keys())


# In[30]:


list(d6.values())


# In[31]:


list(d6.items())


# In[32]:


d6.pop('assignment')


# In[33]:


d6


# In[35]:


d6.pop('class_time')


# In[36]:


d6


# In[ ]:


marks = int(input ("center your marks"))
if marks >= 80:
    print("you will be a part of A0 batch")
elif marks>= 60 and marks< 80:
    print("you will be a part of A1 batch")
elif marks >= 40 and marks <60 :
    print("you will be a part of A2 batch")
else :
    print("you will be a a part of A3 batch")
    


# In[38]:


10 >= 80


# In[ ]:


marks = int(input("center your marks"))


# In[ ]:


price = int(input("enter price"))
if price > 1000:
    print("i will not purchase")
else :
    print("i will purchase")


# In[ ]:


price = int(input("enter price"))
if price > 1000:
    print("i will not purchase")
    if price >5000:
        print("this is too much")


# In[ ]:


l = [1,2,3,3,4,5,6,7,8]


# In[ ]:


l[0] +1


# In[ ]:





# In[2]:


l = [1,2,3,3,4,5,6,7,8]


# In[3]:


l[0] +1


# l1 = [

# In[4]:


l1 = []


# In[5]:


l1.append(l[0] +1)


# In[6]:


l1


# In[7]:


l


# In[12]:


l1 = []
for i in l :
    print(i+1)
    l1.append(i+1)
l1


# In[13]:


l = ["sudh","kumar","pwskills","course"]


# In[16]:


l1 = []
for i in l :
    print(i)
    l1.append(i.upper())


# In[17]:


l1


# In[23]:


l = [1,2,3,4,4,"sudh","kumar",324.24,456,"abc"]


# In[25]:


l1_num = []
l2_str = []
for i in l :
    if type(i) == int or type(i) == float :
        l1_num.append(i)
    else:
        l2_str.append(i)
    


# In[22]:


l1_num


# In[26]:


l2_str


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




