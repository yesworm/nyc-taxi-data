{{ config(materialized='table') }}

SELECT
    pickup_datetime,
    dropoff_datetime,
    TIMESTAMP_DIFF(dropoff_datetime, pickup_datetime, MINUTE) AS trip_duration_mins,
    pickup_location_id,
    dropoff_location_id,
    passenger_count,
    trip_distance,
    total_amount,
    fare_amount,
    tip_amount,
    payment_type,
    is_weekend
FROM {{ ref('stg_yellow_tripdata_combined') }}
WHERE
    pickup_datetime IS NOT NULL
    AND dropoff_datetime IS NOT NULL
    AND pickup_datetime >= '2021-01-01'
    AND trip_distance > 0