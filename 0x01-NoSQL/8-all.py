#!/usr/bin/env python3
""" list all docs in collection """


def list_all(mongo_collection):
    """ list all docs in collection """
    # get docs from collection
    docs = mongo_collection.find()
    # convert the cursor into a list
    docs_lsit = list(docs)

    return docs_lsit
