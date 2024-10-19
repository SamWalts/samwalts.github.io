#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 00:57:45 2024

@author: samuelwalters_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'SNHU1234'
        HOST = 'localhost'
        PORT = 27017
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        try:
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
            self.database = self.client['%s' % (DB)]
            self.collection = self.database['%s' % (COL)]
            print("Connection Successful")
        except Exception as e:
            print("Connection Unsuccessful")
            raise Exception(f"Error occured: {e}")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        """" Create a new document in the collection """
        if data is not None:
            insert = self.database.animals.insert_one(data)
            return True if insert.inserted_id else False
        else:
            raise Exception("Nothing to save, because data parameter is empty.")

# Create method to implement the R in CRUD.

    def read(self, query):
        """ Will return a list of the results of a query, or raise an exception if the query is empty """
        if query is not None:
            result = list(self.database.animals.find(query))
            return result if result else None
        else: 
            raise Exception("Nothing to read because the query paramater is empty.")
            
        
    def update(self, query, update_data):
        if query and update_data is not None:
            result = self.database.animals.update_many(query, {'$set': update_data})
            return result
        else:
            raise Exception("Nothing to update, because the update paremater was empty.")
            
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(remove)
                result = delete_result.raw_result
            else:
                result = "No document was found"
                return result
        else:
            raise Exception("Nothing to delete, becuase delete parameter is empty.")
