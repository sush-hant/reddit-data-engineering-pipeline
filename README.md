# Reddit Data Pipeline Engineering (AWS End-to-End)

An end-to-end Reddit data engineering project demonstrating how to extract data from the Reddit API, orchestrate jobs with Apache Airflow & Celery, store and transform data using Amazon S3, AWS Glue, Amazon Athena, and load into Amazon Redshift for analytics.

---

## 🚀 Features

- **Data Extraction**  
  - Uses [PRAW](https://praw.readthedocs.io/) (Python Reddit API Wrapper) to pull new posts & comments from a target subreddit.  
- **Orchestration**  
  - Apache Airflow & Celery for scheduling, task distribution, and retries.  
  - PostgreSQL as the Airflow metadata backend.  
- **Storage & Cataloging**  
  - Raw data landing in Amazon S3 (Bronze zone).  
  - AWS Glue Crawler to catalog raw objects into the Glue Data Catalog.  
  - Glue ETL Jobs to clean/transform raw data (Silver zone).  
- **Query & Analytics**  
  - Amazon Athena for ad hoc querying directly against S3.  
- **Infrastructure as Code**  
  - Docker Compose for local testing of Airflow + Postgres + Celery.  

---

