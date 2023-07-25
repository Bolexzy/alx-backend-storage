#!/usr/bin/env python3
'''task 12 module
Provides some stats about Nginx logs stored in MongoDB
'''


from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print(f'{collection.estimated_document_count()} logs')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')

    for req in methods:
        print('\tmethods {}: {}'.format(req,
              collection.count_documents({'method': req})))

    print('{} status check'.format(collection.count_documents(
          {'method': 'GET', 'path': '/status'})))
