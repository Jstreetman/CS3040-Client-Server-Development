# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
        # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception:
                return False
        else:
            return False

    # Create method to implement the R in CRUD.
        # Read method to implement the R in CRUD.
    def read(self, query):
        """Query animal documents and return the matching records as a list."""

        if query is not None:
            try:
                # find() returns a MongoDB cursor, so convert the
                # cursor into a list before returning the results.
                cursor = self.collection.find(query)
                return list(cursor)

            except Exception as error:
                # Print the actual MongoDB error so problems with
                # authentication or the query can be identified.
                print("Error reading from MongoDB:", error)
                return []

        else:
            return []
        
    # Update method to implement the U in CRUD.
    def update(self, query, new_data):
        """Update matching animal records and return the number of records changed."""
        
        # Make sure both the search query and new data were provided.
        if query is not None and new_data is not None:
            try:
                # Find all records that match the query and update them
                # with the new values provided.
                result = self.collection.update_many(
                    query,
                    {"$set": new_data}
                )
                
                # Return how many animal records were actually changed.
                return result.modified_count
            
            # If MongoDB cannot complete the update, return 0.
            except Exception:
                return 0
        else:
            return 0


    # Delete method to implement the D in CRUD.
    def delete(self, query):
        """Delete matching animal records and return the number removed."""
        
        # Make sure a search query was provided before trying to delete anything.
        if query is not None:
            try:
                # Find all animal records matching the query and remove them.
                result = self.collection.delete_many(query)
                
                # Return the number of records that were removed.
                return result.deleted_count
            
            # If MongoDB cannot complete the delete operation, return 0.
            except Exception:
                return 0
        else:
            return 0