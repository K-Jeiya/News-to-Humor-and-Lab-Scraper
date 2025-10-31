import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()
BASE_URL = os.getenv("BASE_URL")
LAB_IDS = os.getenv("LAB_IDS").split(",")

all_records = []

for lab_id in LAB_IDS:
    params = {"lab_id": lab_id}
    response = requests.get(BASE_URL, params=params)
    # print(f"Lab {lab_id} Status: {response.status_code}")

    if response.status_code != 200:
        # print(f"Failed to fetch lab {lab_id}")
        continue

    data = response.json()
    tests = data.get("lab_tests", [])

    # Extract required fields
    for test in tests:
        all_records.append({
            "discount": test.get("discount"),
            "discountPercentage": test.get("discountPercentage"),
            "discountedFee": test.get("discountedFee"),
            "fee": test.get("fee"),
            "id": test.get("id"),
            "lab_id": test.get("lab_id"),
            "test_name": test.get("name"),
            "test_type": test.get("type"),
            "lab_name": data.get("name")
        })

# Save to CSV
df = pd.DataFrame(all_records)
df.to_csv("labs_data.csv", index=False)
print(f"Saved {len(df)} records to labs_data.csv")