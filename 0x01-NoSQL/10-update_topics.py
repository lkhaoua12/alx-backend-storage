#!/usr/bin/env python3
""" update docs in collection """


def update_topics(mongo_collection, name, topics):
    """ update docs in collection """

    # insert new doc and retrive it id
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

    return result.modified_count
