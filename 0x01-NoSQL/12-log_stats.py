#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def display_stat():
    """ provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017/')
    logs_collection = client.logs.nginx
    count = logs_collection.count_documents({})
    print("{} logs".format(count))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = logs_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))

    status_check = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))


if __name__ == "__main__":
    display_stat()
