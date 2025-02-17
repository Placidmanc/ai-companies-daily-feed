import requests
import json

# Define API endpoint
url = "https://api.thecompaniesapi.com/v2/companies"
headers = {
    "Authorization": "Basic IcoQtVTxF1ygEUlI4tJpZR5cGmmJRbVk"
}

# Make the GET request
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Convert response to JSON
    data = response.json()
    
    # Save JSON file
    with open("ai_companies.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    print("JSON file generated successfully.")
else:
    # Print the error message
    print(f"Error: {response.status_code} - {response.text}")
