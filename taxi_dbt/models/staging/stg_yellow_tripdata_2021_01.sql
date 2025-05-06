{{ config(materialized='view') }}

SELECT
    -- Rename and clean column names
    vendorid AS vendor_id,
    tpep_pickup_datetime AS pickup_datetime,
    tpep_dropoff_datetime AS dropoff_datetime,
    passenger_count,
    trip_distance,
    ratecodeid AS rate_code_id,
    store_and_fwd_flag,
    PULocationID AS pickup_location_id,
    DOLocationID AS dropoff_location_id,
    payment_type,
    fare_amount,
    extra,
    mta_tax,
    tip_amount,
    tolls_amount,
    improvement_surcharge,
    total_amount,
    congestion_surcharge
FROM {{ source('nyc_taxi_raw', 'yellow_tripdata_2021_01') }}