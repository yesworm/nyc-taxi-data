import os
from google.cloud import bigquery
import pandas as pd

# Path to service account key
GCP_KEY_PATH = os.path.join(os.path.dirname(__file__), '..', 'gcp-key.json')

# GCP project and dataset
PROJECT_ID = "nyc-taxi-analytics-459001"  
DATASET_ID = "nyc_taxi_raw"

# Parquet data folder
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

# Authenticate client
client = bigquery.Client.from_service_account_json(GCP_KEY_PATH)

# Check and create dataset if not exists
def create_dataset_if_not_exists():
    dataset_ref = bigquery.Dataset(f"{PROJECT_ID}.{DATASET_ID}")
    try:
        client.get_dataset(dataset_ref)
        print(f"Dataset {DATASET_ID} already exists.")
    except Exception:
        print(f"Dataset {DATASET_ID} does not exist. Creating now...")
        client.create_dataset(dataset_ref)
        print(f"✅ Dataset {DATASET_ID} created.")

def upload_parquet_to_bq(parquet_file):
    # Extract month from filename
    filename = os.path.basename(parquet_file)
    table_name = filename.replace(".parquet", "").replace("-", "_")
    table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}"

    # Load parquet into dataframe
    df = pd.read_parquet(parquet_file)

    print(f"Uploading {filename} to {table_id}...")

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()  # Wait for job to complete

    print(f"✅ Uploaded {df.shape[0]} rows to {table_id}")

if __name__ == "__main__":
    # Ensure dataset exists
    create_dataset_if_not_exists()

    # Upload all parquet files
    for file in os.listdir(DATA_DIR):
        if file.endswith(".parquet"):
            parquet_path = os.path.join(DATA_DIR, file)
            upload_parquet_to_bq(parquet_path)