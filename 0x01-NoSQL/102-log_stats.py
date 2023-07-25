#!/usr/bin/env python3
'''task 12 module
Provides some stats about Nginx logs stored in MongoDB
'''


from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print('{} logs'.format(collection.count_documents({})))
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))

    status_checks_count = len(list(
        collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))
