#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#PROJECT0:- BY CONNECTING MONGODB TO PYTHON USING PYMONGO WITH MONGODBCOMPASS
#DESCRIPTION:- THE PROJECT SHOWS THE DATABSE OF MEAL_INFORMATON ORDERS FROM DIFFERENT REGIONS ,THE RECORDS OF EACH MEAL_ID WHICH HAS OREDERED 
#FIELDS:- MEAL_ID,CATEGORY,BEVERAGES,CUISINE.


# In[2]:


meal_info=[{"meal_id":1885,"category":"Beverages","cuisine":"Thai"},{"meal_id":1993,"category":"Beverages","cuisine":"Thai"},{"meal_id":2539,"category":"Beverages","cuisine":"Thai"},{"meal_id":1248,"category":"Beverages","cuisine":"Indian"},{"meal_id":2631,"category":"Beverages","cuisine":"Indian"},{"meal_id":1311,"category":"Extras","cuisine":"Thai"},{"meal_id":1062,"category":"Beverages","cuisine":"Italian"},{"meal_id":1778,"category":"Beverages","cuisine":"Italian"},{"meal_id":1803,"category":"Extras","cuisine":"Thai"},{"meal_id":1198,"category":"Extras","cuisine":"Thai"},{"meal_id":2707,"category":"Beverages","cuisine":"Italian"},{"meal_id":1847,"category":"Soup","cuisine":"Thai"},{"meal_id":1438,"category":"Soup","cuisine":"Thai"},{"meal_id":2494,"category":"Soup","cuisine":"Thai"},{"meal_id":2760,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":2490,"category":"Salad","cuisine":"Italian"},{"meal_id":1109,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":2290,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":1525,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":2704,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":1878,"category":"Starters","cuisine":"Thai"},{"meal_id":2640,"category":"Starters","cuisine":"Thai"},{"meal_id":2577,"category":"Starters","cuisine":"Thai"},{"meal_id":1754,"category":"Sandwich","cuisine":"Italian"},{"meal_id":1971,"category":"Sandwich","cuisine":"Italian"},{"meal_id":2306,"category":"Pasta","cuisine":"Italian"},{"meal_id":2139,"category":"Beverages","cuisine":"Indian"},{"meal_id":2826,"category":"Sandwich","cuisine":"Italian"},{"meal_id":2664,"category":"Salad","cuisine":"Italian"},{"meal_id":2569,"category":"Salad","cuisine":"Italian"},{"meal_id":1230,"category":"Beverages","cuisine":"Continental"},{"meal_id":1207,"category":"Beverages","cuisine":"Continental"},{"meal_id":2322,"category":"Beverages","cuisine":"Continental"},{"meal_id":2492,"category":"Desert","cuisine":"Indian"},{"meal_id":1216,"category":"Pasta","cuisine":"Italian"},{"meal_id":1727,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":1902,"category":"Biryani","cuisine":"Indian"},{"meal_id":1247,"category":"Biryani","cuisine":"Indian"},{"meal_id":2304,"category":"Desert","cuisine":"Indian"},{"meal_id":1543,"category":"Desert","cuisine":"Indian"},{"meal_id":1770,"category":"Biryani","cuisine":"Indian"},{"meal_id":2126,"category":"Pasta","cuisine":"Italian"},{"meal_id":1558,"category":"Pizza","cuisine":"Continental"},{"meal_id":2581,"category":"Pizza","cuisine":"Continental"},{"meal_id":1962,"category":"Pizza","cuisine":"Continental"},{"meal_id":1571,"category":"Fish","cuisine":"Continental"},{"meal_id":2956,"category":"Fish","cuisine":"Continental"},{"meal_id":2104,"category":"Fish","cuisine":"Continental"},{"meal_id":2444,"category":"Seafood","cuisine":"Continental"},{"meal_id":2867,"category":"Seafood","cuisine":"Continental"},{"meal_id":1445,"category":"Seafood","cuisine":"Continental"}]


# In[3]:


#importing the packages
import pymongo 
from pymongo import MongoClient


# In[4]:


#connecting with Cilent Mongo
Client=pymongo.MongoClient('localhost',27017)


# In[5]:


#creating a database
Database=Client["PROJECT_0"]


# In[6]:


#creating the Collection
Collection=Database["Meal_Information"]


# In[16]:


# FOR INSERTING MANY RECORDS
res=Collection.insert_many(meal_info)
for i in res:
    print(i)


# In[17]:


#inserting_one_data
insrt={'meal_id':1010,'category':"frenchfries","cuisine":"Indian"}
Result=Collection.insert_one(insrt)
res=Collection.find()
for i in res:
    print(i)


# In[18]:


inserted_ids_value=res.inserted_ids
for i in inserted_ids_value:
    print(i)


# In[11]:


#finding the meal_id
Collection.find_one({'meal_id':1010})


# In[19]:


#deleting one record
Collection.delete_one({'meal_id':1010})


# In[9]:


#displaying limit of the database upto 3
for meal_info in Collection.find().limit(3):
   print(meal_info)


# In[21]:


#sorting in ascending order
res=Collection.find().sort("_id",1)
for i in res:
    print(i)


# In[10]:


Collection.find()


# In[11]:


#update_one
print("Documents in the collection: ")
for meal_info in Collection.find():
    print(meal_info)
Collection.update_one({"meal_id":"2539"},{"$set":{"category":"pure-veg"}})


# In[22]:


# sorting the data in descending order
res=Collection.find().sort("_id",-1)
for i in res:
    print(i)


# In[ ]:


#update_many
print("Documents in the collection: ")
for meal_info in Collection.find():
    print(meal_info)
Collection.update_many({},{"$set":{"category":"PURE_VEG"}})


# In[23]:


#finding all the record
res=Collection.find()
for i in res:
    print(i)


# In[ ]:


meal_info=[{"meal_id": "1067", "category": "seafood", "cuisine": "cintinential"},
           {"meal_id": "15167", "category": "thai", "cuisine": "indian"},
           {"meal_id": "17867", "category": "veg", "cuisine": "indian"}]


# In[30]:


# finding one record
res=Collection.find({"_id":1067,"category":"seafood"})
for i in res:
    print(i)


# In[22]:


Collection.find()


# In[14]:


#printing  all the data 
res=Collection.find()
for i in res:
    print(i)


# In[ ]:





# In[13]:


#deleting one record
Collection.delete_one({"meal_id" : "2581"})


# In[12]:


# finding that deleted record
Collection.find({"meal_id":2581})


# In[32]:


#deleting many records
Collection.delete_many({})


# In[ ]:




