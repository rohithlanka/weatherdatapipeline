# Weather Data Pipeline

This project aims to fetch weather data from an API, load it into a Snowflake data warehouse, perform data transformations using DBT (Data Build Tool), and orchestrate the entire workflow using Apache Airflow running in a Docker container.

## Project Overview

1. **Data Ingestion**: A Python script is used to fetch weather data from openweather API.

2. **Data Loading**: The fetched data is loaded into a Snowflake data warehouse using appropriate Snowflake utilities or libraries.

3. **Data Transformation**: DBT (Data Build Tool) is employed to perform data transformations on the loaded data within the Snowflake environment. This includes defining models, writing SQL transformations, and managing the transformation pipeline.

4. **Workflow Orchestration**: Apache Airflow is used to orchestrate the entire data pipeline workflow. An Airflow DAG (Directed Acyclic Graph) is defined to execute the Python script for data ingestion, trigger the data loading process, and run the DBT models for data transformation.

5. **Docker Containerization**: The Airflow environment is containerized using Docker, allowing for consistent and reproducible deployments across different environments.

## Technologies Used

- Python
- Snowflake Data Warehouse
- DBT (Data Build Tool)
- Apache Airflow
- Docker

## Setup and Usage

1. Ensure you have Docker and Docker Compose installed on your machine.
2. Clone the repository: `git clone https://github.com/rohithlanka/weatherdatapipeline.git`
3. Install the required dependencies (Python packages, DBT, Airflow, Docker, etc.).
4. Configure the project settings:
   - Set up the API credentials and endpoint for data ingestion.
   - Configure the Snowflake connection details.
   - Set up the DBT project and define the data models.
   - Configure the Airflow connections and variables.
5. Navigate to the repository directory and run docker-compose up.
6. Once all containers are up and running, access the Airflow web UI and trigger the DAG execution to run the entire data pipeline.
7. After the ELT process completes, you can access the snowflake UI to view the transformed and old tables.

