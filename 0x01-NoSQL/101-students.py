#!/usr/bin/env python3
""" Task 14 module """


def top_students(mongo_collection):
    '''Returns all students sorted by average score
    '''
    pipe = [
        {
            '$project': {
                'name': '$name',
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]

    return mongo_collection.aggregate(pipe)
