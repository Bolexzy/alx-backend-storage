#!/usr/bin/env python3
'''Defines a function that lists all documents in a collection
'''
from pymongo import MongoClient


def list_all(mongo_collection):
    '''Return a list of all documents in a collection
    '''
    return [doc for doc in mongo_collection.find()]
