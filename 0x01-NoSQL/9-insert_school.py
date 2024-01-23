#!/usr/bin/env python3
""" insert new doc in collection """


def insert_school(mongo_collection, **kwargs):
    """ insert new doc in collection """

    # insert new doc and retrive it id
    new_docs_id = mongo_collection.insert_one(kwargs).inserted_id

    return new_docs_id
