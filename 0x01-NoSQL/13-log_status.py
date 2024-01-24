#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.logs
collection = db.nginx

# Get the total number of logs
total_logs = collection.count_documents({})

# Get the number of logs for each method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents(
    {"method": method}) for method in methods}

# Get the number of logs with method=GET and path=/status
status_check_count = collection.count_documents(
    {"method": "GET", "path": "/status"})

# Display the results
print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check_count} status check")
