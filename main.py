GRAPH_ID = "graph1"

import requests
from datetime import datetime
import os
APP_USERNAME = os.environ.get("APP_USERNAME")
print(APP_USERNAME)
APP_TOKEN = os.environ.get("APP_TOKEN")
print(APP_TOKEN)
"""
This script interacts with the Pixela API to track coding habits by creating a graph and posting data on a daily basis. 
The user can record the minutes spent coding, update the value for a specific day, or delete an entry.

Steps:
1. Create a user account (already done, hence commented out).
2. Create a graph to track the habit.
3. Post a value (minutes spent coding) to the graph.
4. Update the value for a specific date (commented for reference).
5. Delete an entry from the graph (commented for reference).

API Documentation: https://docs.pixe.la/
"""

# Pixela API endpoint for user creation and graph management
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token":APP_TOKEN, # Token generated by the user for authentication
    "username":APP_USERNAME, # # Username created by the user
    "agreeTermsOfService":"yes", # Agreement to terms of service
    "notMinor":"yes", # Confirmation that the user is not a minor
}
#-----------Step1-------------------
#  Step 1: Create user account (already done, so commented out)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Step 2: Create a graph to track coding time
graph_endpoint = f"{pixela_endpoint}/{APP_USERNAME}/graphs"
# Configuration for the graph, specifying units and type of data being tracked
graph_config = {
    "id":GRAPH_ID,
    "name":"Coding",
    "unit":"minutes",
    "type":"int",
    "color":"shibafu",

}
# Headers for authentication using the user’s token
headers ={
    "X-USER-TOKEN":APP_TOKEN
}

# Step 2 (Create Graph) Request (commented as the graph may already exist)
# response =requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

# Step 3: Access the created graph using the following URL:
#--(https://pixe.la/v1/users/a-know/graphs/test-graph)
##---https://pixe.la/v1/users/dimple12345/graphs/graph1  - for Coding Tracker


# Step 4: Post a value (minutes spent coding) to the graph
pixela_creation_endpoint = f"{pixela_endpoint}/{APP_USERNAME}/graphs/{GRAPH_ID}"
today =datetime.now()
formatted_date = today.strftime("%Y%m%d")

habit_input ={
    "date": formatted_date, # Date in YYYYMMDD format
    "quantity":input("How Long did you do coding today?(Enter in Minutes): ")

}

# Post the habit data to the Pixela API
response = requests.post(url=pixela_creation_endpoint,json=habit_input,headers=headers)
print(response.text)


# Step 5: Update the value for a specific day (PUT operation)

# URL for updating a specific date entry in the graph
pixela_put_endpoint =f"{pixela_endpoint}/{APP_USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"

# Data to update the quantity (minutes spent coding) for the specific date
update_input = {
    "quantity":"100" # New value to replace the existing one (in this case, 100 minutes)
}

# PUT request to update the entry (commented for reference)
# response = requests.put(url=pixela_put_endpoint,json=update_input,headers=headers)
# print(response.text)

# Step 6: Delete the value for a specific day (DELETE operation)

# URL to delete the specific date entry from the graph
# pixela_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
# response = requests.delete(url=pixela_delete_endpoint,headers=headers)
# print(response.text)