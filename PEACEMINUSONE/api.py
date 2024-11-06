import requests

# Replace with your actual API URL
API_URL = "https://api.peaceminusone.com/"

def add_user_to_group(user_id, group_id):
    """Function to add a user to a group using the PEACEMINUSONE API"""
    endpoint = f"{API_URL}/add_user"
    payload = {"user_id": user_id, "group_id": group_id}
    response = requests.post(endpoint, json=payload)
    if response.status_code == 200:
        return "User added successfully."
    else:
        return "Failed to add user."

def login_user(user_id):
    """Function to log a user into the PEACEMINUSONE system"""
    endpoint = f"{API_URL}/login"
    payload = {"user_id": user_id}
    response = requests.post(endpoint, json=payload)
    if response.status_code == 200:
        return "Login successful."
    else:
        return "Login failed."
