import os
import requests
import json
from dotenv import load_dotenv

load_dotenv() 

API_KEY = os.getenv("AI_API_KEY")  # Get API key from environment variable
API_URL = "https://api.thecompaniesapi.com/v2/companies"

if not API_KEY:
    raise ValueError("API_KEY is missing. Set it as an environment variable.")

def fetch_data():
    headers = {"Authorization": f"Basic {API_KEY}"}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def save_json(data):
    with open("ai_companies.json", "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    try:
        data = fetch_data()
        save_json(data)
        print("Data fetched and saved successfully.")
    except Exception as e:
        print(f"Error: {e}")
