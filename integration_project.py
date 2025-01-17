import requests
from requests.exceptions import RequestException, Timeout

# Function to handle GET requests
def fetch_data(url, params=None, retries=3, timeout=10):
    #fetches data 
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, params=params, timeout=timeout)
            response.raise_for_status()  # Raise an error for HTTP errors (4xx, 5xx)

            # Attempt to parse JSON response
            try:
                return response.json()
            except ValueError:
                # Handle cases where response is not JSON
                print("Response is not in JSON format.")
                return {"error": "Non-JSON response received."}
        
        except Timeout:
            print(f"Attempt {attempt + 1}: Request timed out. Retrying...")
        except RequestException as e:
            print(f"Attempt {attempt + 1}: Request failed. Error: {e}")
            break
        
        attempt += 1

    return {"error": "Max retries reached or an error occurred."}


# Function to print the API response in a user-friendly way
def print_api_response(data):
    
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("Response data:", data)


def main():
    # Define the URL of the API endpoints
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    
    # Optional parameters for the API request (if needed)
    params = {'userId': 1}
    
    print("Fetching data from the API...")
    
    # Fetch data from the API
    data = fetch_data(api_url, params=params)
    
    if "error" not in data:
        print("\nAPI Response Data:")
        print_api_response(data)
    else:
        print("\nError:", data["error"])


if __name__ == "__main__":
    main()
