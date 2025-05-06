# NYC Taxi Trip Analytics

An end-to-end analytics engineering project processing NYC Yellow Taxi trip data (Jan - Mar 2021), modeled using dbt and visualized in Looker Studio.

## 📦 Business Use Case

This dashboard helps NYC taxi fleet operators, city planners, and financial analysts answer key business questions:

- What are the busiest days and times for pickups?
- How does trip duration vary across weekdays and weekends?
- What payment methods are most common among riders?
- Which pickup locations generate the most rides?
- How do tip amounts correlate with fare amounts?

The dashboard allows for interactive exploration of trends, demand patterns, and rider behavior.

## 🛠️ Tech Stack

- **Google BigQuery**: Cloud data warehouse to store raw and processed data
- **dbt**: Data transformation and modeling (staging + marts)
- **Looker Studio**: Interactive business dashboard
- **Python (optional)**: For initial data ingestion
- **GitHub**: Version control and portfolio showcase

## 📈 Data Pipeline

1. **Raw Data** → NYC Yellow Taxi Tripdata (Parquet files)
2. **Staging Layer (dbt)** → Cleaned and renamed tables
3. **Combined Layer (dbt)** → Unioned data across months + calculated fields
4. **Mart Layer (dbt)** → `fact_trips` table for reporting
5. **Visualization (Looker Studio)** → Business dashboard for analysis

## 📊 Dashboard

👉 [View the live Looker Studio Dashboard](https://lookerstudio.google.com/reporting/2756cb0b-c6f3-4f88-8a80-353058333c01)

Features:
- Trips Over Time
- Average Trip Duration by Day of Week
- Payment Method Split
- Top Pickup Locations
- Tip vs Fare Scatter Analysis
- Filters for Date Range and Weekend/Weekday

## 🚀 Future Improvements

- Add dimensions for pickup/dropoff zones
- Implement dbt tests (not null, unique, accepted values)
- Deploy incremental models for real-time updates
- Add CI/CD via dbt Cloud or Github Actions

## 📎 Project Links

- [GitHub Project](https://github.com/yesworm/nyc-taxi-analytics) 
- [Live Dashboard](https://lookerstudio.google.com/reporting/2756cb0b-c6f3-4f88-8a80-353058333c01)

---

## 👤 Author

Sam Geyer  
[Personal Portfolio](https://samgeyer.com) | [GitHub](https://github.com/yesworm)