import os
import requests

# Folder to store downloaded CSVs
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# Base URL and months to download
BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"
months = ["2021-01", "2021-02", "2021-03"]

for month in months:
    filename = f"yellow_tripdata_{month}.parquet"
    file_url = f"{BASE_URL}/{filename}"
    local_path = os.path.join(DATA_DIR, filename)

    print(f"Downloading {filename}...")
    response = requests.get(file_url, stream=True)
    if response.status_code == 200:
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"✅ Saved to {local_path}")
    else:
        print(f"❌ Failed to download {filename}: {response.status_code}")