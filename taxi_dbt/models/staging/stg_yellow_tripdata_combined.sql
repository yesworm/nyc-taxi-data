{{ config(materialized='view') }}

WITH combined AS (

    SELECT * FROM {{ ref('stg_yellow_tripdata_2021_01') }}
    UNION ALL
    SELECT * FROM {{ ref('stg_yellow_tripdata_2021_02') }}
    UNION ALL
    SELECT * FROM {{ ref('stg_yellow_tripdata_2021_03') }}

)

SELECT
    *,
    TIMESTAMP_DIFF(dropoff_datetime, pickup_datetime, MINUTE) AS trip_duration_mins,
    EXTRACT(DAYOFWEEK FROM pickup_datetime) AS pickup_day_of_week,
    CASE 
        WHEN EXTRACT(DAYOFWEEK FROM pickup_datetime) IN (1,7) THEN TRUE
        ELSE FALSE
    END AS is_weekend
FROM combined