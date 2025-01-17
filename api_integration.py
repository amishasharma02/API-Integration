import requests

# Define the URL of the API endpoint
api_url = "https://jsonplaceholder.typicode.com/posts/1"

# Send a GET request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()
    
    # Print the result (the data from the API)
    print("API Response Data:")
    print(data)
else:
    # Print an error message if the request failed
    print(f"Failed to retrieve data. Status code: {response.status_code}")
