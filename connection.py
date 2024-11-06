import requests

# Replace with your Heroku app URL
url = "https://peaceminusone-chatbot.herokuapp.com/"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Connected successfully!")
    elif response.status_code == 404:
        print("Connected, but endpoint not found (404). Check your app route or endpoint.")
    else:
        print(f"Connected, but received status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print("Connection failed:", e)
