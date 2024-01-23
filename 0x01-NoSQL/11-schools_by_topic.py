#!/usr/bin/env python3
""" list docs in collection """


def schools_by_topic(mongo_collection, topic):
    """ list docs in collection """
    # Find documents in the collection that have the specified topic
    schools_with_topic = mongo_collection.find({"topics": topic})

    # Convert the cursor to a list
    school_list = list(schools_with_topic)

    return school_list
