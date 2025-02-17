import json
import requests
from datetime import datetime

# Define your data source
def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"  # Public API example
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}

# Transform data into a structured format
def create_json():
    data = fetch_data()
    structured_data = {
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "events": data.get("results", [])
    }

    # Save JSON file
    with open("daily_events.json", "w") as f:
        json.dump(structured_data, f, indent=4)

    print("JSON file generated successfully.")

if __name__ == "__main__":
    create_json()
