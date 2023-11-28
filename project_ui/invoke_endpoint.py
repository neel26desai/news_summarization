import requests
import json

# Endpoint URL (replace with your endpoint URL)
endpoint_url = "https://your-azure-ml-endpoint.azurewebsites.net/score"

# If the endpoint is secured with a key
api_key = "your_api_key"  # Replace this with your API key

# Prepare headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"  # Only needed if the endpoint is secured
}

# Prepare the data payload
# Replace this with the data expected by your model
data = {
    "data": [
        # Example input data
    ]
}

# Convert to JSON string
data = json.dumps(data)

# Send the request
response = requests.post(endpoint_url, headers=headers, data=data)

# Get the response
print(response.text)
