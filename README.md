# PROBLEM DESCRIPTION 
###  Meal delivery system in this project mongodb used as the database 


# REQUIREMENT AND TECH STACK
### 1.Python,
### 2.data in json file /documnet file
### 3.Jupyter Notebook
### 4. Mongodb

# MEAL_DELIVERY_SYSTEM
###   By Manaswini

## Service Function
### Install package PYMONGO
### Creating the Database connection
#### Creating the connection with collection meal_info.json file with source code.


## PYMONGO QUERIES
### use mongodb for no sql database and used pymongo for connecting nosql with python

### Creating a Database
  #### database=client["database_name"] 
 

### Inserting many documents in collection
   #### collection.insert_many(info_data)
 
 ### inserting_one_data
   #### result=collection.insert_one(data1) 
 
 ### Finding the meal_id
   #### collection.find_one({'meal_id':1010}) 
   
 ### Deleting one record
   #### Collection.delete_one({"id":123}) 

### Displaying limit of the database upto limit
   ####  COLLECTION.FIND().LIMIT(6) 
 
 ### Inserted_ids to the documents
#### res=collection.insert_many(info)
#### Inserted_IDs=res.inserted_ids
#### for i in Inserted_IDs:
####    print(i)
 
### Sorting the data in ascending order, descending order  
  #### collection.find().sort() 
  #### collection.find.sort("meal_id",-1)

### Update_one
  #### collection.update_one({"_id":123},{"$set":{"name":"manas"})
  
### Update many
 #### collection.update_many({},{"$set":{"name":"manas"})

### Delete many
#### collection.delete_many({"id":1253588,"id":1747636,})
#### collection.delete_many( {"cuisine": {"$regex": "^S"}})
